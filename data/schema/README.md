# Schema-Standards

Dieses Verzeichnis enthält die kanonischen Schema-Definitionen für das Menschheitsgedächtniskarte-System.

## Struktur

```
data/schema/
├── node_schema.json    # Schema für alle Nodes
├── edge_schema.json    # Schema für alle Edges
└── README.md          # Diese Datei
```

## Node Schema

`node_schema.json` definiert die Struktur aller Nodes im System:
- **Individuen**: Personen im menschlichen Netzwerk
- **Orte**: Orte, Plätze, Siedlungen
- **Konzepte**: Abstrakte Ideen, Theorien, Muster
- **Ereignisse**: Historische Ereignisse
- **Patterns**: Wiederkehrende Strukturen
- **Institutionen**: Organisationen, Institutionen
- **Dokumente**: Texte, Aufzeichnungen
- **Kandidaten**: Potentielle Einträge (Review-Status)

### Required Fields
- `id`: Eindeutiger Bezeichner (Pattern: `^[A-Z]+-[A-Z]+-[A-Z0-9-]+$`)
- `name`: Anzeigename
- `type`: Kategorie des Nodes

### Optional Fields
- `description`: Ausführliche Beschreibung
- `metadata`: Metadaten (created, modified, version, status, etc.)
- `attributes`: Typ-spezifische Attribute
- `connections`: Verbindungen zu anderen Nodes
- `tags`: Schlagworte

## Edge Schema

`edge_schema.json` definiert die Struktur aller Verbindungen:

### Required Fields
- `from`: ID des Quell-Nodes
- `to`: ID des Ziel-Nodes
- `type`: Art der Verbindung

### Edge Types
- `BUILT_UPON`: Neue Struktur baut auf älterer auf
- `REFRAMES`: Neue Bedeutung übernimmt alte Form
- `ITERATES`: Verbesserung durch Iteration
- `REFRACTS_TO`: Meta-Pattern manifestiert sich in anderem Kontext
- `INSTANCE_OF_POTENTIAL`: Individuum als Ausschnitt des Potenzialraums
- `EXPRESSES`: Individuum zeigt/lebt eine Fähigkeit
- `LEARNED_VIA`: Lernspur zu Welt/Objekt/Idee
- `ANALOGOUS_TO`: Analog zwischen verschiedenen Kontexten
- `CONTRADICTS`: Widersprüchliche Aussagen
- `INFORMS`: Informiert/ergänzt
- `INSPIRED_BY`: Inspiriert durch
- `CONNECTED_TO`: Allgemeine Verbindung
- `CAUSES`: Verursacht
- `ENABLES`: Ermöglicht
- `PRECEDES`: Geht voraus
- `FOLLOWS`: Folgt auf

### Optional Fields
- `id`: Eindeutiger Bezeichner (optional)
- `strength`: Stärke der Verbindung (0-1)
- `direction`: Richtung (directed/undirected)
- `description`: Beschreibung der Verbindung
- `metadata`: Metadaten
- `temporal_context`: Temporale Kontextinformationen
- `evidence`: Belege für die Verbindung

## Verwendung

### Validierung

JSON-Dateien können gegen die Schemata validiert werden:

```bash
# Beispiel mit ajv-cli
ajv validate -s data/schema/node_schema.json -d data/human_cartography/individuals/DE-EMANUEL-1989.json
ajv validate -s data/schema/edge_schema.json -d data/human_cartography/edges/human_world_edges.json
```

### IDE-Integration

Die Schemata können in IDEs für Autocomplete und Validierung integriert werden:

```json
{
  "$schema": "data/schema/node_schema.json"
}
```

## Versionierung

- Schema-Version wird im `$schema`-Feld definiert
- Breaking Changes: Major Version (z.B. 2.0.0)
- Non-Breaking Changes: Minor Version (z.B. 1.1.0)
- Bugfixes: Patch Version (z.B. 1.0.1)

## Migration

Für Migration von alten Schemata siehe `data/modules/build_on_old/rules.json`.

## Fragen?

Für Fragen zur Schema-Verwendung:
1. Konsultiere die jeweiligen Schema-Dateien für vollständige Definitionen
2. Prüfe `data/modules/build_on_old/rules.json` für Migrationsregeln
3. Siehe `data/README.md` für Übersicht über data/ Struktur
