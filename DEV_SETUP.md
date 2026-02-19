# Development Setup

## Voraussetzungen

- **Python 3.9+** (empfohlen; getestet mit Python 3.9+)
- **pip** (Python Package Manager)
- **make** (optional, aber empfohlen)

## Installation

1. Repository klonen:
   ```bash
   git clone <your-repo-url>
   cd Menschheitsged-chtniskarte
   ```

2. Python-Abhängigkeiten installieren:
   ```bash
   pip install -r requirements.txt
   ```

## Validierung

### Alle JSON-Dateien validieren:
```bash
python3 src/validate/validate_json.py --path .
# oder mit Make:
make validate
```

### JSON-Report für CI/CD:
```bash
python3 src/validate/validate_json.py --path . --json-report -
# oder mit Make:
make validate-json
```

### Self-Check für Link-Nodes:
```bash
python3 src/tools/self_check_link_nodes.py
# oder mit Make:
make self-check-link
```

## Hinweise

- Ohne `jsonschema` funktioniert die Validierung mit einem Basic-Validator (eingebauter Fallback)
- Bei Problemen: `python3 --version` prüfen
- Das validate_json.py Skript gibt bei Fehlern einen entsprechenden Status zurück (siehe `sys.exit()` im Code)