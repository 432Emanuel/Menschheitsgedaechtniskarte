# Source Directory

Dieses Verzeichnis enthält die Standard-Tooling- und Validierungs-Scripte für die Menschheitsgedächtniskarte.

## Struktur

- `validate/` - Validierungs-Scripte für JSON-Daten
- `tools/` - Hilfsscripte für Datenmanagement und Operationen

## Verhältnis zu tooling/

Das Verzeichnis `src/` ist der **neue Standard** für Tooling und Validierung.
Das Verzeichnis `tooling/` ist als **LEGACY** markiert und wird schrittweise abgelöst.

## Migration-Strategie (Migrate-on-touch)

Legacy-Dateien werden bei Berührung nach `src/` migriert:
- Neue Funktionen kommen direkt in `src/`
- Legacy-Funktionen werden bei Bedarf nach `src/` portiert
- `tooling/` bleibt bis zur vollständigen Migration erhalten

## Verwendete Technologien

- Python 3.8+
- jsonschema für JSON-Validierung
- Keine Framework-Abhängigkeiten

## Verwendung

### Validierung
```bash
python src/validate/validate_json.py
```

### Tools
```bash
python src/tools/add_individual.py
python src/tools/link_nodes.py
```

## CI/CD-Integration

Die Validator-Scripte sind für CI/CD-Pipelines optimiert:
- Exit-Codes für automatische Fehlererkennung
- Konsistente Ausgabeformate
- Support für Batch-Validierung
