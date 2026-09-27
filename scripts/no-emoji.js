const fs = require('fs');
const path = require('path');
const roots = ['README.md', 'contracts', 'frontend/app', 'frontend/lib'];
const emoji = /[\u{1F000}-\u{1FAFF}\u{2600}-\u{27BF}]/u;
function walk(p) {
  if (!fs.existsSync(p)) return [];
  const s = fs.statSync(p);
  if (s.isDirectory()) return fs.readdirSync(p).flatMap((n) => walk(path.join(p, n)));
  return [p];
}
const bad = roots.flatMap(walk).filter((p) => emoji.test(fs.readFileSync(p, 'utf8')));
if (bad.length) { console.error(`Emoji found in: ${bad.join(', ')}`); process.exit(1); }
console.log('No emoji found.');
