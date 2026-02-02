# Epistemic Documents (Zeitdokumente / Artefakte der Wissenspraxis)

## Konzeptionelle Abgrenzung

### Was sind epistemische Dokumente?

Epistemische Dokumente sind **Artefakte der Wissenspraxis** – materiale Dokumente, die zeigen, wie Menschen zu bestimmten Zeiten versucht haben, die Welt zu kartographieren, zu vermessen, zu projizieren oder systematisch zu erfassen.

**Beispiele:**
- Karten (Weltkarten, Seekarten, Landkarten)
- Globen
- Atlanten
- Geodätische Messkampagnen
- Projektionssysteme
- Wissenschaftliche Datensätze
- Navigationshandbücher

### Wichtige Abgrenzung: Nicht Zeitzeugen!

Epistemische Dokumente sind **keine** Zeitzeugen im Sinne der Menschheitsgedächtniskarte:

| Zeitzeugen | Epistemische Dokumente |
|------------|------------------------|
| Innenperspektive: Menschen berichten über ihre Erlebnisse | Außenperspektive: Artefakte zeigen, was dokumentiert wurde |
| Subektive Erfahrung, Emotionen, Deutungen | Objekte mit technischen Merkmalen, Provenienz, Materialität |
| "Wie es sich angefühlt hat" | "Was existierte und wie es dargestellt wurde" |
| Beispiel: Interview mit einem Klimaaktivisten 2026 | Beispiel: Klimadaten-Satellitenmesskampagne 1979 |

## Epistemologische Haltung

Dieses Modul folgt einem strikten **Dokumentations-ohne-Validierungs-Prinzip**:

1. **Was existiert, wird dokumentiert** – Das Artefakt wird beschrieben mit allen relevanten technischen und historischen Details.
2. **Nicht bewertet, ob es "stimmt"** – Wir dokumentieren nicht, ob die Karte korrekt war, sondern was sie zeigte.
3. **Rätsel entstehen im Vergleich** – Erst durch den Vergleich verschiedener epistemischer Dokumente werden Widersprüche, Lücken und Entwicklungen sichtbar.

### Beispiel: Antarktis auf historischen Karten

- Caverio-Karte (1505): Zeigt Küstenlinien, die nicht existieren
- Ortelius (1570): Zeigt "Terra Australis"
- Moderne Satellitenkartographie (1979+): Präzise Eisoberflächen

**Wir dokumentieren nicht:** "Die Caverio-Karte war falsch."
**Wir dokumentieren:** "Die Caverio-Karte zeigt Küstenlinien in Regionen, die heute als eisbedeckt gelten. Dies steht im Kontrast zu modernen Messungen, die keine Landmasse anzeigen."

Das Rätsel ("Warum zeigten sie Küsten?") entsteht erst durch den Vergleich – nicht durch vorweggenommene Bewertung.

## Verzeichnisstruktur

```
knowledge/epistemic_documents/
├── README.md                        # Diese Datei
├── index.json                       # Haupt-Index mit Statistiken
├── cartography/                     # Kartographie-Daten
│   ├── timelines/                   # Zeitleisten der Kartographie
│   ├── maps/                        # Einzelne Karten
│   ├── globes/                      # Globen
│   └── atlases/                     # Atlanten
└── [zukünftige Domains]/
    ├── geodesy/                     # Geodäsie
    ├── remote_sensing/              # Fernerkundung
    └── navigation/                  # Navigation
```

## Dateinamenskonventionen

Epistemische Dokumente folgen einem konsistenten Benennungsschema:

```
<KIND>-<SCOPE>-<NAME/IDENTIFIER>-<YEAR>.json
```

**Beispiele:**
- `MAP-WORLD-CAVERIO-1505.json` – Weltkarte von Caverio, ca. 1505
- `GLOBE-WORLD-BEHAIM-1492.json` – Erdglobus von Behaim, 1492
- `ATLAS-EUROPE-STIELER-1878.json` – Stielers Handatlas, 1878
- `MAP-ATLANTIC-CANTINO-1502.json` – Cantino-Planisphäre, 1502

## Schema

Alle epistemischen Dokumente müssen das Schema in `shared/schemas/epistemic_documents/epistemic_document.schema.json` erfüllen.

**Pflichtfelder:**
- `type`: Immer "epistemic_document"
- `id`: Eindeutige ID (folgt Dateinamenskonvention)
- `title`: Titel des Dokuments
- `domain`: Wissensdomain (cartography, geodesy, etc.)
- `document_kind`: Art des Dokuments (map, globe, etc.)
- `date_range`: Zeitliche Einordnung (mindestens start_year)
- `provenance`: Herkunft und Quellenangabe

**Optionale Felder:**
- `creators`: Ersteller mit Rollen
- `region_scope`: Geografischer Geltungsbereich
- `technical`: Technische Details (Projektion, Maßstab, Material)
- `claims_and_limits`: Was das Dokument zu zeigen beansprucht und bekannte Einschränkungen
- `links`: Verknüpfungen zu anderen MGK-Entitäten
- `tags`: Freie Tags für Kategorisierung

## Workflow: Ein neues Dokument hinzufügen

1. **Datei erstellen** im entsprechenden Unterverzeichnis (z.B. `cartography/maps/`)
2. **Schema validieren** mit `ajv validate -s shared/schemas/epistemic_documents/epistemic_document.schema.json -d <deine-datei>.json`
3. **Index aktualisieren** in `index.json`:
   - Dokument-ID zur passenden Liste hinzufügen
   - Statistiken aktualisieren
4. **Commit** mit aussagekräftiger Nachricht

## Beispiel: Die Caverio-Karte

Siehe `cartography/maps/MAP-WORLD-CAVERIO-1505.json` für ein vollständiges Beispiel.

## Ziele dieses Moduls

1. **Artefakte konsistent dokumentieren** – Standardisierte Beschreibung historischer und zeitgenössischer Wissensdokumente
2. **Vergleichbarkeit ermöglichen** – Durch konsistente Struktur können Karten/Globen/etc. über Epochen hinweg verglichen werden
3. **Wissensgeschichte sichtbar machen** – Entwicklung kartographischer/geodätischer Praktiken nachverfolgbar machen
4. **Rätsel generieren** – Widersprüche zwischen Dokumenten werden sichtbar, nicht vorweg "gelöst"

## Zukünftige Erweiterungen

- **Geodesy**: Triangulationskampagnen, Gradmessungen, ellipsoide Modelle
- **Remote Sensing**: Satellitenmissionen, Luftbildarchive, LiDAR-Daten
- **Navigation**: Portolankarten, Navigationshandbücher, Sextant-Beobachtungen
- **Bathymetry**: Tiefenkarten der Ozeane, Echolot-Messungen

## Verwandte Module

- `knowledge/places/` – Orte, die auf epistemischen Dokumenten verzeichnet sind
- `data/lenses/` – Analytische Linsen für Vergleich und Interpretation
- `shared/markers/` – Marker für interessante Widersprüche oder Übereinstimmungen