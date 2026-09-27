const fs = require('fs');
const path = require('path');
const roots = ['README.md', 'contracts', 'frontend/app', 'frontend/lib'];
function walk(p) {
  if (!fs.existsSync(p)) return [];
  const s = fs.statSync(p);
  if (s.isDirectory()) return fs.readdirSync(p).flatMap((n) => walk(path.join(p, n)));
  return [p];
}
const bad = roots.flatMap(walk).filter((p) => fs.readFileSync(p, 'utf8').includes('\u2014'));
if (bad.length) { console.error(`Em dash found in: ${bad.join(', ')}`); process.exit(1); }
console.log('No em dash found.');
