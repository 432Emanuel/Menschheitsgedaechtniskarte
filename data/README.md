# Data Directory

Dieses Verzeichnis enthält ergänzende Datenlayer für die Menschheitsgedächtniskarte.

## Struktur

```
data/
├── schema/                    # Kanonische Schema-Definitionen
│   ├── node_schema.json       # Schema für alle Nodes
│   ├── edge_schema.json       # Schema für alle Edges
│   └── README.md            # Schema-Dokumentation
│
├── modules/
│   └── build_on_old/        # Schichtungs-Analyse (Overbuild, Spolien, Iteration)
│       ├── README.md          # Modul-Dokumentation
│       ├── rules.json         # Transformationsregeln
│       ├── concepts.json      # Konzepte des Weiterbauens
│       └── patterns_onkel.json # Legacy-Patterns (optional)
│
├── lenses/
│   └── meta_patterns/        # Meta-Patterns über Domains hinweg
│       ├── patterns.json      # Alle Meta-Patterns
│       └── README.md         # Lens-Dokumentation
│
└── human_cartography/        # Menschkartographie & Individuen-Netzwerk
    ├── README.md             # Modul-Dokumentation
    ├── humanity_potential_space.json # Kanonischer Potenzialraum
    ├── individuals/           # Individuelle Nodes
    ├── edges/                # Individuelle Verbindungen
    └── overlays/             # Optionale Overlays
        └── onkel_resonance_profile.json # Onkel-Perspektive
```

## Module

### Schema-Standards (`data/schema/`)

Enthält die kanonischen Schema-Definitionen für das gesamte System:
- **node_schema.json**: Standard-Schema für alle Nodes (Individuen, Orte, Konzepte, etc.)
- **edge_schema.json**: Standard-Schema für alle Edges (Verbindungen)

Siehe `data/schema/README.md` für Details.

### Build on Old (`data/modules/build_on_old/`)

Analysiert und dokumentiert Schichtungs-Phänomene:
- **Materielles Weiterbauen**: Neue Bauten auf alten Fundamenten
- **Semantisches Weiterbauen**: Alte Symbole, neue Bedeutung
- **Praktisches Weiterbauen**: Iterative Verbesserung von Techniken
- **Institutionelles Weiterbauen**: Neue Ordnungen auf alten Strukturen

Kernkonzepte:
- **Overbuild**: Neue Struktur über älterer Struktur
- **Spolien**: Wiederverwendete Teile aus älteren Kontexten
- **Iteration**: Verbesserung statt Neuanfang

Siehe `data/modules/build_on_old/README.md` für Details.

### Meta-Patterns (`data/lenses/meta_patterns/`)

Wiederkehrende Meta-Muster über Domains hinweg:
- **Hero's Cycle**: Universelles Muster des Hero's Journey
- **Civilization Resonance Loop**: Wie Kulturen Vorgänger transformieren
- **Memory Resonance**: Muster kollektiver Erinnerung
- **Threshold Crossing**: Universelles Muster des Schwellenübergangs
- **Ritual Core Loop**: Grundlegende Struktur von Ritualen

Siehe `data/lenses/meta_patterns/README.md` für Details.

### Human Cartography (`data/human_cartography/`)

Menschkartographie & Individuen-Netzwerk:
- **humanity_potential_space.json**: Kanonischer Raum menschlicher Möglichkeiten
- **individuals/**: Individuelle Nodes (z.B. DE-EMANUEL-1989)
- **edges/**: Individuelle Verbindungen zur Welt
- **overlays/**: Optionale Overlays für verschiedene Perspektiven

## Integration

Die Daten in diesem Verzeichnis sind ergänzend zu den bestehenden Modulen:
- `zeitgeist_module/`: Zeitgeist-Module für kollektive Phänomene
- `modules/`: Spezielle Module (Imperium, Mythos & Verwaltung)
- `family_module/`: Familien-Module
- `knowledge/`: Wissens-Basis
- `shared/`: Geteilte Ressourcen (Kandidaten, Rubriken, Crosslinks)

## Beziehungen

```
data/schema/ → Definiert Standards für alle Nodes und Edges
     ↓
data/lenses/meta_patterns/ → Analytische Lenses über Domains
     ↓
data/modules/build_on_old/ → Schichtungs-Analyse mit Meta-Patterns
     ↓
data/human_cartography/ → Individuelle Realisierung im Potenzialraum
     ↓
shared/, knowledge/, modules/, zeitgeist_module/ → Bestehende Module
```

## Nutzung

### Validierung

JSON-Dateien können gegen die Schemata validiert werden:

```bash
# Node validieren
ajv validate -s data/schema/node_schema.json -d data/human_cartography/individuals/DE-EMANUEL-1989.json

# Edge validieren
ajv validate -s data/schema/edge_schema.json -d data/human_cartography/edges/human_world_edges.json
```

### Schema-Integration

Füge Schema-Referenz zu JSON-Dateien hinzu:

```json
{
  "$schema": "data/schema/node_schema.json",
  "id": "NODE-ID",
  "name": "Node Name",
  "type": "individual"
}
```

## Migration

Für Migration von alten Schemata siehe:
- `data/modules/build_on_old/rules.json`: Transformationsregeln
- `data/schema/README.md`: Schema-Standardisierung

## Weiterführende Informationen

- `data/schema/README.md`: Schema-Standards und Validierung
- `data/modules/build_on_old/README.md`: Build on Old-Konzept
- `data/lenses/meta_patterns/README.md`: Meta-Pattern-Analyse
- `data/human_cartography/README.md`: Human Cartography
