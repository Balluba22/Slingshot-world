# Változásnapló

Formátum: minden kiadásnál egy szakasz, dátummal. Új bejegyzés mindig legfelülre kerül.

## v1.2 – 2026-11-09
- **Egyesületi archívum** a Versenyek képernyőn: az app betölti a repó `eredmenyek/index.json` jegyzékét, és a közzétett versenyeket egy koppintással importálja. Már importált versenynél „Megnyitás” gomb, nincs duplikálás. Internet nélkül a szakasz nem jelenik meg, minden más változatlan. Négy nyelven.

## Repó – 2026-11-09
- README, változásnapló, `.gitignore`; `eredmenyek/` a Tomzoon kupa exportjával és négy kiértékelő oldallal; `desktop/` a Windows-build forrásaival (az exe a gyökér `index.html`-ből épül).

## v1.1 – 2026-11-08 (Attila)
- **Speciális célpontok**: 6 új célpont (S1–S6) a 3–8 cm-es méretek mellett, saját színnel és ponttal.
- **Pontok kategóriánként**: a célpontok pontértéke külön állítható nőknek, férfiaknak, gyerekeknek („Mind” fül = közös).
- **Részletes ranglista** (📋): minden játékos minden lövése körönként, találati arány, szétlövések;
  export több oldalas PDF-be, vagy JPG-oldalak ZIP-ben, egy-egy oldal JPG-be.
- Háttérkép az alkalmazásban (a fájlba ágyazva – emiatt a HTML ~540 kB).
- **Asztali változat**: Windows .exe pywebview + PyInstaller alapon (`desktop/` mappa), az adatok a `%APPDATA%\SlingshotWorld` mappába mentődnek.
- Az export JSON formátuma kompatibilis maradt (v1); a régi exportok importálhatók.

## v1.0 – 2026-11 (Tomzoon kupa)
- Első verzió a GitHubon: a Tomzoon kupán használt állapot.
- Funkciók: játékosok és kategóriák, körönkénti célpontsor és pontszorzók, ranglista, szétlövés,
  oklevelek, nyomtatás és JPG-export, több verseny kezelése JSON export/importtal,
  magyar/angol/román/cseh nyelv.
