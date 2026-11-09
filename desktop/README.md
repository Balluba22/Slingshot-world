# Asztali (Windows .exe) változat

Attila csomagolása: az appot egy kis Python-program (pywebview) saját ablakban nyitja meg,
böngésző nélkül. Az adatok a `%APPDATA%\SlingshotWorld` mappába mentődnek, és megmaradnak.

Az exe mindig a repó gyökerében lévő `index.html`-ből épül – ugyanabból, amit a GitHub Pages publikál,
így a webes és az asztali változat nem tud szétcsúszni.

## Építés Windowson
1. Python 3.9+ telepítve ("Add to PATH" bepipálva).
2. Töltsd le a repót (Code → Download ZIP) vagy klónozd, és nyisd meg a `desktop` mappát.
3. Tedd ide az `icon.ico` fájlt (a build ezt használja; nincs a repóban, mert bináris).
4. Futtasd a `build_exe.bat`-ot. Eredmény: `dist\SlingshotWorld.exe`.

Fejlesztéshez exe nélkül is futtatható: `python slingshot_app.py` (pywebview telepítve legyen).

Az .exe-t és az ikonokat nem tároljuk a repóban; a kész .exe a GitHub **Releases** oldalra kerül,
a verziószámmal megegyező címkével (pl. `v1.1`).
