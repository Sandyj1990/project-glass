export function challengeHtml(showError: boolean): string {
  const errorMsg = showError ? 'Incorrect access phrase.' : '';
  return `<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>Project Glass · Authorised access only</title>
<link rel="icon" href="/favicon.ico" />
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet" />
<style>
* { box-sizing: border-box; margin: 0; padding: 0; }
html, body { height: 100%; }
body {
  font-family: Inter, system-ui, sans-serif;
  color: #1a1a1c;
  background: #fff;
  -webkit-font-smoothing: antialiased;
}
.gate {
  position: fixed;
  inset: 0;
  display: flex;
  flex-direction: column;
  background: #fff;
  padding: 32px 32px 28px;
  overflow: hidden;
}
.brand {
  display: flex;
  align-items: center;
  gap: 18px;
}
.brand img { width: 36px; height: 36px; display: block; }
.brand .sep { width: 1px; height: 24px; background: #d4d4d2; }
.brand .proj {
  font-family: 'JetBrains Mono', monospace;
  font-size: 12px;
  letter-spacing: 0.22em;
  color: #1a1a1c;
  text-transform: uppercase;
  font-weight: 500;
}
.form {
  width: 100%;
  max-width: 380px;
  margin: auto;
}
.form input {
  width: 100%;
  padding: 16px;
  border: 1px solid #e5e5e3;
  border-radius: 10px;
  background: #fff;
  font: inherit;
  font-size: 15px;
  color: #1a1a1c;
  outline: none;
  transition: border-color .15s, box-shadow .15s;
  box-shadow: 0 1px 2px rgba(0,0,0,0.02);
}
.form input::placeholder { color: #9a9a9d; }
.form input:focus { border-color: #1a1a1c; box-shadow: 0 1px 3px rgba(0,0,0,0.04); }
.form button {
  margin-top: 12px;
  width: 100%;
  padding: 16px;
  border: 0;
  border-radius: 10px;
  background: #8a8a8d;
  color: #fff;
  font: inherit;
  font-weight: 500;
  font-size: 15px;
  cursor: pointer;
  transition: background .15s;
}
.form button:hover { background: #1a1a1c; }
.err {
  color: #c4322f;
  font-size: 13px;
  margin-top: 12px;
  min-height: 18px;
  text-align: center;
}
.conf {
  width: 100%;
  max-width: 760px;
  margin: 0 auto;
  padding: 0 16px;
  text-align: center;
}
.conf-head {
  font-family: 'JetBrains Mono', monospace;
  font-size: 11px;
  font-weight: 600;
  letter-spacing: 0.18em;
  color: #1a1a1c;
  text-transform: uppercase;
  margin-bottom: 18px;
}
.conf-head .dot {
  display: inline-block;
  width: 5px;
  height: 5px;
  border-radius: 50%;
  background: #1a1a1c;
  vertical-align: middle;
  margin-right: 10px;
  transform: translateY(-1px);
}
.conf-body {
  font-size: 13px;
  line-height: 1.7;
  color: #5a5a5e;
  margin: 0 0 18px;
}
.conf-copy {
  font-family: 'JetBrains Mono', monospace;
  font-size: 10px;
  letter-spacing: 0.22em;
  color: #9a9a9d;
  text-transform: uppercase;
}
</style>
</head>
<body>
<div class="gate">
<header class="brand">
<img src="/assets/fynd-logo.png" alt="Fynd" />
<div class="sep"></div>
<div class="proj">Project Glass</div>
</header>
<form class="form" method="POST" action="/__auth" autocomplete="off">
<input type="password" name="password" placeholder="Enter password" autofocus aria-label="Access phrase" />
<button type="submit">Continue</button>
<div class="err">${errorMsg}</div>
</form>
<div class="conf">
<div class="conf-head"><span class="dot"></span>Confidential · Authorised use only</div>
<p class="conf-body">Project Glass is a private workspace operated by Shopsense Retail Technologies Limited (Fynd) and its partners, for a defined group of authorised individuals. The materials hosted here are proprietary, commercially sensitive and protected by copyright and confidentiality obligations. Access, viewing, copying, screenshotting or onward sharing by anyone outside the authorised group is strictly prohibited and may give rise to civil and criminal liability. If you have arrived here by mistake, please close this page.</p>
<div class="conf-copy">© 2026 Shopsense Retail Technologies Limited · All rights reserved</div>
</div>
</div>
</body>
</html>`;
}
