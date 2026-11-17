# Változásnapló

Formátum: minden kiadásnál egy szakasz, dátummal. Új bejegyzés mindig legfelülre kerül.

## v1.5 – 2026-11-17
- **🏅 WSA-rangsor kategóriánként**: az összesített táblázat mellett külön táblázat jelenik meg a nőknek, férfiaknak és gyerekeknek, ugyanúgy, mint a normál ranglistán (a játékos adatbázisbeli kategóriája szerint, saját helyezésekkel és érmekkel).
- **Zászló a játékosoknál**: a játékos létrehozásakor (adatbázis-képernyő, „Adatbázisból” ablak, vagy a 💾 mentés a verseny játékossorán) listából választható az ország zászlaja, valamint a kategória. A zászló megjelenik a névnél a WSA-rangsorban, az adatbázis-listában, a kiválasztó ablakban és a verseny játékossorán. Az ország neve az aktuális nyelven jelenik meg; HU, RO, CZ, SK a lista elején. 85 ország, a zászlók a fájlba ágyazott képek (Windows alatt is helyesen látszanak, internet nélkül is).
- **✏️ Szerkesztés** az adatbázisban: név, kategória és zászló módosítható (a törléshez továbbra is egyesületi jelszó kell).
- **Azonosító kézi módosítása**: a ✏️ Szerkesztés ablakban az `id-…` szám átírható. Egy már használt azonosítót nem fogad el. A módosítás frissíti az ezen az eszközön lévő versenyeket; az egyesületi archívum versenyei a régi azonosítót tartják meg (ezeknél a WSA-rangsor a névegyezésre támaszkodik, ha a régi azonosító már nem létezik).
- A `jatekosok.json` export/import mostantól a zászlót is tartalmazza (`flag`, kétbetűs országkód); a régi fájlok zászló nélkül is betölthetők.
- **Zászló a ranglistán**: a játékos zászlaja megjelenik az összesített és a kategória-ranglistán, valamint a JPG-exportban, a részletes ranglistában és az okleveleken is (az adatbázis-játékosnál az azonosító, a régi versenyeknél a név egyezése alapján).
- A fájl mérete a beágyazott zászlók miatt ~110 kB-tal nőtt.

## v1.4 – 2026-11-16
- **👥 Játékos-adatbázis** (állandó, azonosítóval): minden játékos kap egy egyedi azonosítót (`id-1`, `id-2`, …). Új verseny / „Játékos hozzáadása” mellett ott az **👥 Adatbázisból** gomb: beírod, hogy `id-1` (vagy `1`, vagy a név egy részét) és Enter, a játékos bekerül a versenybe. Új játékos az adatbázis-képernyőn, vagy a verseny játékossorán a 💾 gombbal menthető. A játékosok a versenyektől függetlenül megmaradnak.
- **Törlés csak egyesületi jelszóval**: az adatbázisból törölni ugyanazzal a jelszóval lehet, amit az archívumból törléshez is használunk (a jelszót a Worker ellenőrzi). Ha a Worker nem tudja megerősíteni a jelszót, vagy nincs kapcsolat, nem töröl semmit.
- **Adatbázis export/import** (`jatekosok.json`): ha az exportált fájlt a repó gyökerébe tesszük `jatekosok.json` néven, minden eszköz induláskor betölti és egyesíti a helyi adatbázissal (azonosító szerint, ütközésnél a repóbeli név az érvényes). Új játékosokat lehetőleg egy eszközön hozzunk létre, és az exportot töltsük fel.
- **WSA jelölőnégyzet** minden körnél (3. szakasz, a körszorzó mellett); a WSA-körök a körfeliratokban („K1 · WSA”), a táblákban és a részletes ranglistában is megjelennek.
- **🏅 WSA-rangsor** (új képernyő, külön az összesítéstől): csak a WSA-val jelölt körök számítanak; versenyenként a sikerességi arány = találatok ÷ lövések; a játékos rangsor-értéke a versenyenkénti arányok **átlaga** (pl. 80 % és 70 % → (80+70)÷2 = 75 %). Kezdő- és végdátum választható (alapból az idei év), így éves rangsor is készíthető; „Idén / Tavaly / Mind” gyorsgombok. Egy sorra kattintva látszik versenyenkénti bontás. A számításba a készüléken lévő versenyek és az internetről elérhető egyesületi archívum versenyei is beleszámítanak (dátum alapján, duplikáció nélkül).
- A WSA-rangsorba az a játékos kerül, aki szerepel az adatbázisban: az új versenyekben az azonosító (`pid`) köti össze, a régi, azonosító nélküli exportoknál a név egyezése (kis/nagybetű és ékezet nélkül). Az export JSON formátuma kompatibilis maradt (v1); a `pid` és `wsa` mezők opcionálisak.
- Négy nyelven (magyar, angol, román, cseh).

## v1.3c – 2026-11-14
- **Másolat = új verseny**: a 📋 másolat már nem örökli az archív-hivatkozást, így a ☁️ feltöltése új fájlt készít, nem írja felül az eredetit.
- **Felülírás-védelem**: ha a feltöltendő verseny neve eltér attól, ami az archívumban ugyanazon a fájlon szerepel, az app megkérdezi: „Frissítés »régi név«” vagy „Feltöltés újként”. Elavult hivatkozás (az archívumból közben törölt fájl) esetén automatikusan újként megy.

## v1.3 – 2026-11-14
- **☁️ Archívumba gomb** a versenylistában: a verseny exportját egy Cloudflare Workernek küldi, ami a repóba teszi; egyesületi jelszóval védett, az eszköz megjegyzi. Ha a versenynek nincs dátuma, előbb bekéri – a fájlnév mindig a verseny napjából készül. Újraküldés ugyanazt a fájlt frissíti. Beállítás: `cloud/README.md`. Amíg a `CLOUD_URL` üres, a gomb rejtve marad.
- **Eltávolítás az archívumból** (× gomb az archív soron): egyesületi jelszóval és megerősítéssel törli a versenyt a repóból, minden eszközön eltűnik a listából; a már importált példányok megmaradnak.
- **Dátum és helyszín** a versenyhez: az új verseny / átnevezés ablakban megadható, az exportba is bekerül (`date`, `venue`), a letöltött fájl neve a dátummal kezdődik. Importnál és az archívumból is beolvasódik.
- Az `eredmenyek/index.json` jegyzéket mostantól GitHub Action építi a mappa JSON-jaiból (`scripts/build_index.py`) – új eredménynél elég a fájlt feltölteni.
- **📈 Statisztika képernyő** (a kezdőoldalról és a ranglistáról): „Körönként” fül – minden játékos minden körének pontja és találatszáma, a kör legjobbja sárgával, a nők/gyerekek körgyőztese zölddel; „Helyezések alakulása” fül – kattintható bump chart az összesített helyezésről minden kör után, legfeljebb 5 kiemelt vonallal. Négy nyelven.

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
