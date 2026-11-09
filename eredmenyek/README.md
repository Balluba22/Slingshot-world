# Eredmények

Ide kerül minden verseny JSON-exportja az appból
(🗂 Versenyek → az adott verseny sorában **Exportálás** → **Fájl letöltése**),
és mellé a verseny kiértékelése.

Fájlnév: `ÉÉÉÉ-HH_Verseny_neve.json`, pl. `2026-11_Tomzoon_kupa.json`.
Ha egy versenyt több eszközön vezettek, minden eszközről külön fájl: `..._eszkoz1.json`, `..._eszkoz2.json`.

Az export tartalma: játékosok, kategóriák, célpontsorok, pontértékek, szorzók és minden egyes lövés
(találat/mellé), így a verseny bármikor újraelemezhető vagy visszaimportálható.

## Egyesületi archívum az appban
Az app a 🗂 Versenyek képernyőn megjeleníti az itt közzétett eredményeket („Egyesületi archívum”),
és egy koppintással importálja őket az adott eszközre. A listát az `index.json` fájl adja – **új eredmény
feltöltésekor ide is fel kell venni egy sort**:

```json
{ "file": "2026-11_Tomzoon_kupa.json", "name": "Tomzoon kupa", "date": "2026-11-07", "players": 31 }
```

Mezők: `file` (a JSON neve ebben a mappában), `name` (megjelenő név), `date` (ÉÉÉÉ-HH-NN), `players` (opcionális), `note` (opcionális rövid megjegyzés).

## Tomzoon kupa · 2026. november
- `2026-11_Tomzoon_kupa.json` – a verseny teljes exportja (31 játékos, 1275 lövés)
- `2026-11_Tomzoon_kupa_elemzes.html` – teljes kiértékelés: dobogók, top 10, a nap íve, a három versenyszám, szorzók hatása, tanulságok
- `2026-11_Tomzoon_kupa_koronkent.html` – minden játékos minden köre, körgyőztesek kiemelve
- `2026-11_Tomzoon_kupa_helyezesek.html` – a helyezések alakulása körről körre (bump chart)
- `2026-11_Tomzoon_kupa_szorzo.html` – hivatalos végeredmény és szorzó nélküli rangsor egymás mellett

A HTML-ek önállóak, böngészőben nyílnak, telefonon is olvashatók.
