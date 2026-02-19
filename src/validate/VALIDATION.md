# Schema Routing Guide

## Overview

The JSON validation system uses **explicit schema routing** to validate JSON files against their appropriate schemas. This guide explains how routing works and how to add new routing rules.

## How Schema Routing Works

When `validate_json.py` runs, it determines which schema to use for each file in this order:

### 1. Forced Schema (`--schema` CLI flag)
Overrides all other routing mechanisms. Useful for testing specific schemas.

```bash
python3 src/validate/validate_json.py --schema standard_node --path modules/imperium/
```

### 2. Routing Config (`schema_routing.json`)
Uses glob patterns to match file paths to external schema files. The **most specific pattern wins** (longest glob pattern).

Example from `src/validate/schema_routing.json`:
```json
{
  "glob": "modules/narrative_ecology/analysis/*.json",
  "schema": "modules/narrative_ecology/schema/narrative_node.schema.json",
  "comment": "Narrative ecology analysis files"
}
```

**Features:**
- ✅ **Glob patterns**: `*.json`, `**/*.json` (recursive), `path/to/*.json`
- ✅ **External schemas**: Schema files loaded from anywhere in the repo
- ✅ **Schema caching**: Schemas loaded once and reused for performance
- ✅ **Validation**: Warns if schema file doesn't exist

**Path resolution note:**
- Routing config path (`--routing-config`) and schema paths inside it are resolved relative to the repository root.
- Glob matching is done against repo-root-relative file paths.
- `--path` only controls scan scope (which files are traversed), not routing base resolution.

### 3. Hardcoded Fallback
Minimal fallback for backward compatibility with existing built-in schemas:
- `data/human_cartography/individuals/` → `human_cartography_individual`
- `data/modules/build_on_old/` → `build_on_old`

### 4. No Match
If no rule matches, the file is marked as `schema_missing` with reason "no schema mapping rule".

## Adding New Routing Rules

### Step 1: Create a Schema File

Create a JSON schema file in your module directory:

```bash
modules/my_module/schema/
├── my_entity.schema.json
└── my_relation.schema.json
```

Example schema (`my_entity.schema.json`):
```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "required": ["id", "name"],
  "properties": {
    "id": {"type": "string"},
    "name": {"type": "string"},
    "description": {"type": "string"}
  }
}
```

### Step 2: Add Routing Rule

Edit `src/validate/schema_routing.json`:

```json
{
  "version": "1.0",
  "rules": [
    {
      "glob": "modules/my_module/entities/**/*.json",
      "schema": "modules/my_module/schema/my_entity.schema.json",
      "comment": "My module entities (recursive)"
    },
    {
      "glob": "modules/my_module/relations/*.json",
      "schema": "modules/my_module/schema/my_relation.schema.json",
      "comment": "My module relations"
    }
  ]
}
```

### Step 3: Test

Validate your module:

```bash
python3 src/validate/validate_json.py --path modules/my_module/
```

## Debugging

### View All Schema Mismatches
```bash
python3 src/validate/validate_json.py --json-report - | jq '.schema_missing'
```

### Validate Single File
```bash
python3 src/validate/validate_json.py --path modules/my_module/entities/item.json
```

### Test Specific Schema
```bash
python3 src/validate/validate_json.py \
  --schema standard_node \
  --path knowledge/places/
```

### Custom Routing Config
```bash
python3 src/validate/validate_json.py \
  --routing-config custom_routing.json \
  --path .
```

## Glob Pattern Examples

| Pattern | Matches | Does Not Match |
|---------|---------|----------------|
| `*.json` | `file.json` | `dir/file.json` |
| `path/*.json` | `path/file.json` | `other/file.json`, `path/sub/file.json` |
| `path/**/*.json` | `path/file.json`, `path/sub/file.json`, `path/sub/deep/file.json` | `other/file.json` |
| `**/items/*.json` | `items/file.json`, `sub/items/file.json` | `other/file.json` |

**Tip:** Use `**/*.json` for recursive matching through subdirectories.

## Routing Resolution

When multiple rules match a file, the **longest glob pattern wins**:

```json
{
  "rules": [
    {
      "glob": "modules/**/*.json",  // Length: 18
      "schema": "generic.schema.json"
    },
    {
      "glob": "modules/narrative_ecology/**/*.json",  // Length: 42 - WINS!
      "schema": "narrative.schema.json"
    }
  ]
}
```

File `modules/narrative_ecology/analysis/file.json` matches both rules → uses `narrative.schema.json` (longer pattern).

## Performance

- **Schema caching**: Schemas loaded once and cached in memory
- **Fast glob matching**: Uses Python's `fnmatch` module
- **Early exit**: Stops at first matching rule

## Validation Metrics

After running `validate_json.py`, check the summary:

```
Validation Summary
==================
total_files_scanned: 310
parsed_ok: 310
syntax_errors: 0
schema_valid: 48
schema_invalid: 2
schema_missing: 260
```

- `schema_valid`: Files that pass validation
- `schema_invalid`: Files that fail validation (check `schema_invalid` list)
- `schema_missing`: Files without routing rule (informational, not an error)

## Troubleshooting

### Schema file not found warning
```
Warning: Schema file not found for rule 'modules/**/*.json': modules/schema/my.schema.json
```

**Solution:** Create the schema file or fix the path in `schema_routing.json`.

### All files show `schema_missing`
**Cause:** `schema_routing.json` not found or empty routing config.

**Solution:** 
1. Check file exists: `ls src/validate/schema_routing.json`
2. Verify default path: `--routing-config src/validate/schema_routing.json`
3. If scanning a subfolder (for example `--path modules/narrative_ecology/analysis/`), routing still uses repo-root-relative globs.

### Rule doesn't match
**Cause:** Incorrect glob pattern or path mismatch.

**Solution:**
1. Use `python3` to test glob pattern:
   ```python
   import fnmatch
   fnmatch.fnmatch("modules/narrative_ecology/analysis/file.json", "modules/narrative_ecology/**/*.json")
   ```
2. Check path uses forward slashes: `path/to/file.json` (not `path\to\file.json`)

## Advanced: Multiple Schemas per Module

If your module has multiple entity types, create separate rules:

```json
{
  "glob": "modules/my_module/nodes/*.json",
  "schema": "modules/my_module/schema/node.schema.json",
  "comment": "Node entities"
},
{
  "glob": "modules/my_module/edges/*.json",
  "schema": "modules/my_module/schema/edge.schema.json",
  "comment": "Edge entities"
},
{
  "glob": "modules/my_module/metadata/*.json",
  "schema": "modules/my_module/schema/metadata.schema.json",
  "comment": "Metadata files"
}
```

## Best Practices

1. **Use specific patterns**: Prefer `modules/my_module/entities/*.json` over `**/*.json`
2. **Document rules**: Always include `comment` field explaining what files match
3. **Organize schemas**: Keep schema files next to the data they validate
4. **Test incrementally**: Add rules one at a time and validate
5. **Check output**: Run validation and review `schema_missing` list

## References

- **JSON Schema spec**: https://json-schema.org/
- **fnmatch docs**: https://docs.python.org/3/library/fnmatch.html
- **validator source**: `src/validate/validate_json.py`
