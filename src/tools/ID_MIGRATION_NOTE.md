# ID Migration Note

To reduce ambiguity and simplify tooling, use `id` as the canonical identifier field for new records.

Current compatibility in tooling:
- Canonical lookup order: `id` -> `node_id` -> `module_id`
- Legacy `individual_id` remains supported in `link_nodes.py` for human cartography records

Recommendation:
- New files should always include `id`
- Existing `node_id` and `module_id` can remain during transition, but plan gradual normalization to `id`
