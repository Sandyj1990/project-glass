import { next } from '@vercel/functions';
import { mintCookie, parseCookie, sha256Hex, verifyCookie } from './lib/auth';
import { challengeHtml } from './lib/challenge';

const COOKIE = 'glass_v1';
const SESSION_SECONDS = 86400;

const SECURITY_HEADERS: Record<string, string> = {
  'Content-Security-Policy': [
    "default-src 'self'",
    "script-src 'self' 'unsafe-inline' https://cdn.tailwindcss.com",
    "style-src 'self' 'unsafe-inline' https://fonts.googleapis.com",
    "font-src 'self' https://fonts.gstatic.com",
    "img-src 'self' data: https://socialassets.impetusz0.de https://i.ytimg.com https://yt3.ggpht.com https://d2xsxph8kpxj0f.cloudfront.net",
    "connect-src 'self'",
    "frame-src 'self' https://www.youtube-nocookie.com https://www.youtube.com https://socialassets.impetusz0.de",
    "frame-ancestors 'none'",
    "base-uri 'self'",
    "form-action 'self'",
  ].join('; '),
  'X-Frame-Options': 'DENY',
  'X-Content-Type-Options': 'nosniff',
  'Referrer-Policy': 'strict-origin-when-cross-origin',
  'Permissions-Policy': 'camera=(), microphone=(), geolocation=(), interest-cohort=()',
  'Strict-Transport-Security': 'max-age=63072000; includeSubDomains; preload',
  'Cross-Origin-Opener-Policy': 'same-origin',
  'Cross-Origin-Resource-Policy': 'same-origin',
  'Access-Control-Allow-Origin': 'null',
};

export const config = {
  matcher: ['/((?!assets/|favicon|robots.txt|.well-known/).*)'],
  runtime: 'edge',
};

export default async function middleware(req: Request): Promise<Response> {
  const hash = process.env.GLASS_PW_HASH;
  const sig = process.env.GLASS_SIG_SECRET;

  if (!hash || !sig) {
    return new Response('Auth not configured. Contact ops.', {
      status: 503,
      headers: { 'content-type': 'text/plain; charset=utf-8', ...SECURITY_HEADERS },
    });
  }

  const url = new URL(req.url);
  const cookieValue = parseCookie(req.headers.get('cookie') ?? '', COOKIE);

  if (cookieValue && (await verifyCookie(cookieValue, sig))) {
    return next({ headers: SECURITY_HEADERS });
  }

  if (req.method === 'POST' && url.pathname === '/__auth') {
    const form = await req.formData();
    const pw = String(form.get('password') ?? '');
    if (pw && (await sha256Hex(pw)) === hash) {
      const token = await mintCookie(sig);
      const headers = new Headers(SECURITY_HEADERS);
      headers.set('Location', '/');
      headers.append(
        'Set-Cookie',
        `${COOKIE}=${token}; HttpOnly; Secure; SameSite=Strict; Path=/; Max-Age=${SESSION_SECONDS}`,
      );
      return new Response(null, { status: 303, headers });
    }
    return Response.redirect(new URL('/?e=1', req.url), 303);
  }

  const showError = url.searchParams.get('e') === '1';
  return new Response(challengeHtml(showError), {
    status: 401,
    headers: { 'content-type': 'text/html; charset=utf-8', ...SECURITY_HEADERS },
  });
}
