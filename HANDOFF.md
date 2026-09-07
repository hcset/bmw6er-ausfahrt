# HANDOFF – bmw6er-ausfahrt

**Datum:** 2026-09-07, 16:21
**Repo:** `/Users/ct/bmw6er-ausfahrt` (Branch `main`, HEAD `82377d4`)
**Stand:** läuft – live deployed, Orga-Punkte offen

---

## 1. Was dieses Projekt ist

Roadbook/Handout für die BMW 6er Club Ausfahrt am Sa 03.10.2026 (Rundkurs Bad
Kissingen – Meiningen – Rhön – Bad Kissingen, ~180 km, 3 Etappen). Eine
HTML-Quelle erzeugt A5-Print-PDF und mobile Webseite; dazu interaktive Karte,
GPX und Zusatzinhalte. Auftraggeber: Freund des Users (Markus Renner,
Tourleitung). Live: https://hcset.github.io/bmw6er-ausfahrt/

## 2. Changelog (diese Session, 07.09.2026)

### Route + Roadbook v1.0 (Commit `cfedbbf`, Historie neu aufgesetzt)
- Route per Nominatim-Geocoding + OSRM mit Via-Punkten gebaut (B279 statt
  A71 erzwungen), `continue_straight=false` + Retrace-Pruning gegen
  Dorfkern-Stiche; Etappen 68,6 / 86,3 / 25,5 km
- Handout mit Ablaufplan, Roadbook-Tabellen (SVG-Piktogramme), Stopps,
  Vorlesetexten, Konvoi-Regeln, Teilnehmerliste, Quiz/Bingo; DINish-Font
- Wikimedia-Fotos mit Lizenznachweisen (assets/img/lizenzen.md)
- Git-Historie wurde VOR dem Publish neu aufgesetzt (alte Commits enthielten
  Personenfoto); Backup der alten Historie im Session-Scratchpad (flüchtig)

### 70er-Redesign + v1.2 (Commit `0ae1844`)
- Farbwelt E24-Ära: Cremeweiß/Inka-Orange/Braun/Beige, Speedline,
  Rallye-Startnummern-Plaketten statt Farbbalken; Karten neu gerendert
  (Linien Rotton/Braun/Beige mit weißer Kontur)
- Zeitplan auf Start 09:00 umgerechnet (Nutzer-Korrektur): Führung 11:30 =
  PLANWERT (Markus hat eigene Zeit gebucht, Uhrzeit unbekannt), Rückkehr
  18:30, Sonnenuntergang 18:55
- 2 feste Blitzer aus OSM als Warnzeilen (Ortseinfahrt Meiningen; B279 bei
  Gersfeld, je Tempo 50)
- Zweite PDF-Variante roadbook-a5-sw.pdf (?sw=1, tintensparend); Menü-Link
  in Nav + Karte; Grußwort mit Porträt Markus Renner (Foto-Freigabe liegt
  vor); QR-Code auf Rückseite → Pages-URL
- GitHub Pages aktiviert (Repo public, andere Repos unberührt privat)

### E24-Artikel (Commit `82377d4`)
- Vom User gelieferter Artikel „Der lange Atem des Haifischs" als
  e24-historie.html im Projektdesign, Menüpunkt auf index.html; unsichere
  Werte als [unsicher] markiert
- Verteilt nach NotebookLM (Notebook „BMW 6er Ausfahrt 03.10.2026", ID
  8c2cb8db-98cc-40d9-92c1-8efb0b2032b0, 5 Quellen) und Obsidian-Vault
  `~/Library/Mobile Documents/iCloud~md~obsidian/Documents/BMW6er-Ausfahrt/`
  (4 Notizen inkl. Hub mit Orga-Checkliste)

### Nebenschauplätze dieser Session (nicht dieses Repo)
- Skill `/handoff` global installiert (`~/.claude/skills/handoff/`), plus
  App-Variante als Zip in `~/Downloads/handoff-app-skill.zip`
- alanbuildz.com-Guides inhaltlich geprüft, Prioritäten-PDF an User geliefert

## 3. Repo-Map

