// iminfin (iМониторинг КРИСТА, региональные бюджеты): сбор дефолтных срезов.
// Запуск ТОЛЬКО с ВМ YC (BI-хосты copen-imon/wf-imon.fm.epbs.ru не отвечают с VPS).
// Требования: node ~/.local/bin/node, playwright из npm-кеша (1.63.0, chromium-1243).
// Выход: /tmp/iminfin/<date>/iminfin_<page>.json — массив POST-ответов /Data?uuid=…
// Анатомия: loader/datasets.yaml -> iminfin-regbudget (коммит dfb0397).
const {chromium} = require('/home/ubuntu/.npm/_npx/e41f203b7505f1fb/node_modules/playwright');
const fs = require('fs');

const DATE = process.argv[2] || new Date().toISOString().slice(0, 10);
const OUT = '/tmp/iminfin/' + DATE;
fs.mkdirSync(OUT, {recursive: true});

const PAGES = {
  raskhody_ispoln: '/areas-of-analysis/budget/raskhody-byudzheta-sub-ekta/ispolnenie-raskhodov-sub-ektov-rf-i-koeffitsient',
  dokhody_dinamika: '/areas-of-analysis/budget/dokhody-po-sub-ektam-rf/pomesyachnaya-dinamika-dokhodov',
  transferty: '/areas-of-analysis/budget/dokhody-po-sub-ektam-rf/mezhbyudzhetnye-transferty-sub-ektam-rf',
  dolg: '/areas-of-analysis/budget/gosudarstvennyj-dolg-sub-ektov-rf',
  kredity: '/areas-of-analysis/budget/kredity',
  natsproekty: '/areas-of-analysis/np/ispolnenie-natsionalnyh-proektov'
};

(async () => {
  const b = await chromium.launch();
  for (const [key, path] of Object.entries(PAGES)) {
    const p = await (await b.newContext()).newPage();
    const datas = [];
    p.on('response', async r => {
      if (r.url().includes('/Data?') && r.request().method() === 'POST') {
        try { const j = await r.json(); datas.push(j); } catch (e) {}
      }
    });
    try {
      await p.goto('https://www.iminfin.ru' + path, {timeout: 60000});
      await p.waitForTimeout(15000);
      fs.writeFileSync(OUT + '/iminfin_' + key + '.json', JSON.stringify(datas));
      console.log(key, '->', datas.length, 'datasets, bytes:', JSON.stringify(datas).length);
    } catch (e) { console.log(key, 'ERR:', e.message); }
    await p.context().close();
  }
  await b.close();
  console.log('DONE', DATE);
})();