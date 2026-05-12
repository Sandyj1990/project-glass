const http = require('http');
const fs = require('fs');
const path = require('path');
const ROOT = __dirname;
const PORT = 8765;
const MIME = {'.html':'text/html; charset=utf-8','.css':'text/css','.js':'application/javascript','.json':'application/json','.png':'image/png','.jpg':'image/jpeg','.jpeg':'image/jpeg','.gif':'image/gif','.webp':'image/webp','.svg':'image/svg+xml','.ico':'image/x-icon','.mp4':'video/mp4','.webm':'video/webm','.woff':'font/woff','.woff2':'font/woff2','.ttf':'font/ttf','.pdf':'application/pdf'};
function serve(res, fp) {
  const ext = path.extname(fp).toLowerCase();
  const mime = MIME[ext] || 'application/octet-stream';
  try { const d = fs.readFileSync(fp); res.writeHead(200,{'Content-Type':mime}); res.end(d); }
  catch(e) { res.writeHead(404,{'Content-Type':'text/plain'}); res.end('404'); }
}
http.createServer((req,res) => {
  let url = req.url.split('?')[0];
  let fp = path.join(ROOT, url);
  if (fs.existsSync(fp) && fs.statSync(fp).isFile()) return serve(res,fp);
  if (fs.existsSync(fp) && fs.statSync(fp).isDirectory()) { const i=path.join(fp,'index.html'); if(fs.existsSync(i)) return serve(res,i); }
  const cp = path.join(ROOT, url, 'index.html');
  if (fs.existsSync(cp)) return serve(res,cp);
  const hp = fp+'.html';
  if (fs.existsSync(hp)) return serve(res,hp);
  res.writeHead(404,{'Content-Type':'text/plain'}); res.end('404: '+url);
}).listen(PORT, () => console.log('Server running at http://localhost:'+PORT));
