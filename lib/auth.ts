const TOKEN_BYTES = 16;

export function parseCookie(header: string, name: string): string | null {
  for (const part of header.split(/;\s*/)) {
    const eq = part.indexOf('=');
    if (eq < 0) continue;
    if (part.slice(0, eq) === name) return part.slice(eq + 1);
  }
  return null;
}

export async function sha256Hex(input: string): Promise<string> {
  const buf = await crypto.subtle.digest('SHA-256', new TextEncoder().encode(input));
  return bytesToHex(new Uint8Array(buf));
}

export async function mintCookie(secretHex: string): Promise<string> {
  const random = crypto.getRandomValues(new Uint8Array(TOKEN_BYTES));
  const token = bytesToHex(random);
  const sig = await hmacHex(secretHex, token);
  return `${token}.${sig}`;
}

export async function verifyCookie(value: string, secretHex: string): Promise<boolean> {
  const dot = value.indexOf('.');
  if (dot < 0) return false;
  const token = value.slice(0, dot);
  const provided = value.slice(dot + 1);
  if (token.length !== TOKEN_BYTES * 2) return false;
  if (!/^[0-9a-f]+$/.test(token)) return false;
  const expected = await hmacHex(secretHex, token);
  return constantTimeEqual(provided, expected);
}

async function hmacHex(secretHex: string, data: string): Promise<string> {
  const key = await crypto.subtle.importKey(
    'raw',
    hexToBytes(secretHex),
    { name: 'HMAC', hash: 'SHA-256' },
    false,
    ['sign'],
  );
  const sig = await crypto.subtle.sign('HMAC', key, new TextEncoder().encode(data));
  return bytesToHex(new Uint8Array(sig));
}

function bytesToHex(bytes: Uint8Array): string {
  let out = '';
  for (let i = 0; i < bytes.length; i++) out += bytes[i].toString(16).padStart(2, '0');
  return out;
}

function hexToBytes(hex: string): Uint8Array {
  const out = new Uint8Array(hex.length / 2);
  for (let i = 0; i < out.length; i++) out[i] = parseInt(hex.substr(i * 2, 2), 16);
  return out;
}

function constantTimeEqual(a: string, b: string): boolean {
  if (a.length !== b.length) return false;
  let r = 0;
  for (let i = 0; i < a.length; i++) r |= a.charCodeAt(i) ^ b.charCodeAt(i);
  return r === 0;
}
