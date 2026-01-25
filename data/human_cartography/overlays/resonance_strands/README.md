# Resonance Strands Overlays

Resonance Strands Overlays erfassen und strukturieren individuelle Resonanzen mit Elementen der Menschheitsgedächtniskarte.

## Struktur

```
data/human_cartography/overlays/resonance_strands/
├── README.md
├── index.json
└── RSO-DE-EMANUEL-1989-0001.json
```

## Dateien

### Overlay-Dateien

Overlay-Dateien enthalten:
- `overlay_id`: Eindeutige Kennung im Format `RSO-{ISO}-{NAME}-{YEAR}-{NUM}`
- `scope`: Geltungsbereich (primärer Träger, Zeitfenster)
- `strands`: Array von Strand-IDs
- `edges`: Verbindungen zwischen Strands (optional)
- `metadata`: Erstellungs- und Statusinformationen

### Index-Datei

`index.json` enthält eine Übersicht aller Overlays mit Metadaten.

## Schema

Das Schema für Overlays befindet sich unter:
`shared/schemas/resonance_strands/resonance_strands_overlay.schema.json`

## Integration

### Mit Individuen

Individuen-Dateien können optionale `resonance_overlays` referenzieren:

```json
{
  "individual_id": "DE-EMANUEL-1989",
  "resonance_overlays": [
    {
      "overlay_id": "RSO-DE-EMANUEL-1989-0001",
      "description": "Resonance Strands Overlay mit IRS zur Archäoastronomie"
    }
  ]
}
```

### Mit Nodes

Nodes können optional `resonance_strands` referenzieren (siehe `knowledge/schema/node_schema_v2.json`).

## Beispiele

- `RSO-DE-EMANUEL-1989-0001.json`: Erstes Overlay mit IRS zur Archäoastronomie und Memory Resonance

## Siehe auch

- [Strand-Definitionen](../../lenses/resonance_strands/strands/)
- [Vokabular](../../../shared/schemas/resonance_strands/strand_vocab.json)
- [Strand-Schema](../../../shared/schemas/resonance_strands/RS_strand.schema.json)