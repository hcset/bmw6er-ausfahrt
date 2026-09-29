# HANDOFF – bmw6er-ausfahrt

**Datum:** 2026-09-29, 10:31
**Repo:** `/Users/ct/bmw6er-ausfahrt` (Branch `main`, HEAD `7d14c63`, Tag `v2.3.1`)
**Stand:** DRUCKREIF, eingefroren – wartet auf Baustellen-Lage 02.10. und Markus' Orga-Daten. Diese Session hat am Repo nichts geändert.

---

## 1. Was dieses Projekt ist

Roadbook/Handout für die BMW 6er Club Ausfahrt am Sa 03.10.2026 (Rundkurs Bad
Kissingen – Meiningen – Rhön – Bad Kissingen, ~176 km, 3 Etappen). Eine
HTML-Quelle erzeugt A5-Print-PDF und mobile Webseite; dazu interaktive Karte,
GPX und Zusatzinhalte. Auftraggeber: Freund des Users (Markus Renner,
Tourleitung). Live: https://hcset.github.io/bmw6er-ausfahrt/

## 2. Changelog (diese Session, 29.09.2026)

### Kein Code, keine Commits
Working tree ist clean, HEAD unverändert auf `7d14c63`. Es wurde bewusst
keine Repo-Datei angefasst — Inhalt ist druckreif eingefroren und die
Ausfahrt ist in vier Tagen. Diese Session war Inventur + eine Entscheidung.

### MCP-/Plugin-Inventur (keine Änderung ausgeführt)
- Session-Start-Check: nur `/Users/ct/.claude/CLAUDE.md` geladen, keine
  Projekt-CLAUDE.md in diesem Repo. Memory-Ordner war leer.
- Befund: über 400 Tools beim Start geladen. Größter Einzelposten ist
  Higgsfield mit rund 130 Tools — nicht die Plugins, wie zuerst vermutet.
- 30 Plugin-Server sind reine Stubs, die nur `authenticate` /
  `complete_authentication` anbieten und sonst nichts tun: brand-voice
  (Atlassian, Box, Figma, Gong, Granola, Notion), design (Intercom),
  engineering (Asana, Datadog, GitHub, Linear, PagerDuty, Slack),
  enterprise-search (Guru), finance (BigQuery), marketing (Ahrefs, Canva,
  HubSpot, Klaviyo, Similarweb, Supermetrics), product-management
  (Amplitude ×2, Fireflies, Pendo, Similarweb), productivity (ClickUp, Monday).
- Für DIESES Repo brauchbar: playwright oder claude-in-chrome (HTML prüfen),
  perplexity/firecrawl (Strecken/Sperrungen recherchieren), Gmail +
  Google Drive (PDFs verteilen), serena nur mäßig (reines HTML).
- Empfehlung an den User: Plugins deinstallieren statt sich anzumelden.
  NICHT ausgeführt — das macht der User selbst, siehe Abschnitt 5.

### Higgsfield: geprüft, bewusst nicht eingesetzt
- Abo verifiziert per `mcp__claude_ai_Higgsfield__balance`: Plan `ultra`,
  3000 Credits, bis dahin ungenutzt.
- Vier Optionen bewertet: (A) 5–10 s Teaser-Clip für den Club-Verteiler,
  (B) Erinnerungsvideo NACH dem 03.10. aus echten Teilnehmerfotos,
  (C) Cover-Illustration fürs A5-Heft, (D) reiner Werkzeugtest.
- Entscheidung des Users: **alles so lassen.** Nichts generiert, nichts
  eingebaut.
- Gründe, die auch später gelten: Print war eingefroren und die Ausfahrt
  vier Tage entfernt; generative Modelle treffen E24-Karosseriedetails nicht
  zuverlässig (Nieren, Hofmeister-Knick) und das Oldtimer-Publikum sieht das
  sofort; alle Fotos in `assets/img` stehen unter CC BY / CC BY-SA, als
  Bild-zu-Video-Vorlage zieht das Share-Alike plus Attribution nach.
- Einziger sauberer künftiger Anlass wäre B — eigene Fotos, keine
  Lizenzfrage, keine Deadline.

### Memory-Notiz (außerhalb des Repos)
- Neu: `~/.claude/projects/-Users-ct-bmw6er-ausfahrt/memory/higgsfield-nicht-im-roadbook.md`
  plus Zeile in derselben `MEMORY.md`. Hält die Higgsfield-Entscheidung
  samt Begründung fest, damit sie nicht jede Session neu diskutiert wird.

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

- Es gibt KEINE `package.json`, kein `Makefile`, kein `README.md`. Der
  gesamte Build sind die Chrome-Befehle in Abschnitt 7 — nicht nach einem
  Build-Tool suchen.
- PDF-Erzeugung NUR über lokalen Server (`python3 -m http.server 8791`),
  file:// bricht Leaflet/Fetch; Chrome headless mit
  `--virtual-time-budget=25000 --no-pdf-header-footer`