- `handout.html` – die eine Quelle: Web + Print-CSS (A5) + ?sw=1-Variante
- `index.html` – Menü/Startseite (7 Karten)
- `e24-historie.html` – Modellhistorie-Artikel
- `karten/karte.html` – Leaflet; Params: ?etappe=1|2|3, ?static=1 (für
  Screenshots: ohne Zoom-Buttons/Menü-Knopf)
- `daten/build_route.py` – Geocoding+OSRM+Pruning; schreibt route.json + GPX
- `daten/stopps.md` – Recherche Stopps/Zeiten; `daten/blitzer.json` – OSM-Blitzer
- `roadbook-a5.pdf` / `roadbook-a5-sw.pdf` – generiert, im Repo committed
- `assets/img/lizenzen.md` – Pflicht-Attributionen aller Bilder

## 4. Key Facts (nicht nochmal recherchieren)

- PDF-Erzeugung NUR über lokalen Server (`python3 -m http.server 8791`),
  file:// bricht Leaflet/Fetch; Chrome headless mit
  `--virtual-time-budget=25000 --no-pdf-header-footer`
- Frische --user-data-dir-Profile hängen Chrome headless gelegentlich →
  Default-Profil nutzen oder Prozess killen
- Dampflokwerk-Führungen offiziell NUR samstags 10:00 (Apr–Okt); Gruppen ab
  6 Personen anmeldepflichtig, 03693 851602, 6 €/Person BAR
- Kontakte: Brückenmühle 03693 801004 (feste Gerichte für Gruppe vereinbart,
  kein Speisekarten-Link gewünscht) · Berghaus Rhön 09749 9307721 (Sa 10–22,
  Reservierung nur telefonisch) · Hotel Bayerischer Hof 0971 80450
- Etappenfarben-Tokens heißen historisch --blau/--rot/--gruen, enthalten
  aber die 70er-Werte (#b4441c/#6f4520/#7c5f2b); Kartenlinien separat in
  karte.html (#b4441c/#6f4520/#c8a25e)
- SYNC-PFLICHT: Inhalte liegen an 4 Orten (Web/Repo, NotebookLM, Obsidian,
  gedruckte PDFs) – bei Änderungen alle nachziehen; auch in
  project_bmw6er_ausfahrt.md vermerkt
- Design gepinnt: 70er/E24-Ära; impeccable + emil-design-eng bei
  Designarbeit laden (Nutzerregel)

## 5. Offene Aufgaben (in Reihenfolge)

1. (User→Markus) Gebuchte Führungszeit Dampflokwerk bestätigen – bei
   Abweichung von 11:30: Claude rechnet Zeitplan um (Cover-Fakten, Zeitplan,
   Roadbook-Zeile 31, Etappen-Köpfe)
2. (User→Markus) Grußwort-Wording absegnen
3. (User→Markus) Reservierungen: Dampflokwerk-Gruppenanmeldung, Brückenmühle,
   Berghaus Rhön
4. (User) Orga-Handynummern + Teilnehmerdaten liefern → Claude trägt ein
5. (Claude, optional angeboten) Mapillary-Fotos für knifflige Abzweige
   (kleine Berghaus-Einfahrt); PowerPoint fürs Briefing aus gleichem Inhalt
6. (User) Druckerei/Ausdruck der finalen PDFs, wenn Punkte 1–4 eingepflegt

## 6. Bekannte Lücken / Blocker

- Führungszeit 11:30 ist unbestätigter Planwert – steht so markiert im Heft;
  nur Markus kennt die gebuchte Zeit (Claude kann nicht anrufen)
- Street-View-Bilder verworfen (Google-Lizenz verbietet Abdruck) –
  Alternative Mapillary/eigene Testfahrt-Fotos noch nicht beauftragt
- Rückkehr 18:30 bei Sonnenuntergang 18:55: wenig Puffer; bei späterer
  Führung als 11:30 wird die letzte Etappe zur Dämmerungsfahrt

## 7. Wiedereinstieg

```
cd /Users/ct/bmw6er-ausfahrt
python3 -m http.server 8791 &   # Vorschau: http://localhost:8791/
# PDF neu bauen:
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless \
  --disable-gpu --virtual-time-budget=25000 --no-pdf-header-footer \
  --print-to-pdf=roadbook-a5.pdf "http://localhost:8791/handout.html"
git push   # Pages deployt automatisch (~40 s)
```
