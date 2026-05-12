# Project Glass · Security Remediation · v0.1 spec

**Author** · Kushan Shah · **Date** · 2026-05-04 · **Owner** · Fynd · **Target** · `glass.jiocommerce.io`

A remediation spec for the security findings surfaced by passive recon of `glass.jiocommerce.io` on 2026-05-03. Covers the bypassable client-side gate, missing security headers, third-party JS in production, and lower-severity hygiene items. Scope is the deployed site only; the build pipeline and source repo are out of scope for this spec.

---

## §0 · Status as of 2026-05-04 · 6 of 7 findings closed

Production verified post-merge. Post-remediation pen-test report archived at [`docs/audits/glass-security-report-2026-05-04.pdf`](audits/glass-security-report-2026-05-04.pdf) (also rendered as HTML for diffing).

| § | Sev | Finding | Status | Closed by |
|---|---|---|---|---|
| §3.1 | 🟥 CRIT | Client-side gate bypassable | ✅ Closed | PR #63 |
| §3.2 | 🟥 CRIT | SHA-256 hash published in JS | ✅ Closed | PR #63 |
| §3.3 | 🟧 HIGH | Missing security headers | ✅ Closed | PR #63 |
| §3.4 | 🟧 HIGH | Wildcard CORS | ✅ Closed | PR #63 |
| §3.5 | 🟨 MED | Third-party JS in production | ⏳ Deferred | Step 2 |
| §3.6 | 🟨 MED | robots.txt comment leak | ✅ Closed | PR #66 |
| §3.7 | 🟦 LOW | Hygiene cluster | ✅ Closed | PR #63 + #66 |

**Estimated header posture: A+** (all 8 standard security headers present including CSP with `frame-ancestors 'none'`, HSTS preload, COOP/CORP same-origin). Mozilla Observatory grade run pending; spec §6 acceptance otherwise verified by the runnable transcript in the audit PDF.

The site is no longer in the *"treat as public"* category. §3.5 (Tailwind CDN + Google Fonts) is the sole open item — by design, since it's build-pipeline work rather than a security fix; supply-chain risk persists until self-host lands.

---

## §1 · Why now

Project Glass is framed in its own overlay as *"a private workspace … proprietary, commercially sensitive and protected by copyright and confidentiality obligations"* with an explicit ban on screenshotting and onward sharing. The current implementation does not match that framing. Two findings make the gate non-load-bearing for any motivated adversary:

1. The full 53 KB / 934-line HTML payload — title, every `<section>`, every visible string — ships in the response body **before** `auth.js` runs. The password overlay is painted client-side over content already in the DOM. `curl https://glass.jiocommerce.io/` returns the workspace verbatim.
2. The password's SHA-256 hash is published in `auth.js` line 3. Single round, unsalted. Any dictionary phrase or common-pattern password ≤ ~9 chars from a known charset is brute-forceable offline on a single consumer GPU in minutes to hours.

Until #1 is fixed, the site should be treated as if it were public. This spec resolves that and the supporting weaknesses in one bounded change.

---

## §2 · Decision · own the gate via Routing Middleware, then layer the rest

Four viable shapes for the auth fix:

| Approach | What it looks like | Why we are / are not picking it |
|---|---|---|
| **Harden the client gate** | Stronger KDF (argon2 / PBKDF2 with high iterations + salt), gate insertion before `<body>` content, server-side rendering of empty shell. | Still bypassable. Any client-side gate is theatre against `curl` + JS-disabled clients. Rejected. |
| **Vercel Password Protection** | Edge-level password gate. No HTML reaches an unauthenticated client. Configured in Vercel dashboard, no code change. | Eliminates findings §3.1 + §3.2 in one step. But the challenge page is **Vercel-branded and not white-labelable** — no API for logo, copy, colors, or template overrides. Loses the Fynd / Project Glass branding and the confidentiality language that the current overlay carries. Rejected as the primary control because the gate copy is load-bearing. |
| **Vercel Routing Middleware** ✓ | `middleware.ts` at the project root runs before the CDN cache on every request. Returns a fully-branded 401 challenge page to unauthenticated clients; sets a signed HttpOnly cookie on auth success; passes authenticated requests through with security headers injected. Framework-agnostic — works on the existing static-HTML layout, no Next.js or rewrite required. | Same security properties as Vercel Password Protection (no HTML reaches unauth clients, hash lives server-side in env vars). Adds full visual control over the challenge page so it matches the landing register exactly (§A.5). Cost: ~80 lines of middleware code in one file. **Picked** as the primary control. |
| **Vercel Authentication / SSO** | Identity-bound auth via Vercel team membership. Per-person audit trail. | Stronger than the picked option (auditable, revocable per person), but also Vercel-branded challenge UI, and requires every viewer to have a Vercel account. Future option for a v0.2 if per-person audit becomes a requirement. Not v0.1. |

The remaining findings (CSP and friends, third-party JS, CORS, robots.txt comments) get fixed via configuration changes that are independent of the auth choice — and §3.3 partially folds into the middleware (header injection happens on the same `next()` call that passes the request through).

---

## §3 · Findings, severity-ordered

### §3.1 · 🟥 CRITICAL · Client-side auth gate is fully bypassable

**Evidence.** `curl -s https://glass.jiocommerce.io/ | wc -l` returns 934 lines including `<title>Fynd × Reliance Retail · The AI Frontier</title>` and every section. `auth.js` only paints a `position: fixed; z-index: 99999` overlay over already-loaded content. Bypass methods, no exploit needed:
- `curl` / `wget` / any non-browser client
- DevTools → disable JS → reload
- DevTools → Elements → delete `#__fyndrrl_gate`
- View Source (`Ctrl-U`) — JS does not run for source view
- Headless scrapers with JS off
- The documented dev bypass: `sessionStorage.setItem('fyndrrl_auth_v1', '1')`

