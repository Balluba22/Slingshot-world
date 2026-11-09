# SlingshotWorld

Csúzliverseny-vezető webalkalmazás a Magyar Csúzli Sportegyesület számára.
Egyetlen HTML-fájl, telepítés és háttérrendszer nélkül, telefonon és laptopon is fut.

**Élő alkalmazás:** https://balluba22.github.io/Slingshot-world/ (GitHub Pages: Settings → Pages → Branch: main, / root)

## Funkciók
- Játékosok és kategóriák (nők / férfiak / gyerekek), egyszerre 1–3 játékos lő
- Körönként szabadon összeállítható célpontsor: 3–8 cm méretek + 6 speciális célpont (S1–S6)
- Pontértékek kategóriánként külön is állíthatók, pontszorzók körönként (×1/×2/×3)
- Ranglista összesítve és kategóriánként, holtverseny esetén szétlövés
- Részletes ranglista minden lövéssel és találati aránnyal, PDF- és JPG-exporttal
- Oklevelek (top 3 kategóriánként), nyomtatás, JPG-export
- Több verseny kezelése, JSON export/import eszközök között
- Egyesületi archívum: a repóban közzétett eredmények egy koppintással importálhatók bármely eszközön
- Nyelvek: magyar, angol, román, cseh
- Asztali (Windows .exe) változat: lásd `desktop/`

## Fontos tudnivaló
Az app minden adatot a böngésző saját tárhelyén (localStorage) tart, **eszközönként külön**.
Verseny után mindig készíts JSON-exportot (🗂 Versenyek → Exportálás → Fájl letöltése),
és töltsd fel az `eredmenyek/` mappába.

## Mappák
- `index.html` – maga az alkalmazás (ezt publikálja a GitHub Pages); a `SlingshotWorld.html` ugyanez a fájl az eredeti nevén
- `eredmenyek/` – a versenyek JSON-exportjai és kiértékelései
- `desktop/` – a Windows .exe építéséhez szükséges fájlok

## Fejlesztés
- A `main` ág = a versenyen használható stabil verzió. Erre a GitHub Pages automatikusan publikál.
- Minden változtatás külön ágon (branch) készül, és Pull Requesttel kerül a `main`-re.
- Ötletek, hibák: az **Issues** fülön.
- Változások összefoglalója: `CHANGELOG.md`.
- Az export JSON formátuma (`v: 1`) maradjon visszafelé kompatibilis, hogy a régi versenyek importálhatók maradjanak.

## Csapat
Attila (Balluba22) · Erika · Csaba (csabacsongeto)
