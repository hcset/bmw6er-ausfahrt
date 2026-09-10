#!/usr/bin/env python3
"""Geocodiert Wegpunkte und baut die Route per OSRM.

Ergebnis: daten/route.json (Etappen mit Distanz/Dauer + GeoJSON-Linien),
karten/ausfahrt.gpx (komplette Route fuer Navi).
"""
import json
import time
import urllib.parse
import urllib.request
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
UA = {"User-Agent": "bmw6er-ausfahrt-roadbook/1.0 (privates Club-Handout)"}

# Wegpunkte je Etappe, in Fahr-Reihenfolge. Nominatim-Suchstrings.
ETAPPEN = {
    "1": [
        "Hotel Bayerischer Hof, Bad Kissingen",
        "Flugplatz, Bad Kissingen",
        "Untere Saline, Bad Kissingen",
        "Nüdlingen",
        "Meininger Straße, Münnerstadt",
        "Bad Neustadt an der Saale",
        "Heustreu",
        "Oberstreu",
        "Bahnhof, Mellrichstadt",
        "Dampflok Erlebniswelt, Meiningen",
        "Landsberger Straße, Meiningen",
        "Brückenmühle, Meiningen",
    ],
    "2": [
        "Brückenmühle, Meiningen",
        "Stepfershausen",
        "Dörrensolz",
        "Oberkatz",
        "Aschenhausen",
        "Kaltensundheim",
        "Reichenhausen, Thüringen",
        "Frankenheim/Rhön",
        "Birx",
        "Seiferts, Ehrenberg",
        "Deutsches Segelflugmuseum, Gersfeld",
        "Abtsroda, Poppenhausen",
        "Guckaisee",
        "Gersfeld",
        "Schwedenschanze, Rhön",
        "Riedenberg",
        "Berghaus Rhön, Riedenberg",
    ],
    "3": [
        "Berghaus Rhön, Riedenberg",
        "Schildeck, Bad Brückenau",
        "Poppenroth, Bad Kissingen",
        "Klaushof, Bad Kissingen",
        "Hotel Bayerischer Hof, Bad Kissingen",
    ],
}


def geocode(q: str):
    url = "https://nominatim.openstreetmap.org/search?" + urllib.parse.urlencode(
        {"q": q, "format": "json", "limit": 1, "countrycodes": "de"}
    )
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=30) as r:
        data = json.load(r)
    time.sleep(1.1)  # Nominatim-Ratelimit
    if not data:
        return None
    return {"q": q, "lat": float(data[0]["lat"]), "lon": float(data[0]["lon"]),
            "name": data[0]["display_name"]}


def haversine_km(a, b):
    import math
    lat1, lon1, lat2, lon2 = map(math.radians, (a[1], a[0], b[1], b[0]))
    h = (math.sin((lat2 - lat1) / 2) ** 2
         + math.cos(lat1) * math.cos(lat2) * math.sin((lon2 - lon1) / 2) ** 2)
    return 2 * 6371 * math.asin(math.sqrt(h))


def prune_spurs(coords):
    """Entfernt Hin-und-zurueck-Stiche (Geocode-Snap auf Seitenstrassen):
    Muster ...A,B,A... wird zu ...A... reduziert, iterativ."""
    coords = [tuple(c) for c in coords]
    changed = True
    while changed:
        changed = False
        out = []
        i = 0
        while i < len(coords):
            if out and i + 1 < len(coords) and coords[i + 1] == out[-1]:
                i += 2  # B und zweites A verwerfen
                changed = True
            else:
                out.append(coords[i])
                i += 1
        coords = out
    # Doppelte aufeinanderfolgende Punkte entfernen
    dedup = [coords[0]]
    for c in coords[1:]:
        if c != dedup[-1]:
            dedup.append(c)
    return [list(c) for c in dedup]


def osrm_route(coords):
    path = ";".join(f"{c['lon']:.6f},{c['lat']:.6f}" for c in coords)
    url = (f"https://router.project-osrm.org/route/v1/driving/{path}"
           "?overview=full&geometries=geojson&steps=false&continue_straight=false")
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=60) as r:
        data = json.load(r)
    if data.get("code") != "Ok":
        raise RuntimeError(f"OSRM: {data.get('code')} {data.get('message')}")
    route = data["routes"][0]
    raw = route["geometry"]["coordinates"]
    pruned = prune_spurs(raw)
    km = sum(haversine_km(pruned[i], pruned[i + 1]) for i in range(len(pruned) - 1))
    # Dauer proportional zur bereinigten Distanz skalieren
    faktor = km / (route["distance"] / 1000) if route["distance"] else 1
    print(f"  Spur-Pruning: {len(raw)} -> {len(pruned)} Punkte, "
          f"{route['distance']/1000:.1f} -> {km:.1f} km")
    return {"distance_km": km,
            "duration_min": route["duration"] / 60 * faktor,
            "geometry": {"type": "LineString", "coordinates": pruned}}


def main():
    cache_file = BASE / "daten" / "geocode_cache.json"
    cache = json.loads(cache_file.read_text()) if cache_file.exists() else {}

    fehler = []
    for etappe, punkte in ETAPPEN.items():
        for q in punkte:
            if q in cache:
                continue
            res = geocode(q)
            if res is None:
                fehler.append(q)
                print(f"NICHT GEFUNDEN: {q}")
            else:
                cache[q] = res
                print(f"ok: {q} -> {res['lat']:.4f},{res['lon']:.4f}")
    cache_file.write_text(json.dumps(cache, ensure_ascii=False, indent=1))
    if fehler:
        print(f"\n{len(fehler)} Punkte fehlen — erst fixen, dann Routing.")
        return

    out = {}
    for etappe, punkte in ETAPPEN.items():
        coords = [cache[q] for q in punkte]
        r = osrm_route(coords)
        out[etappe] = {"wegpunkte": coords, **r}
        print(f"Etappe {etappe}: {r['distance_km']:.1f} km, "
              f"{r['duration_min']:.0f} min (OSRM-Normaltempo)")
        time.sleep(1)

    (BASE / "daten" / "route.json").write_text(
        json.dumps(out, ensure_ascii=False), encoding="utf-8")

    # GPX: eine Datei, drei Tracks
    gpx = ['<?xml version="1.0" encoding="UTF-8"?>',
           '<gpx version="1.1" creator="bmw6er-roadbook" '
           'xmlns="http://www.topografix.com/GPX/1/1">',
           '<metadata><name>BMW 6er Club Ausfahrt 03.10.2026</name></metadata>']
    namen = {"1": "Etappe 1 Bad Kissingen–Meiningen",
             "2": "Etappe 2 Meiningen–Berghaus Rhön",
             "3": "Etappe 3 Berghaus Rhön–Bad Kissingen"}
    for etappe in ("1", "2", "3"):
        gpx.append(f"<trk><name>{namen[etappe]}</name><trkseg>")
        for lon, lat in out[etappe]["geometry"]["coordinates"]:
            gpx.append(f'<trkpt lat="{lat:.6f}" lon="{lon:.6f}"/>')
        gpx.append("</trkseg></trk>")
    gpx.append("</gpx>")
    (BASE / "karten" / "ausfahrt.gpx").write_text("\n".join(gpx), encoding="utf-8")
    print("route.json + ausfahrt.gpx geschrieben.")


if __name__ == "__main__":
    main()