**Fix.** Add `middleware.ts` at the project root (see §A.4). Middleware runs at the Vercel edge before the CDN cache; returns the branded 401 challenge to anyone without a valid session cookie. Delete `auth.js`, the inline gate styles, and the documented `sessionStorage` dev bypass from team docs (the bypass becomes the password itself once the gate is server-side).

**Acceptance.** `curl -s -o /dev/null -w "%{http_code}\n" https://glass.jiocommerce.io/` returns `401` from any unauthenticated origin. The 401 body is the branded challenge page (~3 KB inline HTML, no third-party assets). DevTools Network tab on a fresh browser shows no workspace HTML before authentication. `curl -s https://glass.jiocommerce.io/jcp/ -H "Cookie: glass_v1=invalid"` also returns `401`.

---

### §3.2 · 🟥 CRITICAL · Password hash is offline-brute-forceable

**Evidence.** `auth.js` line 3:
```
HASH = '813a2ea5ae33d25893a3ead376ec72dafd33addcbec0fdbf1cb40a440348391e'
```
Single-round, unsalted SHA-256. SHA-256 throughput is ~10 GH/s on a single consumer GPU. An attacker downloads `auth.js` once (no rate limit applies), then runs hashcat against rockyou + a custom wordlist seeded with `fynd / glass / reliance / jio / project / apex / confidential / RRL …`. Dictionary phrases fall in minutes; common-pattern passwords ≤ 9 chars in hours.

**Fix.** Same as §3.1 — the middleware reads `process.env.GLASS_PW_HASH` server-side. The hash never ships to any client. Set the env var via `vercel env add GLASS_PW_HASH production`. Also add `GLASS_SIG_SECRET` (32 random bytes, hex) for signing the session cookie so a stolen cookie value cannot be forged offline.

**Acceptance.** No password material (hash, salt, KDF parameters, or ciphertext) is reachable in any asset served by the deployment. `curl -s https://glass.jiocommerce.io/auth.js` returns `404`. `curl -s https://glass.jiocommerce.io/ | grep -iE "[0-9a-f]{64}"` returns no matches (no 64-hex-char strings anywhere in served HTML or JS).

---

### §3.3 · 🟧 HIGH · Zero security headers beyond HSTS

**Evidence.** Headers present on `/`:
```
strict-transport-security: max-age=63072000
access-control-allow-origin: *
x-robots-tag: noindex, nofollow, noarchive, nosnippet, noimageindex, notranslate
server: Vercel
```
**Missing**, with concrete impact for this site:

| Header | Why it matters here |
|---|---|
| `Content-Security-Policy` | No defence vs XSS or third-party script compromise. With Tailwind CDN and Google Fonts pulled inline (§3.5), supply-chain compromise → full XSS. |
| `X-Frame-Options` / `frame-ancestors` | Page can be iframed by any origin. Combined with §3.1, a phishing page can iframe glass and harvest already-loaded content. |
| `Referrer-Policy` | Browsers leak full URL paths (`/jcp`, `/impetus`, `/granary` …) in `Referer` to Google Fonts, Tailwind CDN, and outbound clicks. Path names are sensitive metadata for a confidential workspace. |
| `X-Content-Type-Options: nosniff` | MIME sniffing allowed. |
| `Permissions-Policy` | No restriction on camera / mic / geolocation. |
| `Cross-Origin-Opener-Policy` / `COEP` / `CORP` | No cross-origin isolation. |

**Fix.** Headers are injected by the middleware on every authenticated `next()` response (see §A.4) — keeps headers and auth in one place. Asset graph is small (self + `fonts.googleapis.com` + `fonts.gstatic.com` + `cdn.tailwindcss.com` until §3.5 lands), so a tight CSP is feasible:

```ts
{
  source: '/(.*)',
  headers: [
    { key: 'Content-Security-Policy', value: [
      "default-src 'self'",
      "script-src 'self' 'unsafe-inline' https://cdn.tailwindcss.com",
      "style-src 'self' 'unsafe-inline' https://fonts.googleapis.com",
      "font-src 'self' https://fonts.gstatic.com",
      "img-src 'self' data:",
      "connect-src 'self'",
      "frame-ancestors 'none'",
      "base-uri 'self'",
      "form-action 'self'",
    ].join('; ') },
    { key: 'X-Frame-Options', value: 'DENY' },
    { key: 'X-Content-Type-Options', value: 'nosniff' },
    { key: 'Referrer-Policy', value: 'no-referrer' },
    { key: 'Permissions-Policy', value: 'camera=(), microphone=(), geolocation=(), interest-cohort=()' },
    { key: 'Cross-Origin-Opener-Policy', value: 'same-origin' },
    { key: 'Cross-Origin-Resource-Policy', value: 'same-origin' },
  ],
}
```

After §3.5 (drop Tailwind CDN, self-host fonts), CSP tightens further to `script-src 'self'` and `font-src 'self'`.

**Acceptance.** `curl -sI https://glass.jiocommerce.io/` shows all seven headers. Mozilla Observatory grade ≥ A-.

---

### §3.4 · 🟧 HIGH · `Access-Control-Allow-Origin: *` on confidential HTML

**Evidence.** Every response carries wildcard CORS, including the gated workspace HTML. Reproducible with `curl -sI -H "Origin: https://evil.example" https://glass.jiocommerce.io/` → response includes `access-control-allow-origin: *`.

