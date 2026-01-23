# Meta-Patterns Lens

Dieses Modul enthält wiederkehrende Meta-Muster, die sich über verschiedene Domains hinweg zeigen (Mythos, Geschichte, Psychologie, Soziologie).

## Konzept

Meta-Patterns sind universelle Strukturen, die in unterschiedlichen Kontexten auftauchen:
- **Hero's Cycle**: Universelles Muster des Hero's Journey
- **Civilization Resonance Loop**: Wie Kulturen ihre Vorgänger transformieren
- **Memory Resonance**: Muster kollektiver Erinnerung
- **Threshold Crossing**: Universelles Muster des Schwellenübergangs
- **Ritual Core Loop**: Grundlegende Struktur von Ritualen

Diese Patterns dienen als analytische Lenses, um:
1. Gemeinsamkeiten zwischen unterschiedlichen Phänomenen zu erkennen
2. Strukturelle Verbindungen über Domains hinweg zu identifizieren
3. Zeitgeist-Module in größere Kontexte einzubetten

## Struktur

```
meta_patterns/
├── patterns.json          # Alle Meta-Patterns
├── node_candidates.json   # Kandidaten für zukünftige Meta-Nodes
└── README.md             # Diese Datei
```

## Verwendung

### Als analytische Linse

Verwende Meta-Patterns als Linse über:
- Zeitgeist-Module (z.B. Memory Resonance auf ZG-001 anwenden)
- Historische Biografien (z.B. Hero's Cycle auf Gilgamesch)
- Rituale (z.B. Ritual Core Loop auf Übergangsrituale)
- Kulturelle Phänomene (z.B. Civilization Resonance Loop auf Renaissance)

### Pattern-Identifikation

Wenn ein Phänomen ein Meta-Pattern manifestiert:
1. Dokumentiere das Phänomen
2. Verlinke es mit dem entsprechenden Meta-Pattern
3. Analysiere Unterschiede und Besonderheiten

## Cross-References

Meta-Patterns sind untereinander verknüpft:
- **Hero's Cycle** → **Threshold Crossing** (als Phase)
- **Civilization Resonance Loop** → **Memory Resonance** (als Implementierung)
- **Ritual Core Loop** → **Threshold Crossing** (als Form)

Diese Verbindungen sind in `patterns.json` dokumentiert.

## Examples

### Example 1: Hero's Cycle in Zeitgeist-Modulen
- ZG-001 (Memory Loss) als "Call to Adventure"
- ZG-002 (Order & Powerlessness) als "Initiation"
- ZG-004 (Transition & Initiation) als "Return"

### Example 2: Memory Resonance in Orten
- Archäoastronomische Orte als Spatial Anchoring
- Familien als Intergenerational Transmission
- Rituale als Ritual Encoding

## Integration

### Mit Zeitgeist-Modulen

Meta-Patterns können als analytisches Raster für Zeitgeist-Module verwendet werden:
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

### Mit Build on Old

Build on Old analysiert, wie Meta-Patterns in materiellen und semantischen Schichten manifestieren:
```json
{
  "build_on_old_concept": "BOO_SEMANTIC",
  "meta_pattern": "META-PAT-003",
  "relationship": "Semantic Building als Manifestation von Memory Resonance"
}
```

## Node Candidates

`node_candidates.json` enthält erkannte Meta-Strukturen, die noch nicht kanonisiert sind. Diese Datei dient als Arbeitsbereich für:

### Prinzipien

1. **Vermeide frühe Kanonisierung** - Alle Strukturen bleiben zunächst Kandidaten
2. **Beobachte Wiederkehr** - Trage auf, wie oft ein Kandidat in Quellen auftaucht
3. **Tragfähigkeit prüfen** - Analyse Anschlussfähigkeit über mehrere Kontexte
4. **Explizites Gatekeeping** - Begründe, warum noch nicht kanonisiert wurde

### Struktur pro Kandidat

```json
{
  "id": "M1",
  "title": "DON'T KNOW MIND / FORSCHERHALTUNG",
  "status": "candidate",           // candidate | promoted | archived
  "confidence_signal": "sehr stark", // phänomenologische Einschätzung
  "trajectory": "wahrscheinlich zentral", // vorausschauend, unverbindlich
  "recurrence": {
    "count": 0,                   // Anzahl der Beobachtungen
    "contexts": []                 // Kontexte der Beobachtungen
  },
  "gatekeeping_reason": "Noch nicht kanonisiert, da Vergleichsdichte nötig."
}
```

### Workflow

1. **Identifikation** - Neue Struktur in `node_candidates.json` eintragen
2. **Beobachtung** - Recurrence-Count bei jeder Fundquelle erhöhen
3. **Analyse** - Connections und Sources dokumentieren
4. **Entscheidung** - Bei ausreichender Dichte:
   - `status: "promoted"` → In `patterns.json` übernehmen
   - `status: "archived"` → Als nicht tragfähig markieren

### Beispiel-Kandidaten (Stand: 2026-01-23)

- **M1: Don't Know Mind** (sehr stark, wahrscheinlich zentral)
- **M2: Unvergleichbarkeitsbehauptung** (stark, gut beobachtbar)
- **M3: Präzedenzfall-Angst** (stark, gut anschlussfähig)
- **M4: Beobachter mit Reflexionsmarkierung** (mittel-stark, wertvoll für L2)
- **M5: Sprachneuschöpfung als Legitimation** (stark, Brücke zu R3 & R4)
- **M6: Ambivalenz als Analysehaltung** (optional, evtl. Teil von M1)
- **M7: Ordnungsübergang** (beobachten, noch nicht fixieren)
- **M8: Fremdleibgarde als Machtindikator** (stark, imperienübergreifend)
- **M9: Gruppenrekursion / Soziale Fraktalität** (sehr stark, epochenübergreifend, L3)
- **M10: Moralischer Feindmarker** (sehr stark, epochenübergreifend, sensibel)
- **M11: Erosion von Machtlegitimität** (sehr stark, epochenübergreifend, Arbeitstitel)

## Schwellen-Subtypen (S-Typen)

S-Typen sind Schwellenübergänge innerhalb von Meta-Kandidaten. Sie beschreiben:
- Den exakten Moment eines qualitativen Wandels
- Ungekehrte Grenzen in Systemen
- Typische Marker und irreversible Richtungen

**Beispiel:**
- **S-Typ LEGITIMATION → REPRESSION** (M11)
  - System überschreitet die unsichtbare Grenze von Überzeugung zu reiner Kontrolle
  - Marker: Abschaltung von Zeugen, Totalanklage, eskalierende Gewalt bei sinkender Wirksamkeit
  - Richtung: Irreversibel ohne Neu-Legitimation

S-Typen werden in `node_candidates.json` unter `threshold_subtypes` geführt.

## Erweiterung

Neue Meta-Patterns können hinzugefügt werden:
1. Pattern identifizieren und dokumentieren
2. Phasen/Aspekte definieren
3. Cross-References zu anderen Patterns erstellen
4. Examples aus verschiedenen Domains sammeln

**Alternativ** für neue Strukturen:
1. Kandidat in `node_candidates.json` eintragen
2. Recurrence und Connections über Zeit aufbauen
3. Bei ausreichender Beobachtungsdichte promoten

## Fragen?

Für Fragen zur Meta-Pattern-Integration:
1. Prüfe `patterns.json` für vollständige Pattern-Definitionen
2. Prüfe `node_candidates.json` für neue Kandidaten im Beobachtungsprozess
3. Konsultiere Cross-References für Verbindungen
4. Siehe `data/modules/build_on_old/` für Integration mit Schichtungs-Analyse
