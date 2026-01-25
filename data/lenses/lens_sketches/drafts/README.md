# Drafts für Lens-Skizzen

Dieser Ordner enthält Arbeitsversionen und Entwürfe für neue Lenses.

## Organisationsprinzipien

1. **Konvention vor Promotion**: Drafts werden im Hauptordner verwaltet, erst nach Abschluss in einen separaten Promotions-Ordner verschoben
2. **Versionierung**: `v1`, `v2`-Suffix für Arbeitsversionen
3. **Archivierung**: Abgeschlossene Versionen in `archived/` verschieben

## Struktur

```
drafts/
├── README.md
├── meta/                      # Meta-Pattern-spezifische Skizzen
│   ├── META-PAT-006-quiet-disruption/
│   │   ├── leise_integration_vs_loud_disruption.json
│   │   └── notes.md
├── zeitgeist/             # Zeitgeist-spezifische Skizzen
│   ├── individual/          # Individuelle Skizzen
│   └── cross_pattern/    # Cross-Pattern-Skizzen
└── templates/              # Vorlagen für neue Lenses
    ├── lens_template.md
    └── meta_pattern_template.json
```

## Benennskonventionen

### Ordner-Name
Format: `{TYP}-{TITEL}-{NUM}`
Beispiel: `leise_integration_vs_loud_disruption` (kein META-PAT-Präfix)

### Dateinamen
Format: `{LENS_NAME}-{VERSION}-{NUM}`
Beispiel: `leise_integration_vs_loud_disruption_v1`

## Workflow

1. Draft in `drafts/meta/` erstellen
2. Arbeitsschritte dokumentieren
3. Bei Abschluss (oder Abbruch) Version archivieren
4. Bei Promotion Datei in Hauptordner verschieben

## Archivierung

Abgeschlossene Versionen werden in `archived/` verschoben. Sie enthalten:
- `meta/` - Vollständige Meta-Pattern-Skizzen
- `zeitgeist/` - Vollständige Zeitgeist-Skizzen
- `individual/` - Vollständige Individuelle Skizzen
- `cross_pattern/` - Vollständige Cross-Pattern-Skizzen
- `templates/` - Vollständige Vorlagen

## Metadaten

- Erstellt: 2026-01-25
- Zweck: Organisationsstruktur für Lens-Skizzen
- Version: 1.0.0