**Impact.** CORS does not block top-level navigation, but it does allow any malicious site loaded in a victim's browser to `fetch('https://glass.jiocommerce.io/jcp/')` and exfil the response body cross-origin. Directly contradicts the legal language in the overlay.

**Fix.** Drop the header. The site has no public APIs and same-origin assets do not require CORS at all. Remove from `vercel.ts` headers / any framework middleware setting it.

**Acceptance.** `curl -sI https://glass.jiocommerce.io/ | grep -i access-control` returns no output.

---

### §3.5 · 🟨 MEDIUM · Third-party JS in production

**Evidence.** Page loads `https://cdn.tailwindcss.com/` (302 → `3.4.17`), executing arbitrary JS in the workspace origin. Console emits the upstream warning: *"cdn.tailwindcss.com should not be used in production."* Google Fonts loaded directly from `fonts.googleapis.com` + `fonts.gstatic.com`.

**Impact.**
- **Supply chain.** Compromise of `cdn.tailwindcss.com` (or DNS / Cloudflare hijack) gives the attacker JS execution on glass. With no CSP (§3.3), no second line.
- **Telemetry.** Tailwind Labs and Google see every request — IP, UA, Referer (path) — to a confidential workspace.

**Fix.**
1. Install Tailwind as a build step. Repo already has a `tools/` convention; add a `npm` / `pnpm` build that produces `style.css` with the required utilities and drops the runtime script.
2. Self-host Inter (weights 400/500/600/700/800/900) and JetBrains Mono (400/500/600) as `woff2` files in `/assets/fonts/`. ~9 files total. Add `@font-face` declarations to `style.css`.
3. Remove `<script src="https://cdn.tailwindcss.com">` and the Google Fonts `<link>` from the page.

**Acceptance.** `curl -s https://glass.jiocommerce.io/ | grep -E "tailwindcss\.com|fonts\.googleapis|fonts\.gstatic"` returns no matches. Network panel on first load shows zero third-party origins.

---

### §3.6 · 🟨 MEDIUM · `robots.txt` body leaks internal framing

**Evidence.**
```
# Internal property · Fynd × Reliance Retail register
# Not for public consumption. All crawlers, all paths, no exceptions.

User-agent: *
Disallow: /
```
Adversaries grep robots.txt comments for "interesting target" signals. The `Disallow: /` is correct; the comment names both parent orgs and confirms the property is intentionally hidden — a recon win.

**Fix.** Strip comments. Keep:
```
User-agent: *
Disallow: /
```

**Acceptance.** `curl -s https://glass.jiocommerce.io/robots.txt | grep '^#'` returns no output.

---

### §3.7 · 🟦 LOW · Hygiene

| # | Finding | Fix |
|---|---|---|
| 1 | No `/.well-known/security.txt` | Add per RFC 9116 with a Fynd security contact email and a 12-month `Expires`. |
| 2 | `HSTS` lacks `includeSubDomains; preload` | Update to `max-age=63072000; includeSubDomains; preload` once all `*.jiocommerce.io` subdomains are confirmed HTTPS-only. |
| 3 | `<title>` set pre-auth | Resolved by §3.1 (no HTML reaches unauth clients). |
| 4 | `server: Vercel` and `x-vercel-id` info disclosure | Accept. Minor. Removing requires platform-level workaround not worth the cost. |
| 5 | Console verbose: input lacks `autocomplete` attribute | Add `autocomplete="off"` (or `current-password`) to the password input — moot once §3.1 lands. |

---

## §4 · Out of scope

- The build pipeline and source repository for Glass.
- Active testing (auth bypass attempts on Vercel Password Protection itself, fuzzing, injection probes). Findings here are passive-recon-only.
- Subdomain enumeration across `*.jiocommerce.io`. The Let's Encrypt cert lists only `glass.jiocommerce.io` as a SAN; broader DNS / CT-log enumeration is a separate exercise.
- Per-person audit logging of who accessed what page, when. Resolved only by Vercel SSO (the §2 future option), not by Vercel Password Protection.

---

## §5 · Fix order

1. **§3.1 + §3.2 + §3.3 + §3.4** — add `middleware.ts` per §A.4. Set `GLASS_PW_HASH` and `GLASS_SIG_SECRET` env vars in Vercel (production env only, encrypted). Inject security headers and drop wildcard CORS in the same `next()` call. Delete `auth.js`. Single PR, ~80 lines of new code, eliminates both criticals and both highs.
2. **§3.5** — Tailwind build step + self-hosted fonts. Largest change; do after #1 lands so the middleware's CSP can tighten to `script-src 'self'` and `font-src 'self'`.
3. **§3.6 + §3.7** — robots cleanup, security.txt, HSTS update, autocomplete. Single PR, mechanical.

After step 1, the site is no longer "treat as public." After step 3, Mozilla Observatory grade should be A or A+.

---

## §6 · Acceptance · whole spec

- `curl -s -o /dev/null -w "%{http_code}\n" https://glass.jiocommerce.io/` → `401` from unauthenticated origin.
- `curl -sI https://glass.jiocommerce.io/` shows: HSTS with preload, CSP, X-Frame-Options DENY, nosniff, Referrer-Policy no-referrer, Permissions-Policy, COOP same-origin, CORP same-origin. No `Access-Control-Allow-Origin`.
- `curl -s https://glass.jiocommerce.io/ | grep -E "tailwindcss\.com|fonts\.google"` → no matches.
- `curl -s https://glass.jiocommerce.io/robots.txt | grep '^#'` → no matches.
- `curl -s https://glass.jiocommerce.io/.well-known/security.txt` → 200 with valid RFC 9116 body.
- Mozilla Observatory: A or A+.

---

## §A · Appendix · middleware shape

