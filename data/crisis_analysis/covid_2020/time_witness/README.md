# Time Witness System für COVID-19 Zeitzeugenberichte

## Zweck

Dieses Modul sammelt COVID-19-bezogene Zeitzeugenberichte (2019-2021). Die Berichte werden als eigenständige JSON-Dateien im `time_witness/`-Ordner gespeichert und über die `index.json`-Datei zentral indiziert.

## Struktur

```
time_witness/
├── index.json                 # Zentraler Index aller Berichte
├── ZG-KI-2026-001.json     # Bericht über KI als Resonanz
├── ZG-CB-DE-2020-01.json # COVID-19 und die Ordnung der Welt (DE)
├── ZG-CB-DE-2020-02.json # Fortsetzung (DE)
├── ZG-CB-VE-2020-01.json # COVID-19 und die Ordnung der Welt (VE)
├── ZG-CB-VE-2020-02.json # Italien (IT)
├── README.md                   # Diese Datei
└── raw/                     # Rohe Interview-Transkripte (optional)
```

## Bericht-Typen

Das System unterstützt verschiedene Arten von Zeitzeugenberichten:

### COVID-19 Berichte (ZG-CB)
- **ZG-CB-DE-2020-01**: "COVID-19 und die Ordnung der Welt" (DE)
- **ZG-CB-DE-2020-02**: "Fortsetzung" (DE)
- **ZG-CB-VE-2020-01**: "COVID-19 und die Ordnung der Welt" (Venezuela)
- **ZG-CB-VE-2020-02**: "Italien" (IT)

### Zeitzeugenberichte (ZG-KI, ZG-RISE)
- **ZG-KI-2026-001**: "KI als Resonanz und Erkenntnisverstärker" (DE)
- **ZG-RISE-2026-001**: "Gesellschaftliche Dynamiken in Krisenzeiten" (DE)

## JSON-Struktur

Jeder Bericht ist eine eigenständige JSON-Datei mit folgendem Schema:

```json
{
  "id": "ZG-XXXX-202X-XX",
  "type": "zeitzeugenbericht",
  "title": "Titel des Berichts",
  "timeframe": {
    "period": "2020–2021",
    "context": "Krisenkontext"
  },
  "thematic_domain": [
    "Krise",
    "Gesellschaft",
    "..."
  ],
  "core_observations": [
    "Beobachtung 1",
    "Beobachtung 2",
    "Beobachtung 3"
  ],
  "key_tensions": [
    "Spannung 1",
    "Spannung 2"
  ],
  "zeitzeugen_these": "Hauptthese des Berichts",
  "related_lenses": [
    "Resonanz",
    "Macht",
    "..."
  ],
  "status": "draft",
  "created_at": "YYYY-MM-DD",
  "notes": "Zusätzliche Anmerkungen"
}
```

## Feld-Beschreibungen

### Metadaten
- **id**: Eindeutige ID (Präfix + Jahr + Typ-Nummer)
- **type**: Berichttyp ("zeitzeugenbericht" für alle COVID-19- und ZG-Berichte)
- **title**: Vollständiger Titel
- **timeframe**: Zeitliche Einordnung (period, context)
- **thematic_domain**: Thematische Domains (max. 3-5)
- **core_observations**: Beobachtete Aussagen (min. 3)
- **key_tensions**: Identifizierte Spannungen (min. 3)
- **zeitzeugen_these**: Kernaussage oder Hauptthese
- **related_lenses**: Verweise auf Patterns oder Lenses
- **status**: "draft", "published", "archived"

## Namenskonventionen

### COVID-19 Berichte (ZG-CB)
Format: `ZG-CB-{LÄNDER}-{JAHR}-{JAHR}-{NUM}`

Beispiele:
- `ZG-CB-DE-2020-01`: Deutschland, 2020, Bericht 1
- `ZG-CB-VE-2020-01`: Venezuela, 2020, Bericht 1

### Zeitzeugenberichte (ZG-KI, ZG-RISE)
Format: `ZG-{TYP}-{JAHR}-{JAHR}-{NUM}`

Beispiele:
- `ZG-KI-2026-001`: Deutschland, 2026, Bericht 1
- `ZG-RISE-2026-001`: Deutschland, 2026, Bericht 1

## Index-Verwaltung

Die `index.json`-Datei verwaltet alle Berichte:

```json
{
  "reports": [
    {
      "id": "ZG-CB-DE-2020-01",
      "title": "COVID-19 und die Ordnung der Welt",
      "date": "2020-01-01"
    },
    {
      "id": "ZG-KI-2026-001",
      "title": "KI als Resonanz und Erkenntnisverstärker",
      "date": "2026-01-25"
    }
    // ... weitere Berichte
  ]
}
```

## Guidelines für neue Berichte

1. **ID-Nummerierung**: Verwende bestehende Nummern und wähle die nächste freie
2. **Titelwahlung**: Prägnante, deskriptiv und thematisch relevant
3. **Dateiformat**: ISO 8601 (YYYY-MM-DD)
4. **Themen-Domains**: Wähle max. 3-5 thematisch relevante Domains
5. **Beobachtungen**: Füge min. 3 kernhafte Aussagen hinzu
6. **Spannungen**: Identifiziere max. 3 Schlüsselspannungen
7. **Status**: Beginne immer mit "draft", erst bei Veröffentlichung auf "published"
8. **Verknüpfungen**: Füge relevante Patterns oder Lenses hinzu

## Integration mit anderen Modulen

### Resonance Strands
Berichte können mit `related_lenses` auf Resonance Patterns verweisen:
```json
"related_lenses": [
  "Resonanz",
  "Memory Resonanz",
  "Kollektive Intelligenz"
]
```

### Zeitgeist-Module
Berichte können mit thematischen Domains auf ZG-Module verweisen (z.B. "Gesellschaft", "Macht").

### Pattern Lenses
Berichte können als analytische Werkzeuge dienen (vgl. META-PAT-006 "Leise Integration vs. laute Disruption").

## Versionsverwaltung

Berichte sollten versioniert werden, wenn wesentliche Änderungen vorgenommen werden:
1. **Minor-Änderungen**: Korrekturen, Ergänzungen (nur created_at aktualisieren)
2. **Major-Änderungen**: Neue Strukturen, neue Kernthesen (neue ID erstellen)

## Metadaten

- **Modul**: `data/crisis_analysis/covid_2020/time_witness`
- **Erstellt**: 2026-01-25
- **Zuletzt aktualisiert**: 2026-01-25

## Best Practices

1. **Konsistenz**: Alle Berichte sollten einheitliches Schema befolgen
2. **Neutralität**: Berichte als eigenständige Objekte behandeln, keine Hierarchien
3. **Chronologische Ordnung**: Berichte nach Datum im Index sortieren
4. **Rückwärtskompatibilität**: Neue Berichtstypen können hinzugefügt werden, ohne bestehende zu brechen
5. **Dokumentation**: Jede Änderung sollte dokumentiert werden (in `notes` oder in separater README)

## Verweise

- [COVID-19-Module](../zeitgeist_module/ZG-CB/)
- [Meta-Patterns](../../lenses/meta_patterns/)
- [Pattern Lenses Dokumentation](../../src/tools/pattern_lenses/)
- [Projekt-Übersicht](../../README.md)

## Status

- ✅ Modul-Struktur erstellt
- ✅ Index-System implementiert
- ✅ Benennskonventionen definiert
- ✅ COVID-19- und ZG-Berichte integriert
- ✅ README-Dokumentation erstellt

Das System ist bereit für die Verwaltung weiterer Zeitzeugenberichte und COVID-19-Analysen.