#!/usr/bin/env python3
"""Az eredmenyek/index.json jegyzék előállítása a mappában lévő verseny-exportokból.

Minden *.json (az index.json kivételével) egy sor lesz:
  file    – a fájl neve
  name    – az exportban tárolt versenynév (ha nincs, a fájlnévből)
  date    – az export "date" mezője; ha üres, a fájlnév eleje (ÉÉÉÉ-HH vagy ÉÉÉÉ-HH-NN)
  venue   – az export "venue" mezője (ha van)
  players – a roster hossza
  shots   – az összes rögzített lövés
Nem ír, ha a tartalom nem változott (így nincs felesleges commit).
"""
import json, os, re, sys

DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'eredmenyek')
OUT = os.path.join(DIR, 'index.json')

items = []
for fn in sorted(os.listdir(DIR)):
    if not fn.endswith('.json') or fn == 'index.json':
        continue
    path = os.path.join(DIR, fn)
    try:
        with open(path, encoding='utf-8') as f:
            o = json.load(f)
    except Exception as e:
        print(f'kihagyva (nem olvasható JSON): {fn} – {e}', file=sys.stderr)
        continue
    cfg = o.get('cfg', o) if isinstance(o, dict) else None
    if not isinstance(cfg, dict) or not isinstance(cfg.get('roster'), list) or not cfg['roster']:
        print(f'kihagyva (nem verseny-export): {fn}', file=sys.stderr)
        continue
    m = re.match(r'(\d{4}-\d{2}(?:-\d{2})?)', fn)
    date = str(o.get('date') or '')[:10] or (m.group(1) if m else '')
    name = o.get('name') or re.sub(r'^\d{4}-\d{2}(-\d{2})?_', '', fn[:-5]).replace('_', ' ')
    shots = sum(len(s or '') for v in (cfg.get('res') or {}).values() if isinstance(v, list) for s in v)
    item = {'file': fn, 'name': str(name)[:40], 'date': date, 'players': len(cfg['roster']), 'shots': shots}
    if o.get('venue'):
        item['venue'] = str(o['venue'])[:60]
    items.append(item)

items.sort(key=lambda x: (x['date'], x['file']), reverse=True)
new = json.dumps(items, ensure_ascii=False, indent=2) + '\n'
old = open(OUT, encoding='utf-8').read() if os.path.exists(OUT) else None
if new != old:
    with open(OUT, 'w', encoding='utf-8') as f:
        f.write(new)
    print(f'index.json frissítve: {len(items)} verseny')
else:
    print(f'index.json változatlan: {len(items)} verseny')