### §A.0 · Roles · the lock vs. the room

The middleware is a thin gatekeeper, **not** a replacement for any workspace page. Two distinct jobs, two distinct files:

| Component | Job | Lifecycle |
|---|---|---|
| `middleware.ts` | **Lock.** On every matched request: check the cookie. No cookie → return the 401 challenge HTML inline. Valid cookie → call `next()` and step out of the way. | Runs as a Function on every matched request, before the CDN cache. |
| `index.html`, `jcp/index.html`, `impetus/index.html`, … | **Rooms.** The actual workspace content. Unchanged by this spec except for one mechanical edit: remove `<script src="/auth.js">`. | Static files, served from the CDN cache once `next()` fires. |

The middleware never serves workspace HTML itself. Pushing the 50+ workspace pages through a Function on every request would bypass the CDN, slow every page load, and add Function invocation cost to every authenticated reader scrolling the deck.

What this means in practice:
- Every existing page (`/`, `/jcp/`, `/impetus/`, `/granary/`, `/agents/*`, etc.) continues to exist as a static file and continues to be served from the CDN — just behind the lock now.
- Adding new workspace pages requires **no middleware change**. The matcher (§A.2) catches everything by default; the next-deployed page is gated automatically.
- Existing authoring conventions and canonical-source rules — Presentation Mode wiring, nav sweep via `tools/site_chrome.py`, Path-to-L4 sweep, org-stats hydration — all unchanged. Middleware sits orthogonal to the page lifecycle.

**One thing not to do.** Do not collapse the challenge page back into the landing's `<body>` and gate it client-side again. That re-introduces §3.1 — the bug this spec is fixing. The challenge HTML lives only in the middleware function; the landing's `<body>` only ever ships to authenticated clients.

### §A.1 · Files added / changed

```
glass/
├── middleware.ts          ← NEW · the gate (~80 lines)
├── auth.js                ← DELETE
├── index.html             ← edit: remove <script src="/auth.js">
├── jcp/index.html         ← edit: same
├── …                      ← edit: same on every page
└── vercel.json            ← optional · only if not using vercel.ts
```

The per-page edit is mechanical — a `sed` over `<script src="/auth.js"></script>` across all `index.html` files. Since the existing site already has sweep tooling (`tools/inject_chrome.py` etc.), this can be added as a one-time `tools/strip_client_auth.py` run.

### §A.2 · Runtime + matcher

```ts
export const config = {
  matcher: ['/((?!assets/|favicon|robots.txt|.well-known/).*)'],
  runtime: 'edge',
};
```

`edge` runtime is sufficient — auth needs only `crypto.subtle` (SHA-256 + HMAC) and standard `Request` / `Response`. Cold start is sub-50ms; under Fluid Compute, warm responses are sub-millisecond. Asset paths (`/assets/`, `/favicon`, `robots.txt`, `/.well-known/`) bypass the gate so the challenge page can load its own logo and security.txt is reachable to outsiders.

### §A.3 · Cookie shape

| Property | Value | Why |
|---|---|---|
| Name | `glass_v1` | Versioned so a future cookie-format change doesn't lock anyone out indefinitely. |
| Value | `<random-token>.<hmac-sha256(token, GLASS_SIG_SECRET)>` | Signed so a forged or stolen value can't be replayed. |
| `HttpOnly` | yes | Not readable by client JS — defends against XSS exfiltration. |
| `Secure` | yes | HTTPS only. |
| `SameSite` | `Strict` | Not sent on cross-site requests — defends against CSRF + cross-site cookie leaks. |
| `Path` | `/` | Covers all routes. |
| `Max-Age` | `86400` (24h) | Short-lived so an abandoned session expires the same day. |

### §A.4 · The middleware

```ts
// middleware.ts
import { next } from '@vercel/functions';

const COOKIE = 'glass_v1';
const HASH = process.env.GLASS_PW_HASH!;          // sha256(password), hex
const SIG  = process.env.GLASS_SIG_SECRET!;       // 32 random bytes, hex

const SECURITY_HEADERS = {
  'Content-Security-Policy': [
    "default-src 'self'",
    "script-src 'self' 'unsafe-inline' https://cdn.tailwindcss.com",
    "style-src 'self' 'unsafe-inline' https://fonts.googleapis.com",
    "font-src 'self' https://fonts.gstatic.com",
    "img-src 'self' data:",
    "connect-src 'self'",
    "frame-ancestors 'none'",
    "base-uri 'self'",
    "form-action 'self'",
  ].join('; '),
  'X-Frame-Options': 'DENY',
  'X-Content-Type-Options': 'nosniff',
  'Referrer-Policy': 'no-referrer',
  'Permissions-Policy': 'camera=(), microphone=(), geolocation=(), interest-cohort=()',
  'Strict-Transport-Security': 'max-age=63072000; includeSubDomains; preload',
  'Cross-Origin-Opener-Policy': 'same-origin',
  'Cross-Origin-Resource-Policy': 'same-origin',
};

export const config = {
  matcher: ['/((?!assets/|favicon|robots.txt|.well-known/).*)'],
  runtime: 'edge',
};

export default async function middleware(req: Request) {
  const url = new URL(req.url);
  const cookie = parseCookie(req.headers.get('cookie') ?? '', COOKIE);
  const error = url.searchParams.get('e') === '1';

  if (cookie && await verifyToken(cookie, SIG)) {
    return next({ headers: SECURITY_HEADERS });
  }

  if (req.method === 'POST' && url.pathname === '/__auth') {
    const form = await req.formData();
    const pw = String(form.get('password') ?? '');
    if (await sha256Hex(pw) === HASH) {
      const token = await mintToken(SIG);
      return new Response(null, {
        status: 303,
        headers: {
          Location: '/',
          'Set-Cookie': `${COOKIE}=${token}; HttpOnly; Secure; SameSite=Strict; Path=/; Max-Age=86400`,
          ...SECURITY_HEADERS,
        },
      });
    }
    return Response.redirect(new URL('/?e=1', req.url), 303);
  }

  return new Response(challengeHtml(error), {
    status: 401,
    headers: { 'content-type': 'text/html; charset=utf-8', ...SECURITY_HEADERS },
  });
}
```

