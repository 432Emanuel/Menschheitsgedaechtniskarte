# Crosslinks

Dieses Verzeichnis enthält Querverweise (Crosslinks) zwischen allen Modulen der Menschheitsgedächtniskarte.

## Konzept

Crosslinks verbinden verschiedene Knoten (Nodes) aus unterschiedlichen Modulen:
- Zeitgeist-Module
- Familienmodule
- Imperium-Module
- Knowledge-Layer
- Human Cartography
- Build on Old

## Struktur

- `links.json` - Alle Crosslinks im Repository
- `example_link.json` - Beispiel für einen Crosslink
- `README.md` - Diese Datei

## Link-Typen

### Verbindungstypen (Edge Types)

| Typ | Beschreibung | Beispiel |
|-----|-------------|-----------|
| `supports` | Positiver Support, Bestätigung | Ein Zeitgeist-Modul unterstützt ein Pattern |
| `contradicts` | Widerspruch, Spannung | Ein Pattern widerspricht einem anderen |
| `informs` | Informative Verbindung | Ein Modul liefert Kontext zu einem anderen |
| `analogous_to` | Analogie, Ähnlichkeit | Zwei Patterns sind ähnlich strukturiert |
| `inspired_by` | Inspirationsbeziehung | Ein Element wurde durch ein anderes inspiriert |
| `resonant` | Resonanzverbindung | Starke emotionale/intellektuelle Resonanz |
| `conflict` | Konfliktbeziehung | Ambivalente oder spannungsreiche Verbindung |
| `neutral` | Neutrale Verbindung | Verbindung ohne starke Bewertung |
| `origin` | Ursprungsverbindung | Creator/Creator-Beziehung |

## Struktur eines Links

```json
{
  "id": "LINK-20220122143000",
  "source_id": "ZG-001-memory-loss",
  "target_id": "BOL-CON-003",
  "link_type": "resonant",
  "strength": 0.8,
  "description": "Das Phänomen des Erinnerungsverlusts resoniert stark mit dem Memory Resonance Konzept",
  "timestamp": "2026-01-22",
  "metadata": {
    "verified": true,
    "context": "manual_entry"
  }
}
```

### Felder

- `id`: Eindeutige Kennung für den Link
- `source_id`: ID des Quellknotens
- `target_id`: ID des Zielknotens
- `link_type`: Typ der Verbindung (siehe Tabelle oben)
- `strength`: Stärke der Verbindung (0.0 - 1.0)
- `description`: Beschreibung der Verbindung
- `timestamp`: Datum der Erstellung
- `metadata`: Zusätzliche Metadaten
  - `verified`: Ob der Link verifiziert wurde
  - `context`: Kontext der Erstellung (manual_entry, automatic, etc.)

## Verwendung

### Tool-basierte Verwaltung

```bash
# Interaktive Link-Erstellung
python src/tools/link_nodes.py

# Links validieren
python src/tools/link_nodes.py --validate

# Links exportieren (JSON)
python src/tools/link_nodes.py --export json

# Links exportieren (CSV)
python src/tools/link_nodes.py --export csv
```

### Manuelle Verwaltung

1. Öffne `links.json`
2. Füge neuen Link zum `links`-Array hinzu
3. Aktualisiere `metadata.updated`
4. Speichere die Datei

## Integration mit anderen Modulen

### Human Cartography

Human Cartography verwendet ein spezielles Edge-System für Individuum ↔ Welt-Verbindungen:
- Datei: `data/human_cartography/edges/human_world_edges.json`
- Ähnliche Struktur, aber für individuelle Perspektiven

### Build on Old

Build on Old definiert Transformationsregeln für Legacy-Strukturen:
- Datei: `data/modules/build_on_old/rules.json`
- BOL-RULE-004: Crosslink Normalization

## Validierung

Das `link_nodes.py` Tool validiert automatisch:
- Existenz der verlinkten Knoten
- Gültigkeit des Link-Typs
- Range der Stärke (0.0 - 1.0)
- Vollständigkeit der Pflichtfelder

## Best Practices

1. **Präzise Beschreibungen**: Erkläre WARUM zwei Knoten verbunden sind
2. **Stärke-Relevanz**: Nutze 1.0 nur für absolute Klärungen, 0.5 für Standards
3. **Konsistente Typen**: Verwende Link-Typen konsistent über das gesamte Repository
4. **Regelmäßige Validierung**: Führe `--validate` regelmäßig aus
5. **Kontext-Metadaten**: Dokumentiere den Entstehungskontext

## Beispiele

### Beispiel 1: Zeitgeist-Modul ↔ Pattern

```json
{
  "id": "LINK-ZG-PAT-001",
  "source_id": "ZG-001-memory-loss",
  "target_id": "BOL-CON-003",
  "link_type": "resonant",
  "strength": 0.8,
  "description": "Das Phänomen des kollektiven Erinnerungsverlusts resoniert mit dem Memory Resonance Pattern"
}
```

### Beispiel 2: Individuum ↔ Welt (Human Cartography)

```json
{
  "id": "EDGE-EMANUEL-001",
  "individual_id": "DE-EMANUEL-1989",
  "world_node_id": "knowledge/places/places_archaeoastronomy",
  "edge_type": "resonant",
  "strength": 0.9,
  "description": "Starke persönliche Resonanz mit archäoastronomischen Orten"
}
```

## Migration und Legacy

Legacy-Crosslinks werden automatisch validiert und normalisiert:
- `BOL-RULE-004` definiert die Normalisierungsregeln
- Legacy-Link-Typen werden auf neue Typen gemappt

## Fragen?

Für Fragen zur Crosslink-Integration:
1. Prüfe `example_link.json` für ein vollständiges Beispiel
2. Konsultiere `src/tools/link_nodes.py` für automatisierte Funktionen
3. Siehe `data/modules/build_on_old/rules.json` für Transformationsregeln
