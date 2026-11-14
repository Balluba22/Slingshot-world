# Eredmények

Ide kerül minden verseny JSON-exportja az appból
(🗂 Versenyek → az adott verseny sorában **Exportálás** → **Fájl letöltése**),
és mellé a verseny kiértékelése.

Fájlnév: az app által letöltött név, `ÉÉÉÉ-HH-NN_Verseny_neve.json`, pl. `2026-11-07_Tomzoon_kupa.json`.
Ha egy versenyt több eszközön vezettek, minden eszközről külön fájl: `..._eszkoz1.json`, `..._eszkoz2.json`.

Az export tartalma: játékosok, kategóriák, célpontsorok, pontértékek, szorzók és minden egyes lövés
(találat/mellé), így a verseny bármikor újraelemezhető vagy visszaimportálható.

## Egyesületi archívum az appban
Az app a 🗂 Versenyek képernyőn megjeleníti az itt közzétett eredményeket („Egyesületi archívum”),
és egy koppintással importálja őket az adott eszközre.

A listát az `index.json` adja, **ezt nem kell kézzel szerkeszteni**: amikor új JSON kerül a mappába
(a `main` ágon), egy GitHub Action (`.github/workflows/eredmenyek-index.yml`) lefuttatja a
`scripts/build_index.py` szkriptet, ami a fájlokból újraépíti a jegyzéket és commitolja.
A név, a dátum és a helyszín az exportból jön (az app v1.3-tól írja bele); régi exportnál a dátum a
fájlnév elejéről. Ha kell, a workflow kézzel is indítható az Actions fülön („Run workflow”).