`sha256Hex`, `mintToken`, `verifyToken`, `parseCookie`, and `challengeHtml` are small helpers — full code in the implementation PR. `mintToken` / `verifyToken` are HMAC-SHA-256 over a random 16-byte token with `GLASS_SIG_SECRET` as the key.

### §A.5 · Challenge page · matches the landing register exactly

The current `auth.js` overlay uses near-but-not-quite tokens (`#1a1a1c`, `#d4d4d2`). The new middleware-served challenge page uses the canonical landing tokens directly so visitor and authenticated states feel like one site:

| Token | Value | Used on landing for | Used on challenge for |
|---|---|---|---|
| `--bg` | `#FFFFFF` | Page background | Page background |
| `--ink` | `#0A0A0A` | Body text, hero | Heading, button hover |
| `--ink-muted` | `#6B7280` | Secondary copy | Confidentiality body |
| `--caption` | `#4B5563` | Eyebrows, captions | "CONFIDENTIAL" eyebrow |
| `--accent` | `#6B5BD6` | Accent phrases, links | Submit button, hero halo |
| `--accent-soft` | `#EDE9FE` | Tinted highlights | Input focus ring |
| `--border` | `#D4D4D4` | Card / section dividers | Input border |
| Font · sans | Inter 400/500/600/700 | Body, hero | Body, heading, button |
| Font · mono | JetBrains Mono 400/500 | Eyebrows, captions, tags | Eyebrow, "© 2026" line |
| Hero halo | `radial-gradient(ellipse at top, rgba(107,91,214,0.08) 0%, transparent 60%)` | `.hero-grad` | Behind the form |

**Layout · mirrors the landing hero.** Same vertical rhythm: 32px page padding, brand row at top (Fynd logo · separator · `PROJECT GLASS` mono eyebrow), centred form column max 380 px wide, confidentiality block centred max 760 px wide below — identical proportions to the landing's hero/impact split. The hero halo (`.hero-grad`) sits behind the form so the page reads as the first slide of the deck rather than a separate utility screen.

