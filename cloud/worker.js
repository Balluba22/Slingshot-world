/**
 * SlingshotWorld – archívum-feltöltő Worker (Cloudflare Workers)
 *
 * Az app ide POST-olja a verseny exportját; a Worker ellenőrzi az egyesületi
 * jelszót, majd a GitHub API-n keresztül beteszi a fájlt a repó eredmenyek/
 * mappájába (új fájl vagy ugyanannak a versenynek a frissítése).
 * A GitHub-token csak itt, a Worker titkos beállításai között él.
 *
 * Beállítandó változók (Worker → Settings → Variables and Secrets):
 *   GITHUB_TOKEN   (secret)  fine-grained token, csak erre a repóra, Contents: Read and write
 *   CLUB_PASSWORD  (secret)  az egyesületi jelszó, amit az app kér
 *   GITHUB_REPO    (text)    pl. Balluba22/Slingshot-world
 *   GITHUB_BRANCH  (text)    main
 *   ALLOWED_ORIGIN (text)    pl. https://balluba22.github.io   (vesszővel több is adható; * = bármi)
 */
export default {
  async fetch(request, env) {
    const origin = request.headers.get('Origin') || '';
    const cors = corsHeaders(origin, env.ALLOWED_ORIGIN || '*');
    if (request.method === 'OPTIONS') return new Response(null, { status: 204, headers: cors });
    if (request.method !== 'POST') return json({ error: 'POST only' }, 405, cors);

    let body;
    try { body = await request.json(); } catch { return json({ error: 'bad json' }, 400, cors); }

    if (!env.CLUB_PASSWORD || body.password !== env.CLUB_PASSWORD) {
      return json({ error: 'wrong password' }, 401, cors);
    }
    const exp = body.export;
    if (!exp || exp.app !== 'slinggame' || !exp.cfg || !Array.isArray(exp.cfg.roster) || !exp.cfg.roster.length) {
      return json({ error: 'not a tournament export' }, 400, cors);
    }

    // fájlnév: ÉÉÉÉ-HH-NN_Nev.json – ugyanaz, mint az app letöltési neve
    const date = /^\d{4}-\d{2}-\d{2}$/.test(exp.date || '') ? exp.date : new Date().toISOString().slice(0, 10);
    const safe = String(exp.name || 'verseny').normalize('NFD').replace(/[̀-ͯ]/g, '')
      .replace(/[^\w\-]+/g, '_').replace(/^_+|_+$/g, '').slice(0, 40) || 'verseny';
    const path = `eredmenyek/${date}_${safe}.json`;
    const content = JSON.stringify(exp, null, 1);

    const api = `https://api.github.com/repos/${env.GITHUB_REPO}/contents/${path}`;
    const gh = {
      'Authorization': `Bearer ${env.GITHUB_TOKEN}`,
      'Accept': 'application/vnd.github+json',
      'User-Agent': 'slingshotworld-archive-worker',
      'X-GitHub-Api-Version': '2022-11-28',
    };

    // létezik már? (akkor frissítjük – ehhez kell a sha)
    let sha = null;
    const head = await fetch(`${api}?ref=${env.GITHUB_BRANCH || 'main'}`, { headers: gh });
    if (head.status === 200) sha = (await head.json()).sha;
    else if (head.status !== 404) return json({ error: 'github read failed', status: head.status }, 502, cors);

    const shots = Object.values(exp.cfg.res || {}).reduce((n, v) => n + (Array.isArray(v) ? v.join('').length : 0), 0);
    const put = await fetch(api, {
      method: 'PUT', headers: { ...gh, 'Content-Type': 'application/json' },
      body: JSON.stringify({
        message: `${sha ? 'eredmenyek: frissítve' : 'eredmenyek: új verseny'} – ${exp.name} (${exp.cfg.roster.length} játékos, ${shots} lövés)`,
        content: btoa(unescape(encodeURIComponent(content))),
        branch: env.GITHUB_BRANCH || 'main',
        ...(sha ? { sha } : {}),
      }),
    });
    if (!put.ok) {
      const t = await put.text();
      return json({ error: 'github write failed', status: put.status, detail: t.slice(0, 300) }, 502, cors);
    }
    return json({ ok: true, file: path.replace('eredmenyek/', ''), updated: !!sha }, 200, cors);
  },
};

function corsHeaders(origin, allowed) {
  const list = allowed.split(',').map(s => s.trim());
  const ok = list.includes('*') || list.includes(origin);
  return {
    'Access-Control-Allow-Origin': ok ? (origin || '*') : 'null',
    'Access-Control-Allow-Methods': 'POST, OPTIONS',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '86400',
  };
}
function json(obj, status, cors) {
  return new Response(JSON.stringify(obj), { status, headers: { 'Content-Type': 'application/json', ...cors } });
}