- Frische --user-data-dir-Profile hängen Chrome headless gelegentlich →
  Default-Profil nutzen oder Prozess killen
- Higgsfield: Plan `ultra`, 3000 Credits (Stand 29.09.2026), für dieses
  Projekt bewusst ungenutzt. Nur wieder aufgreifen, wenn der User es selbst
  anstößt. Kein BMW-Logo generieren (Marke), Auto nie als Detaildarstellung.
- Alle Bilder in `assets/img` sind CC BY / CC BY-SA von Wikimedia → nicht als
  Vorlage für generierte Bilder/Videos verwenden, die veröffentlicht werden.
- Dampflokwerk-Führungen offiziell NUR samstags 10:00 (Apr–Okt); Gruppen ab
  6 Personen anmeldepflichtig, 03693 851602, 6 €/Person BAR
- Kontakte: Brückenmühle 03693 801004 (feste Gerichte für Gruppe vereinbart,
  kein Speisekarten-Link gewünscht) · Berghaus Rhön 09749 9307721 (Sa 10–22,
  Reservierung nur telefonisch) · Hotel Bayerischer Hof 0971 80450
- Etappenfarben-Tokens heißen historisch --blau/--rot/--gruen, enthalten
  aber die 70er-Werte (#b4441c/#6f4520/#7c5f2b); Kartenlinien separat in
  karte.html (#b4441c/#6f4520/#c8a25e)
- SYNC-PFLICHT: Inhalte liegen an 4 Orten (Web/Repo, NotebookLM, Obsidian,
  gedruckte PDFs) – bei Änderungen alle nachziehen
- Design gepinnt: 70er/E24-Ära; impeccable + emil-design-eng bei
  Designarbeit laden (Nutzerregel)

## 5. Offene Aufgaben (in Reihenfolge)

1. (User) Baustellen-Lage am 02.10. prüfen – letzter Check vor dem Druck.
   Bei Änderung: Claude zieht Roadbook-Positionen + PDFs nach
2. (User→Markus) Gebuchte Führungszeit Dampflokwerk bestätigen – bei
   Abweichung von 11:30: Claude rechnet Zeitplan um (Cover-Fakten, Zeitplan,
   Roadbook-Zeile 31, Etappen-Köpfe)
3. (User→Markus) Grußwort-Wording absegnen
4. (User→Markus) Reservierungen: Dampflokwerk-Gruppenanmeldung, Brückenmühle,
   Berghaus Rhön
5. (User) Orga-Handynummern + Teilnehmerdaten liefern → Claude trägt ein
6. (User) Druckerei/Ausdruck der finalen PDFs, wenn 1–5 eingepflegt
7. (User, projektfremd) Plugins aufräumen: finance, marketing, engineering,
   enterprise-search, design, brand-voice, product-management, productivity
   deinstallieren; danach `/usage` gegenprüfen. Größter Brocken bleibt aber
   Higgsfield mit ~130 Tools
8. (Claude, erst nach dem 03.10.) Optional Erinnerungsvideo aus echten
   Teilnehmerfotos via Higgsfield – nur auf Ansage des Users
9. (Claude, optional angeboten) Mapillary-Fotos für knifflige Abzweige
   (kleine Berghaus-Einfahrt); PowerPoint fürs Briefing aus gleichem Inhalt

## 6. Bekannte Lücken / Blocker

- Führungszeit 11:30 ist unbestätigter Planwert – steht so markiert im Heft;
  nur Markus kennt die gebuchte Zeit (Claude kann nicht anrufen)
- Baustellen-Lage 02.10. kann Claude nicht selbst feststellen – hängt an
  Marcus'/User-Testfahrt bzw. Ortskenntnis
- Street-View-Bilder verworfen (Google-Lizenz verbietet Abdruck) –
  Alternative Mapillary/eigene Testfahrt-Fotos noch nicht beauftragt
- Rückkehr 18:30 bei Sonnenuntergang 18:55: wenig Puffer; bei späterer
  Führung als 11:30 wird die letzte Etappe zur Dämmerungsfahrt
- Kein eigenes, rechtlich freies E24-Foto vorhanden – deshalb wäre selbst ein
  Bild-zu-Video-Weg aktuell blockiert. Löst der User, indem er ein eigenes
  Foto (z. B. Markus' Wagen, mit Freigabe) beisteuert

## 7. Wiedereinstieg

```
cd /Users/ct/bmw6er-ausfahrt
git checkout main   # falls noch nicht drauf
python3 -m http.server 8791 &   # Vorschau: http://localhost:8791/
# PDF neu bauen:
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless \
  --disable-gpu --virtual-time-budget=25000 --no-pdf-header-footer \
  --print-to-pdf=roadbook-a5.pdf "http://localhost:8791/handout.html"
git push   # Pages deployt automatisch (~40 s)
```

---

# Ältere Handoffs

# HANDOFF – bmw6er-ausfahrt

**Datum:** 2026-09-29, 10:05
**Repo:** `/Users/ct/bmw6er-ausfahrt` (Branch `main`, HEAD `712c558`, Tag `v2.3.1`)
**Stand:** DRUCKREIF – Inhalt eingefroren, wartet nur noch auf die Baustellen-Lage am 02.10.
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

### Abmahn-Check + Rechtsteil im Heft, v2.3.1 (Commit `712c558`, 29.09.2026)
- 18-Punkte-Selbstcheck vor dem Druck: bestanden. Einziger Befund war, dass
  der Datenschutz-Text in `handout.html` knapper war als der in `index.html`,
  obwohl beide auf `karten/karte.html` verlinken
- Heft trägt jetzt den Wortlaut der Startseite wörtlich (OSMF-Kachelserver
  namentlich, IP-Übertragung, Leaflet lokal) plus das Impressum, das vorher
  nur die Startseite hatte. Vorlage wird im Fix-Script direkt aus
  `index.html` gelesen – die beiden Texte dürfen nicht wieder auseinanderlaufen
- Der Rechtsblock ist im Druck enger gesetzt (`@media print`, `.lizenzen`
  auf 0.62rem/1.35), sonst rutscht die Rückseite auf Seite 23. Heft bleibt
  bei 22 Seiten, gekürzt wurde nichts
- `assets/img/lizenzen.md`: QR-Code dokumentiert, Hinweis dass
  `meiningen.jpg` ausgeliefert, aber nirgends eingebunden wird

### Baustelle Meiningen + Etappe-2-Wegweiser, v2.3.0 (Commit `9922355`, 29.09.2026)
- Zweite Testfahrt von Marcus und Elisa: Baustelle in Meiningen
- Etappe 1: Kreisel vor Meiningen ist die dritte Ausfahrt (war zweite),
  Punkt 23 „über den Kreisverkehr hinaus", Kreisel Henneberger Straße ist
  die erste Ausfahrt Richtung Suhl. Zwei neue Punkte 26/27 umfahren die
  Baustelle (Kreisel zweite Ausfahrt Richtung Sportstätten Meiningen /
  Werrastraße, dann Ampelkreuzung rechts Richtung Fulda). Alte Punkte 26–40
  rutschen auf 28–42, Zwischenziel-Index im Distanz-Script von 31 auf 33,
  Landsberger Straße bekommt „Richtung Fulda"
- Etappe 2: Kaltennordheim statt Kaltensundheim (Punkte 3+5), Aschenhausen
  aus Punkt 5 gestrichen, B284 nach Wüstensachsen Richtung Gersfeld statt
  Bischofsheim, Wasserkuppen-Baustellenhinweis nennt den Wiedereinstieg
  (Punkt 19). Punkt 6 bleibt bewusst „durch Kaltensundheim" – die Wegweiser
  nennen den größeren Ort, gefahren wird weiter durch Kaltensundheim
- Route/Karte/GPX bewusst NICHT angefasst: ein erzwungener Wegpunkt
  Werrastraße ändert die gemessene Distanz um unter 10 m. Nur die PDFs neu
- Heft weiterhin 22 Seiten, Etappe 1 jetzt 42 statt 40 Positionen
- `.serena/` und `daten/__pycache__/` in .gitignore aufgenommen

### Etappe 1 neu durchs Saaletal, v2.2.0 (Commit `7c8908f`, 28.09.2026)
- Marcus ist die Alternative über Aschach abgefahren: Baustelle weg, keine
  Ampeln, schönere Strecke. Roadbook-Positionen 7–14 ersetzt – links in die
  Untere Saline, St 2292 durch Hausen/Kleinbrach/Großenbrach, an Aschach
  vorbei, Kreisel, Hohn/Steinach/Unterebersbach, links auf die St 2445.
  Entfällt: Nordring/Ostring und B287 über Nüdlingen/Münnerstadt
- Unverändert: Positionen 1–6 und 15–40, Etappen 2+3, alle Zeiten und Stopps.
  71,4 → 71,6 km; Gesamt bleibt 176 km, Heft bleibt bei 22 Seiten
- Wegpunkte in `build_route.py` bewusst schlank (Aschach, Steinach,
  Unterebersbach); mehr Zwischenpunkte erzeugen nur Dorfkern-Stiche.
  Rebuild lief nur für Etappe 1 und wurde in route.json gemergt, damit
  E2/E3-Kilometer stehen bleiben
- `karte.html`: tileerror-Retry (3 Versuche) ergänzt – ohne den bleiben beim
  Screenshot der Gesamtkarte graue Kachel-Löcher, der OSM-Kachelserver
  drosselt den Burst. Höheres --virtual-time-budget hilft nicht
- Nachgezogen: e1.jpg, gesamt.jpg, ausfahrt.gpx, beide PDFs, Pages live
  verifiziert, NotebookLM (alte roadbook-a5.pdf + routenbeschreibung.md
  gelöscht, neue hochgeladen, Änderungsnotiz angelegt), Obsidian-Hub

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
   – Stand 28.09.2026 druckreif: neue Etappe 1 + vollständiger Datenschutz-Text drin

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