**Typography · landing register, no marketing voice.**
- Heading on the form: *"Project Glass"* — Inter 700, `clamp(40px, 6vw, 64px)`, line-height 0.95, `--ink`. (Smaller cousin of the landing's `clamp(48px, 8vw, 96px)` display.)
- Subhead under heading: *"Authorised access only · Fynd × RRVL · JPL"* — JetBrains Mono 12px uppercase 0.04em, `--caption`. Same treatment as `.hero-subhead` on landing.
- Input placeholder: *"Access phrase"* (not "Password" — register-consistent with the existing overlay).
- Button label: *"Continue"* on default state, *"Verifying…"* during the 303 round-trip.
- Error line on incorrect submit: *"Access phrase did not match."* — `--red` (`#DC2626`), 13px, no exclamation.
- Confidentiality body: lifted verbatim from the current overlay — already in the right register, already legally vetted. JetBrains Mono 11px eyebrow `· CONFIDENTIAL · AUTHORISED USE ONLY` matches `.lens-eyebrow` on landing.

**Component reuse.**
- Input field: same `border: 1px solid var(--border); border-radius: 10px; padding: 16px;` as `.filter-chip` and `.platform-card` ride on. Focus state borrows `border-color: var(--ink); box-shadow: 0 1px 3px rgba(0,0,0,0.04);` from the existing form pattern.
- Submit button: solid `--ink` background, white text, `--accent` on hover — same as the `.filter-chip.active` pattern, scaled up.
- Brand row: identical to the landing's `<header>` (Fynd logo · `×` separator · `RRVL · JPL` mono lockup).

**ASCII mock — same proportions as the landing hero:**
```
┌──────────────────────────────────────────────────────────────────────┐
│ ◆ Fynd  ×  RRVL · JPL                                                │
│                                                                      │
│                                                                      │
│                          PROJECT GLASS                               │
│                                                                      │
│                          ┌──────────────────────┐                    │
│                          │  Access phrase       │                    │
│                          └──────────────────────┘                    │
│                          ┌──────────────────────┐                    │
│                          │      Continue        │                    │
│                          └──────────────────────┘                    │
│                                                                      │
│                                                                      │
│           · CONFIDENTIAL · AUTHORISED USE ONLY ·                     │
│                                                                      │
│   Project Glass is a private workspace operated by Shopsense Retail  │
│   Technologies Limited (Fynd) and its partners …                     │
│                                                                      │
│                  © 2026 SHOPSENSE RETAIL TECHNOLOGIES                │
└──────────────────────────────────────────────────────────────────────┘
       ⤷ same hero halo gradient as the landing's §0
```

**Net visual outcome.** A first-time visitor sees a screen that reads as the first slide of the same deck — same fonts, same colors, same proportions, same brand lockup, same confidentiality voice — rather than a generic Vercel auth challenge or a vendor-shaped login form. After successful auth, the landing renders without any visual transition penalty because both pages share the `:root` token block.

### §A.6 · Local development · two servers, one chosen by what you're touching

Today's CLAUDE.md documents one local-dev path:

```bash
python3 -m http.server 8765
# open http://localhost:8765/<route>
```

…with a `sessionStorage` bypass to dismiss the client-side overlay. After Step 1 lands, that bypass is dead code (the overlay is gone) and the local picture splits into two paths chosen by what you're working on.

#### §A.6.1 · `python3 -m http.server` — content / styles / sweeps

Unchanged. Use it for everything that doesn't touch the gate:
- editing page content, copy, styles
- running `tools/inject_chrome.py`, `tools/inject_present.py`, `tools/inject_path_to_l4.py`, `tools/build_org_data.py`, etc.
- visual checks via Chrome DevTools MCP `take_screenshot` / `evaluate_script`

`http.server` is a static file server — it does not run middleware. Pages render directly, no gate. Faster iteration than today (no overlay to dismiss), at the cost of not exercising the auth path.

```bash
python3 -m http.server 8765
# open http://localhost:8765/   →  workspace renders immediately, no gate
```

**Delete from CLAUDE.md** as part of the Step 1 PR:

```js
sessionStorage.setItem('fyndrrl_auth_v1', '1'); location.reload();   // ← obsolete
```

#### §A.6.2 · `vercel dev` — gate, challenge page, cookie flow, CSP

For anything middleware-adjacent — challenge page styling, cookie behavior, CSP debugging, headers, error states — switch to `vercel dev`. This actually runs the middleware against your local files.

One-time setup after env vars are set in Vercel:

```bash
vercel link                       # connect this folder to the Vercel project
vercel env pull .env.local        # pull GLASS_PW_HASH + GLASS_SIG_SECRET to .env.local
```

Then for each session:

```bash
vercel dev
# open http://localhost:3000/   →  branded challenge appears, enter password,
#                                  cookie set, workspace loads
```

**Add to `.gitignore`** (verify, then add only if missing) as part of the Step 1 PR:

```
.env.local
.env*.local
.vercel
```

#### §A.6.3 · Which to pick · matrix

| When you're working on… | Use | Gate runs? | Why |
|---|---|---|---|
| Page content, copy, styles, sweeps | `python3 -m http.server` | No | Faster · same workflow as today, minus the overlay |
| Diagram work, SVG, agent pages | `python3 -m http.server` | No | Same |
| Middleware code, helpers | `vercel dev` | Yes | Need actual function execution |
| Challenge page styling | `vercel dev` | Yes | Only served by middleware on 401 |
| Cookie behavior, expiry, signing | `vercel dev` | Yes | Need real `Set-Cookie` round-trip |
| CSP / headers debugging | `vercel dev` | Yes | Headers come from middleware |
| Pre-merge final visual check | `vercel dev` | Yes | Mirror production behavior |

#### §A.6.4 · Preview deployments

Vercel runs the same middleware on preview deployments as on production. Two consequences:

1. **Env vars must be set on the `Preview` environment** in Vercel, not just `Production`. Either:
   - Set `GLASS_PW_HASH` + `GLASS_SIG_SECRET` to the same values across all three environments (`Production`, `Preview`, `Development`) — simplest, lets reviewers use the production password to access preview deploys.
   - Set a different password for `Preview` — stronger isolation, but reviewers need to know two passwords. Recommended only if preview deploys go to a wider audience than production access.
2. **Preview URLs (`*-<hash>-<team>.vercel.app`)** are gated by the same middleware. The 401 challenge appears on preview URLs too. There is no longer a "preview = open" mode.

#### §A.6.5 · Multi-domain note · `reliance-retail-fynd.vercel.app` vs. `glass.jiocommerce.io`

The Vercel project serves two production domains. By default, the middleware runs on both — both URLs get the gate.

If a future requirement needs one domain gated and the other open (e.g., `reliance-retail-fynd.vercel.app` opens publicly, `glass.jiocommerce.io` stays gated), the middleware can branch on `req.headers.get('host')`:

```ts
const host = req.headers.get('host') ?? '';
if (host.startsWith('reliance-retail-fynd')) return next();   // public on this domain
// else: continue to gate
```

Out of scope for v0.1.1 of this spec — both domains gated until product decides otherwise.

### §A.7 · CLAUDE.md · edits to land in the Step 1 PR

The repo's CLAUDE.md (loaded into every assistant session, per the *Read first* list) carries instructions that need updating in the same PR so future sessions don't drift back to the obsolete patterns.

| Section in CLAUDE.md today | Edit |
|---|---|
| `## Local dev` | Replace the single `http.server` block + `sessionStorage` bypass with the two-server matrix from §A.6.3. |
| `## Things to NEVER do` | Add: *"Never reintroduce a client-side `auth.js` or any DOM-painted gate. The middleware at `middleware.ts` is the single source of auth. See `docs/glass-security-spec.md` §3.1 for why."* |
| `## Things to ALWAYS check` | Add: *"After any edit to `middleware.ts`, the challenge HTML, or any header in `vercel.json`: `vercel dev` then `curl -sI http://localhost:3000/` shows the full security-header set + 401 from no-cookie state."* |
| `## Workflow` (the auth-bypass gotcha) | Drop the `fyndrrl_auth_v1` sessionStorage line — no longer applies. |

---

## §B · Appendix · operations runbook

Step-by-step ops for setting, rotating, and debugging the gate after Step 1 (`middleware.ts`) is live. This is the runbook — keep it open in a tab when touching env vars or production deploys.

### §B.1 · Generate the env var values locally

Two values are required: `GLASS_PW_HASH` (SHA-256 of the access phrase, hex) and `GLASS_SIG_SECRET` (32 random bytes, hex). Both 64 hex characters. Never paste plaintext passwords into Slack, email, GitHub, or this repo — only the hash.

#### §B.1.1 · `GLASS_SIG_SECRET` · always generate fresh

```bash
python3 -c "import secrets; print(secrets.token_hex(32))"
```
Prints 64 hex characters. Copy the value. This is the HMAC key that signs the session cookie — rotating it invalidates all live sessions, so set once and leave alone unless you suspect compromise.

#### §B.1.2 · `GLASS_PW_HASH` · two cases

**Case A · Reuse the existing access phrase** (the one that's been on `glass.jiocommerce.io` since launch):

```
GLASS_PW_HASH = 813a2ea5ae33d25893a3ead376ec72dafd33addcbec0fdbf1cb40a440348391e
```

Copy that hash directly. Zero-friction merge — current authorised users keep working unchanged. Pre-spec the hash was published in `auth.js`; post-spec it lives only in `process.env`.

**Case B · Rotate to a new phrase:**

```bash
python3 -c "import getpass, hashlib; print(hashlib.sha256(getpass.getpass('New access phrase: ').encode()).hexdigest())"
```

Prompts for the phrase silently (no terminal echo, no shell history), prints the 64-char hex hash. Use Python's `getpass` rather than shell `read -p` because the latter has cross-shell quirks (`zsh` interprets `-p` as "no coprocess", not "prompt").

**Verify before you forget the phrase** (Case B only):

```bash
python3 -c "import getpass, hashlib; print(hashlib.sha256(getpass.getpass('Re-enter to verify: ').encode()).hexdigest())"
```

Output should byte-match the hash you saved.

#### §B.1.3 · Why not bash/zsh `read -p`

`read -rs -p "prompt: " VAR` works in bash but not zsh (zsh `-p` means "no coprocess"). Cross-shell zsh-friendly form is `read -rs "VAR?prompt: "`. Easier to skip the shell-syntax minefield entirely and use `python3 -c "import getpass, hashlib; …"` — works on any shell, no escaping, no history leak.

### §B.2 · Set in the Vercel dashboard

1. https://vercel.com/dashboard → click the project (`reliance-retail-fynd`).
2. Top nav → **Settings** → left sidebar → **Environment Variables**.
3. Add `GLASS_PW_HASH`:

   | Field | Value |
   |---|---|
   | Key | `GLASS_PW_HASH` |
   | Value | the 64-char hex hash from §B.1.2 |
   | Type | `Encrypted` (default) |
   | Environments | tick **Production**, **Preview**, **Development** |

4. Add `GLASS_SIG_SECRET`:

   | Field | Value |
   |---|---|
   | Key | `GLASS_SIG_SECRET` |
   | Value | the 64-char hex from §B.1.1 |
   | Type | `Encrypted` |
   | Environments | tick **Production**, **Preview**, **Development** |

5. Trigger a redeploy — env-var changes do **not** auto-rebuild. Either:
   - Top nav → **Deployments** → latest production → kebab (⋯) → **Redeploy**. Untick *"Use existing Build Cache"* so the function picks up the new env values.
   - Or merge a PR — the merge triggers a fresh build.

#### §B.2.1 · Per-environment isolation (optional, not v0.1)

Default per spec §A.6.4: same `GLASS_PW_HASH` + `GLASS_SIG_SECRET` across Production / Preview / Development. Reviewers can test preview deploys with the production password.

If a future requirement needs different passwords per env (e.g., preview phrase rotated independently when a reviewer leaves), edit `GLASS_PW_HASH`, untick the offending env, save, then add a new `GLASS_PW_HASH` with the alternate hash and only that env ticked. Same pattern for `GLASS_SIG_SECRET`.

### §B.3 · Verify production after deploy

After the deploy promotes (Deployments tab shows green for the production URL), run from any machine:

```bash
# Status (no cookie) — expect 401, NOT 503
curl -s -o /dev/null -w "%{http_code}\n" https://glass.jiocommerce.io/

# 503 means env vars not picked up — see §B.4.5
# 200 means middleware not running — check the deploy actually used the new build
# 401 means gate is live — continue verification

# Security headers — expect 8+ headers
curl -sI https://glass.jiocommerce.io/ | grep -iE "x-frame|content-security|referrer-policy|permissions-policy|strict-transport|cross-origin|access-control|x-content-type"

# Branded challenge keywords
curl -s https://glass.jiocommerce.io/ | grep -ciE "Project Glass|Access phrase|Confidential · Authorised use only"
# expect: 3+

# Wildcard CORS gone
curl -sI https://glass.jiocommerce.io/ | grep -i "access-control-allow-origin"
# expect: "Access-Control-Allow-Origin: null"

# Old auth.js gone (file deleted, middleware intercepts)
curl -s -o /dev/null -w "%{http_code}\n" https://glass.jiocommerce.io/auth.js
# expect: 401

# Static-asset paths bypass middleware
curl -s -o /dev/null -w "%{http_code}\n" https://glass.jiocommerce.io/robots.txt
# expect: 200

# Wrong-password POST → redirect to /?e=1
curl -s -o /dev/null -w "%{http_code} %{redirect_url}\n" -X POST -d "password=wrong" https://glass.jiocommerce.io/__auth
# expect: 303 https://glass.jiocommerce.io/?e=1

# Deep route also gated (after cleanUrls trailing-slash redirect)
curl -sL -o /dev/null -w "%{http_code}\n" https://glass.jiocommerce.io/jcp/
# expect: 401
```

If all of the above pass, the gate is correctly live.

### §B.4 · Debugging · "Access phrase did not match"

This is the user-visible error when `sha256(input) !== process.env.GLASS_PW_HASH`. Five causes, in descending order of likelihood.

#### §B.4.1 · You forgot the original access phrase (Case A reuse)

Reusing hash `813a2ea5…` from the launch-era `auth.js` — but no one wrote down what the phrase actually was. Symptom: every plausible guess fails.

**Fix:** rotate. Pick a new phrase, recompute the hash via §B.1.2 Case B, update `GLASS_PW_HASH` in Vercel, redeploy, distribute the new phrase to authorised users.

#### §B.4.2 · Hash mismatch · phrase variant

You're typing a phrase that *almost* matches what was hashed — but with a typo, capitalisation difference, smart-quote vs ASCII-quote (paste from chat apps does this), trailing space, or Unicode normalisation difference (NFC vs NFD on macOS pastes from Word).

**Diagnose:** run §B.1.2 Case B with the *exact* phrase you're typing into the gate. Compare the printed hash to the env var value in Vercel. If they differ → it's this. Either rehash with the new phrase OR re-enter exactly what was hashed.

#### §B.4.3 · Trailing whitespace or newline in the env var

Common when pasting from a terminal that includes a trailing newline (e.g. `echo "..." | shasum`). The middleware compares strings exactly — a trailing `\n` on the env var means no input ever matches.

**Diagnose:** in the Vercel dashboard, reveal the `GLASS_PW_HASH` value. Copy it. Run:

```bash
echo -n "<paste-here>" | wc -c
# expect: 64  (64 hex chars, no newline)
# 65 or more → trailing whitespace
# less than 64 → truncated
```

**Fix:** edit the env var, retype just the 64 hex chars, save, redeploy.

#### §B.4.4 · You stored the wrong hash format

`base64`, mixed case, leading `0x`, etc. The middleware expects lowercase hex.

**Fix:** must be 64 lowercase hex characters, nothing else. If you have a hash in another format, recompute via §B.1.2 to get the canonical form.

#### §B.4.5 · 503 instead of "Access phrase did not match"

Different error. Means env vars are missing or unreadable from the function. The middleware fails closed before any password check.

**Diagnose:**
1. Vercel dashboard → Settings → Environment Variables. Confirm both `GLASS_PW_HASH` and `GLASS_SIG_SECRET` are listed AND have **Production** ticked.
2. Vercel dashboard → Deployments → latest production. Was it built **after** you set the env vars? If before, redeploy.
3. Check the deploy log for the function — look for "ENV" lines confirming the vars were available at build time.

#### §B.4.6 · Verifying the fix

After any env-var or hash change, redeploy then run §B.3 verification block. The wrong-password POST line should still return `303 → /?e=1`. The right-password POST should return `303 → /` plus a `Set-Cookie: glass_v1=…`. Test the right-password path in a browser (not curl — curl puts the phrase in shell history; or use `printf` with stdin redirect).

### §B.5 · Rotating the access phrase

Steps to change the password without forcing all users out simultaneously *(soft rotation is not supported in v0.1 — every rotation invalidates nothing on the cookie side, but every old phrase stops working immediately)*:

1. Pick a new phrase. Compute the hash via §B.1.2 Case B.
2. Vercel dashboard → Settings → Environment Variables → edit `GLASS_PW_HASH` → paste new hash → save.
3. Trigger a redeploy (§B.2 step 5).
4. Distribute the new phrase to authorised users via secure channel.
5. Wait for the old session cookies to expire naturally (24h) — there is no global "log out everyone" button. If you need immediate global logout, also rotate `GLASS_SIG_SECRET` (every signed cookie becomes invalid the moment the deploy promotes with the new secret).

### §B.6 · Rotating `GLASS_SIG_SECRET`

When to rotate:
- Suspected compromise of the env var (e.g. someone with dashboard access leaves the team).
- You want to force every active session to re-authenticate immediately.

Steps:
1. Generate a new value via §B.1.1.
2. Vercel dashboard → edit `GLASS_SIG_SECRET` → paste new value → save.
3. Redeploy.

Effect: every existing `glass_v1` cookie becomes invalid (the HMAC signature no longer verifies). All currently-logged-in users see the challenge page on their next request. Their session is gone, the password they re-enter still works (because `GLASS_PW_HASH` is unchanged unless you also rotated it).

### §B.7 · Common operational gotchas

| Symptom | Cause | Fix |
|---|---|---|
| 503 after merge, before env vars set | Fail-closed working as designed (§3.1 acceptance) | Set env vars per §B.2 |
| 503 after env vars set | Deploy ran before env vars existed | Redeploy without build cache |
| 401 forever, no challenge page | Middleware crash · check function logs | Look for runtime exception in Vercel dashboard → Functions → Logs |
| Security headers missing on `/assets/*` | Matcher excludes `/assets/` from middleware (intentional, §A.2) | `vercel.json > headers` block applies to those paths instead |
| Browser shows challenge but POST fails with 401 | CORS or method-mismatch | Check the form `action="/__auth"` and `method="POST"` are intact |
| Challenge page renders but fonts missing | CSP blocking Google Fonts | Confirm CSP includes `font-src 'self' https://fonts.gstatic.com` and `style-src` includes `https://fonts.googleapis.com` |
| Preview deploy 401s but you're a Vercel team member | Vercel SSO is on for Preview, intercepting before middleware | Log in via Vercel SSO first; then you'll hit the middleware challenge |
| Preview deploy 401s for an external reviewer | Vercel SSO blocking them | Use a `vercel curl --deployment <url>` bypass token, OR temporarily turn off Deployment Protection for the Preview env |
| Wrong-password redirect loops on `/?e=1` | Browser is following the redirect into a fresh GET, which 401s with the challenge — that is correct behaviour | Not a bug. The challenge re-renders with the error message inline. |
