# Resonance Strands

Resonance Strands sind detaillierte Beschreibungen individueller Resonanzen mit Elementen der Menschheitsgedächtniskarte.

## Struktur

```
data/lenses/resonance_strands/
├── README.md
├── strands/
│   └── RS-IRS-EMANUEL-ARCHASTRO-0001.json
└── vocab/
    └── (Erweiterungen zu strand_vocab.json)
```

## Dateien

### Strand-Dateien

Strand-Dateien enthalten:
- `strand_id`: Eindeutige Kennung im Format `RS-{TYPE}-{CARRIER}-{NUM}`
- `strand_type`: Art des Strands (IRS, FRS, OeRS)
- `carrier`: Träger des Strands (Individuum, Familie, etc.)
- `motifs`: Wiederkehrende Muster und Themen
- `couplings`: Verbindungen zu Elementen der Menschheitsgedächtniskarte
- `evidence`: Belege und Quellen
- `time_window`: Zeitlicher Kontext (optional)
- `metadata`: Erstellungs- und Statusinformationen

## Strand-Typen

- **IRS** (Individueller Resonanzstrang): Resonanzen auf individueller Ebene
- **FRS** (Familiärer Resonanzstrang): Resonanzen in familiären Strukturen
- **OeRS** (Öffentlicher Resonanzstrang): Resonanzen in öffentlichen/kulturellen Kontexten

## Coupling-Modes

Verbindungen zu anderen Elementen können folgende Modi haben:
- `amplifies`: Verstärkt die Wirkung
- `dampens`: Dämpft die Wirkung
- `filters`: Filtert bestimmte Aspekte
- `translates`: Übersetzt in anderen Kontext
- `gates`: Steuert den Zugang
- `echoes`: Spiegelt Muster wider
- `conflicts_with`: Steht in Konflikt

## Evidence-Grades

Qualitätsstufen für Belege:
- `raw_observation`: Direkte Wahrnehmung (niedrige Konfidenz)
- `reported`: Berichtete Erfahrung (mittlere Konfidenz)
- `documented`: Systematisch dokumentiert (hohe Konfidenz)
- `verified`: Extern verifiziert (sehr hohe Konfidenz)

## Schemas

- **Overlay-Schema**: `shared/schemas/resonance_strands/resonance_strands_overlay.schema.json`
- **Strand-Schema**: `shared/schemas/resonance_strands/RS_strand.schema.json`
- **Vokabular**: `shared/schemas/resonance_strands/strand_vocab.json`

## Beispiele

- `RS-IRS-EMANUEL-ARCHASTRO-0001.json`: IRS zur Archäoastronomie und Memory Resonance

## Integration

### Mit Overlays

Strands werden in Overlay-Dateien referenziert:

```json
{
  "overlay_id": "RSO-DE-EMANUEL-1989-0001",
  "strands": [
    "RS-IRS-EMANUEL-ARCHASTRO-0001"
  ]
}
```

### Mit Nodes

Nodes können Strands über das `resonance_strands` Array referenzieren (siehe `knowledge/schema/node_schema_v2.json`).

## Erstellung neuer Strands

1. Bestimme Strand-Typ (IRS, FRS, OeRS)
2. Identifiziere Träger und Zeitfenster
3. Erfasse Motifs mit Häufigkeit und Intensität
4. Dokumentiere Couplings zu existierenden Elementen
5. Füge Evidence-Belege hinzu
6. Referenziere den Strand im entsprechenden Overlay

## Siehe auch

- [Overlay-Definitionen](../../human_cartography/overlays/resonance_strands/)
- [Vokabular](../../../shared/schemas/resonance_strands/strand_vocab.json)