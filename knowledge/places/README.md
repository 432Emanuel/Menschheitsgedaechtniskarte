# Places - Orte im Menschheitsgedächtniskarte-Projekt

## Überblick

Dieser Ordner verwaltet **Place-Daten** – einzelne Orte, die für das MGK-Projekt relevant sind. Places können sein:

- Archäologische Stätten
- Monumente und Denkmäler
- Natürliche Formationen
- Historische Bauwerke
- Ritual- und Kultorte

## Struktur

```
knowledge/places/
├── README.md                      (Diese Datei)
├── index.json                     (Index aller Places)
├── resonance_index.json           (Index der Resonanz-Orte)
├── items/                         (Einzelne Place-Dateien)
│   ├── PLACE-DE-GOSECK-0001.json
│   ├── PLACE-DE-LEIPZIG-VOELKERSCHLACHTDENKMAL-0001.json
│   └── ...
├── resonance_sites/               (Bestehende Resonanz-Sites)
├── places_archaeoastronomy.json   (Archäoastronomie-Collection)
└── candidates_archaeoastronomy.json
```

## Place-Datei-Struktur

Jede Place-Datei in `items/` enthält mindestens:

### Basisinformationen
- `type`: "place"
- `identifier`: Eindeutige ID (z.B. "PLACE-DE-GOSECK-0001")
- `title`: Name des Ortes
- `country`: Ländercode (ISO 3166-1 alpha-2)
- `region`: Region/Bundesland (optional)
- `location`: Stadt, Koordinaten (optional)

### Zeitliche Einordnung
- `timeframe`: Periodenangabe

### Tags
- `tags`: Array von Tag-IDs (aus `shared/vocabularies/tags.json`)

### Beschreibungen
- `descriptions`: Mehrsprachige Kurzbeschreibungen

### Quellen
- `sources`: Quellenangaben

### Optional: Resonanz-Profil

Places können einen optionalen `resonance_profile`-Block enthalten:

```json
"resonance_profile": {
  "version": "0.1",
  "classification": ["ritual_landscape", "monument", "cave", ...],
  "channels": ["acoustics", "light", "verticality", "enclosure", ...],
  "thresholds": [
    {
      "name": "Eingang / Schwelle",
      "description": "Kurz neutrales Feld"
    }
  ],
  "affordances": [
    {
      "action": "gehen|stehen|schweigen|sprechen|...",
      "notes": "Was der Körper hier tun kann"
    }
  ],
  "expected_effects": [
    "Phänomenologisch formulierte Effekte"
  ],
  "marker_links": [],
  "notes": "Freifeld für Hinweise"
}
```

## Resonanz-Index

Der `resonance_index.json` listet alle Places mit Resonanz-Profil:

- Filterbar nach Tags
- Klassifizierung
- Kanälen

## Nutzung

### Für Autoren
- Legen Sie neue Places als einzelne JSON-Dateien unter `items/` an
- Verwenden Sie das bestehende Tag-Vokabular
- Fügen Sie bei Bedarf `resonance_profile` hinzu
- Tragen Sie die neue Datei in `index.json` ein

### Für Module/Lenses
- Places können über Marker-IDs mit Lenses verknüpft werden
- Resonanz-Profile ermöglichen phänomenologische Zugänge
- Tags ermöglichen maschinelle Filterung

## Bestehende Sammlungen

- `resonance_sites/`: Akustische Resonanzorte (12 Orte, Europa-Fokus)
- `places_archaeoastronomy.json`: Archäoastronomische Orte (große Sammlung)
- `candidates_archaeoastronomy.json`: Kandidatenliste

## Verwandte Dateien

- `shared/vocabularies/tags.json`: Tag-Vokabular
- `knowledge/layers/`: Epistemic/Resonance Layers

---

**Stand**: 2026-02-19
**Version**: 0.1
