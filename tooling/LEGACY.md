# ⚠️ LEGACY DIRECTORY

## Status: DEPRECATED

This directory is marked as **LEGACY** and will be phased out gradually.

## Migration Path

All new tooling and validation scripts are now located in:
- **New Standard:** `src/`
- **Legacy (this directory):** `tooling/`

## Migrate-on-touch Strategy

Legacy files will be migrated to `src/` as they are touched:
1. New functionality → Direct implementation in `src/`
2. Legacy functionality → Ported to `src/` when needed
3. This directory → Maintained until full migration is complete

## What's in src/

### Validation
- `src/validate/validate_json.py` - Übergreifender JSON-Validator mit Legacy-Adapter
  - Validiert alle JSON-Dateien im Repository
  - Unterstützt neue Strukturen (data/) und Legacy-Strukturen
  - Includes adapter for legacy formats

### Tools
- `src/tools/add_individual.py` - Tool für Human Cartography
  - Interaktive und Batch-Modus
  - Validierung gegen humanity_potential_space.json
  - Automatische Edge-Erzeugung

- `src/tools/link_nodes.py` - Tool für Crosslinks
  - Interaktive Link-Erstellung
  - Export in JSON/CSV
  - Link-Validierung

## Migration Timeline

- ✅ Phase 1 (2026-01-22): `src/`-Verzeichnis erstellt mit neuen Scripten
- 🔄 Phase 2 (in progress): Legacy-Code wird bei Bedarf nach `src/` portiert
- ⏳ Phase 3 (future): Vollständige Migration und Entfernung von `tooling/`

## Usage

**Please use the new tools in `src/` instead:**

```bash
# Validation (NEW)
python src/validate/validate_json.py

# Add Individual (NEW)
python src/tools/add_individual.py

# Link Nodes (NEW)
python src/tools/link_nodes.py
```

## Questions?

If you need help migrating code or have questions about the new structure:
1. Check `src/README.md` for documentation
2. Review existing scripts in `src/` for examples
3. Create an issue or contact the maintainer
