// Local preview of a Slides-type deck folder: renders each project/slides/<id>.html
// at 1920x1080 with the deck's Google Fonts, approximating the runtime's defaults.
// Usage: node render.cjs <deckRoot> <outDir> [id ...]
const fs = require('fs');
const path = require('path');
const { chromium } = require('/opt/node22/lib/node_modules/playwright');

const [, , deckRoot, outDir, ...only] = process.argv;
const deck = JSON.parse(fs.readFileSync(path.join(deckRoot, 'project/deck.json'), 'utf8'));
const links = Object.values(deck.faces || {})
  .filter((f) => f.href)
  .map((f) => `<link rel="stylesheet" href="${f.href}">`)
  .join('\n');

const BASE = `
html,body{margin:0;padding:0;background:#777}
section{width:1920px;height:1080px;position:relative;box-sizing:border-box;overflow:hidden;display:flex;flex-direction:column;font-size:32px;line-height:1.4}
section *{box-sizing:border-box;margin:0}
section div{display:flex;flex-direction:column;min-width:0}
h1{font-size:96px;font-weight:600;line-height:1.1}
h2{font-size:64px;font-weight:600;line-height:1.15}
h3{font-size:44px;font-weight:600;line-height:1.2}
p,li{font-size:inherit}
p{line-height:inherit}
ul,ol{padding-left:1.1em}
table{border-collapse:collapse}
td,th{border:1px solid rgba(20,32,43,.18);padding:.35em .6em;text-align:left;vertical-align:top}
aside{display:none}
`;

(async () => {
  fs.mkdirSync(outDir, { recursive: true });
  const proxy = process.env.HTTPS_PROXY ? { server: process.env.HTTPS_PROXY } : undefined;
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium', proxy });
  const page = await browser.newPage({ viewport: { width: 1920, height: 1080 }, deviceScaleFactor: 1 });
  // Chromium does not trust the egress proxy's CA, so fetch Google Fonts with curl (which does) and serve from a local cache.
  const { execFileSync } = require('child_process');
  const crypto = require('crypto');
  const cacheDir = path.join(__dirname, 'fontcache');
  fs.mkdirSync(cacheDir, { recursive: true });
  const UA = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0 Safari/537.36';
  await page.route(/fonts\.(googleapis|gstatic)\.com/, async (route) => {
    const url = route.request().url();
    const isCss = url.includes('googleapis.com/css');
    const file = path.join(cacheDir, crypto.createHash('sha1').update(url).digest('hex') + (isCss ? '.css' : '.woff2'));
    try {
      if (!fs.existsSync(file)) execFileSync('curl', ['-sS', '--max-time', '30', '-A', UA, '-o', file, url]);
      await route.fulfill({ path: file, contentType: isCss ? 'text/css' : 'font/woff2', headers: { 'access-control-allow-origin': '*' } });
    } catch (e) { await route.abort(); }
  });
  const ids = only.length ? only : deck.order;
  const report = [];
  for (const id of ids) {
    const file = path.join(deckRoot, 'project/slides', `${id}.html`);
    if (!fs.existsSync(file)) { report.push(`${id}: MISSING`); continue; }
    const html = fs.readFileSync(file, 'utf8');
    await page.setContent(`<!doctype html><html><head><meta charset="utf-8">${links}<style>${BASE}</style></head><body>${html}</body></html>`, { waitUntil: 'networkidle' });
    await page.evaluate(() => document.fonts.ready);
    // Overflow check: any text element whose content overflows its box, or anything past the canvas.
    const issues = await page.evaluate(() => {
      const out = [];
      const sec = document.querySelector('section');
      const sr = sec.getBoundingClientRect();
      const els = sec.querySelectorAll('h1,h2,h3,p,li,td,th,div');
      els.forEach((el) => {
        const r = el.getBoundingClientRect();
        const txt = (el.textContent || '').trim().slice(0, 40);
        if (['P', 'H1', 'H2', 'H3', 'LI', 'TD', 'TH'].includes(el.tagName)) {
          if (el.scrollWidth > el.clientWidth + 2) out.push(`h-overflow <${el.tagName.toLowerCase()}> "${txt}" (${el.scrollWidth}>${el.clientWidth})`);
          if (el.scrollHeight > el.clientHeight + 2 && el.style.height) out.push(`v-overflow <${el.tagName.toLowerCase()}> "${txt}"`);
          const fs = parseFloat(getComputedStyle(el).fontSize);
          if (fs < 24) out.push(`small-font ${fs}px <${el.tagName.toLowerCase()}> "${txt}"`);
        }
        if (r.width && (r.right > sr.right + 1 || r.bottom > sr.bottom + 1)) out.push(`off-canvas <${el.tagName.toLowerCase()}> "${txt}" bottom=${Math.round(r.bottom)} right=${Math.round(r.right)}`);
        if (el.tagName !== 'DIV' && r.width && r.bottom > 952 && getComputedStyle(el).position !== 'absolute') out.push(`below-952 flow <${el.tagName.toLowerCase()}> "${txt}" bottom=${Math.round(r.bottom)}`);
        // Pinned footers are meant to be one line; a wrapped one creeps up toward the content.
        if (el.tagName === 'P' && el.style.bottom && getComputedStyle(el).position === 'absolute' && r.height > 1.6 * parseFloat(getComputedStyle(el).fontSize) * 1.4) out.push(`footer-wrap "${txt}" h=${Math.round(r.height)}`);
      });
      // Detect flow content extending past section content box (squeeze would kick in)
      const kids = [...sec.children].filter((c) => getComputedStyle(c).position !== 'absolute' && c.tagName !== 'ASIDE');
      const pb = parseFloat(getComputedStyle(sec).paddingBottom);
      const maxBottom = Math.max(0, ...kids.map((c) => c.getBoundingClientRect().bottom));
      if (maxBottom > sr.bottom - pb + 1) out.push(`flow-overfull: content bottom ${Math.round(maxBottom)} > ${Math.round(sr.bottom - pb)}`);
      out.push(`elements=${sec.querySelectorAll('*').length} flowBottom=${Math.round(maxBottom)}`);
      return out;
    });
    await page.locator('section').first().screenshot({ path: path.join(outDir, `${id}.png`) });
    report.push(`${id}: ${issues.join(' | ')}`);
  }
  // Contact sheet
  const thumbs = ids.filter((id) => fs.existsSync(path.join(outDir, `${id}.png`)))
    .map((id) => `<figure style="margin:0"><img src="data:image/png;base64,${fs.readFileSync(path.resolve(outDir, id + '.png')).toString('base64')}"><figcaption>${id}</figcaption></figure>`).join('');
  await page.setViewportSize({ width: 1940, height: 1200 });
  await page.setContent(`<html><body style="margin:0;background:#444;display:grid;grid-template-columns:repeat(2,960px);gap:10px;padding:5px;font:20px sans-serif;color:#eee">${thumbs.replace(/<img /g, '<img style="width:960px;height:540px;display:block" ')}</body></html>`, { waitUntil: 'load' });
  await page.screenshot({ path: path.join(outDir, '_contact.png'), fullPage: true });
  await browser.close();
  console.log(report.join('\n'));
})();
