# Meta-Patterns Lens

Dieses Modul enthält wiederkehrende Meta-Muster, die sich über verschiedene Domains hinweg zeigen (Mythos, Geschichte, Psychologie, Soziologie).

## Konzept

Meta-Patterns sind universelle Strukturen, die sich in unterschiedlichen Kontexten manifestieren:
- **Hero's Cycle**: Universelles Muster des Hero's Journey
- **Civilization Resonance Loop**: Wie Kulturen ihre Vorgänger transformieren
- **Memory Resonance**: Muster kollektiver Erinnerung über Generationen
- **Threshold Crossing**: Universelles Muster des Schwellenübergangs
- **Ritual Core Loop**: Grundlegende Struktur von Ritualen
- **Leise Integration vs. laute Disruption**: Unterschiede zwischen lautem Auftritt und leiser Integration

## Verwendung als analytisches Werkzeug

### Analyse-Indikation
Eine Pattern-Lense strukturiert, welche Aspekte eines Phänomens relevant sind:
- **Achsen**: Unterschiedliche Dimensionen (z.B. laut/leise, kurzlebig/dauerhaft)
- **Indikatoren**: Konkrete Beobachtungszeichen (z.B. Schlagzeilen-Dichte, Feature-by-Feature-Integration)
- **Mechanismen**: Erklärungsmodelle für das Funktionieren der Lense

### Vergleichs-Optionale
Verschiedene Lenses können auf denselben Phänomen angewandt werden:
- Hero's Cycle vs. Ritual Core Loop (beide Ritual-Strukturen)
- Memory Resonance vs. Threshold Crossing (beide Übergangsphasen)

### Dokumentations-Vorlage
Strukturierte Erfassung von Beobachtungen und Indikatoren:
- Systematische Kategorisierung
- Operationalisierbarkeit der Indikatoren
- Verknüpfung mit verwandten Elementen

### Als Tool-Referenz
Andere Werkzeuge können über `links.suggested_tools` auf Pattern Lenses verweisen:
- Kohärente Analyse über verschiedene Werkzeuge hinweg
- Wiederverwendung strukturierter Kategorien und Indikatoren

### Als Wissensbasis
Die Lenses dokumentieren beobachtete Muster und Mechanismen:
- Manuelle Analyse
- Schulungszwecke
- Qualitative Forschung

## Struktur

```
meta_patterns/
├── patterns.json          # Alle Meta-Patterns
├── node_candidates.json   # Kandidaten für zukünftige Meta-Nodes
└── README.md             # Diese Datei
```

## Pattern-Identifikation

Wenn ein Phänomen ein Meta-Pattern manifestiert:
1. Dokumentiere das Phänomen
2. Verlinke es mit dem entsprechenden Meta-Pattern
3. Analysiere Unterschiede und Besonderheiten
4. Dokumentiere Beispiele und Gegenbeispiele

## Cross-References

Meta-Patterns sind untereinander verknüpft:
- **Hero's Cycle** → **Threshold Crossing** (als Phase)
- **Civilization Resonance Loop** → **Memory Resonance** (als Implementierung)
- **Ritual Core Loop** → **Threshold Crossing** (als Form)

Diese Verbindungen sind in `patterns.json` dokumentiert.

## Examples

### Example 1: Hero's Cycle in Zeitgeist-Modulen
- **ZG-001 (Memory Loss)** als "Call to Adventure"
- **ZG-002 (Order & Powerlessness)** als "Initiation"
- **ZG-004 (Transition & Initiation)** als "Return"

### Example 2: Memory Resonance in Orten
- **Archäoastronomische Orte** als Spatial Anchoring
- **Familien** als Intergenerational Transmission

## Integration mit Resonance Strands

Pattern Lenses können mit Resonance Strands verknüpft werden über `links.suggested_overlays`:
- Detaillierte individuelle Resonanzen
- Systematische Erfassung von Resonanzmustern
- Integration anthropologischer Muster in persönliche Resonanzprofile

## Integration mit Zeitgeist-Modulen

Meta-Patterns dienen als analytische Raster für Zeitgeist-Module:
```json
{
  "zeitgeist_module": "ZG-001-memory-loss",
  "meta_pattern": "META-PAT-003",
  "mapping": {
    "phase": "Spatial Anchoring",
    "manifestation": "Archäoastronomische Orte als Erinnerungsorte"
  }
}
```

## Integration mit Build on Old

Build on Old analysiert, wie Meta-Patterns in materiellen und semantischen Schichten manifestiert:
```json
{
  "build_on_old_concept": "BOO_SEMANTIC",
  "meta_pattern": "META-PAT-003",
  "relationship": "Semantic Building als Manifestation von Memory Resonance"
}
```

## Tool-Referenz

Die konzeptionelle Dokumentation zu Pattern Lenses als analytisches Werkzeug:
- `src/tools/pattern_lenses/README.md` - Nutzung und Best Practices

## Schwellen-Subtypen (S-Typen)

S-Typen beschreiben Schwellenübergänge innerhalb von Meta-Kandidaten:
- **S-TYP LEGITIMATION** → REPRESSION (System überschreibt die Grenze)
- **S-TYP HERO'S ASCENSION** → TRANSFORMATION (Erhöhung, neue Ebene)
- **S-TYP COLLAPSE** → FRAGMENTATION (Zerfall der Ordnung)

Diese S-Typen werden in `node_candidates.json` unter `threshold_subtypes` dokumentiert.

## Weiterentwicklung

### Mögliche Erweiterungen
- Quantifizierung: Numerische Indikatoren statt qualitativer Beschreibungen
- Visualisierung: Grafische Darstellung der Achsen
- Filter-Möglichkeiten: Nach bestimmten Kategorien filtern
- Export-Formate: CSV, Markdown für Weiterverarbeitung

### Best Practices
- Kategorien klar und trennscharf definieren
- Indikatoren operationalisierbar gestalten
- Beispiele aus verschiedenen Domains aufnehmen
- Gegenbeispiele nicht vergessen (brechen die Heuristik)

## Verweise

- [Meta-Patterns Index](../meta_patterns/patterns.json)
- [Resonance Strands System](../../human_cartography/overlays/resonance_strands/)
- [Pattern Lenses Dokumentation](../src/tools/pattern_lenses/README.md)
- [Node Candidates](./node_candidates.json)
- [Methoden-Werkzeuge](../../)

## Metadaten

- Erstellt: 2026-01-22
- Letzte Aktualisierung: 2026-01-25
- Zweck: Dokumentation der Meta-Patterns als analytisches Werkzeug
- Version: 1.0.0