# Felhő-mentés (☁️ Archívumba gomb)

Az app a verseny exportját egy Cloudflare Workernek küldi, ami az egyesületi jelszó
ellenőrzése után beteszi a fájlt a repó `eredmenyek/` mappájába. Ezután a jegyzék-Action
frissíti az `index.json`-t, és a verseny megjelenik mindenkinél az Egyesületi archívumban.

Miért kell a Worker: az app egy publikus weboldal, GitHub-tokent nem tartalmazhat.
A token csak a Worker titkos beállításaiban él.

## Egyszeri beállítás (kb. 15 perc)

1. **GitHub-token** – azzal a fiókkal, amelyik írhat a repóba:
   github.com → jobb felül profil → Settings → Developer settings → Personal access tokens →
   Fine-grained tokens → Generate new token.
   Name: `slingshotworld-archive`; Expiration: 1 év; Repository access: Only select repositories →
   a repó; Permissions → Repository permissions → **Contents: Read and write**. Generate, a tokent másold ki
   (csak egyszer látszik).
2. **Cloudflare-fiók** – dash.cloudflare.com, ingyenes regisztráció e-mail-címmel.
3. **Worker létrehozása** – bal menü Compute (Workers) → Create → Start with Hello World → név:
   `slingshotworld-archive` → Deploy. Utána Edit code → a `worker.js` teljes tartalmát bemásolni a
   szerkesztőbe a meglévő helyére → Deploy.
4. **Változók** – a Worker oldalán Settings → Variables and Secrets → Add:
   - `GITHUB_TOKEN` – Secret – az 1. lépés tokenje
   - `CLUB_PASSWORD` – Secret – az egyesületi jelszó (ezt kéri az app)
   - `GITHUB_REPO` – Text – `Balluba22/Slingshot-world`
   - `GITHUB_BRANCH` – Text – `main`
   - `ALLOWED_ORIGIN` – Text – `https://balluba22.github.io` (a Pages címe; több is adható vesszővel)
   Deploy.
5. **A Worker címe** – a Worker oldalán látszik, `https://slingshotworld-archive.csongeto-csaba.workers.dev`.
   Ezt kell beírni az `index.html` elején a `CLOUD_URL` változóba (`var CLOUD_URL='https://…/';`),
   és feltölteni az `index.html`-t. Amíg `CLOUD_URL` üres, a ☁️ gomb nem jelenik meg.

## Működés
- A verseny dátuma kötelező: ha nincs, az app a küldés előtt bekéri. A fájlnév ebből készül, nem a feltöltés napjából.
- Az archív soron lévő × gomb jelszóval és megerősítéssel törli a fájlt a repóból (`action: delete`).
- A fájl neve `ÉÉÉÉ-HH-NN_Verseny_neve.json` (dátum az exportból). Ugyanannak a versenynek az
  újraküldése felülírja a fájlt (frissítés), nem duplikál.
- A jelszót az app az eszközön megjegyzi; hibás jelszónál újra kérdez.
- Jelszócsere: a Workerben a `CLUB_PASSWORD` módosítása; az app a következő küldésnél újra kérdezi.
- Ingyenes keret: napi 100 000 kérés – ennek töredéke sem kell.
