# Quellenarchiv / Sources Archive

## Epistemisches Prinzip

**TXT = Quelle**  
**JSON = epistemische Hülle**  
**Erkenntnis entsteht nicht hier, sondern in späteren Modulen.**

## Struktur

```
data/sources/
├── index.json              # Zentrales Register aller Quellen
├── transcripts/            # Rohtranskripte
│   ├── raw/               # Unveränderte TXT-Originale
│   │   └── SRC-TRANSCRIPT-[REGION]-[YEAR]-[NNN].txt
│   └── metadata/          # Epistemische Hüllen
│       └── SRC-TRANSCRIPT-[REGION]-[YEAR]-[NNN].meta.json
└── README.md
```

## Benennungskonvention

### Dateinamen

- **TXT-Datei:** `SRC-TRANSCRIPT-[REGION]-[YEAR]-[NNN].txt`
- **Metadaten:** `SRC-TRANSCRIPT-[REGION]-[YEAR]-[NNN].meta.json`

### Beispiel

`SRC-TRANSCRIPT-DE-2024-001.txt` + `SRC-TRANSCRIPT-DE-2024-001.meta.json`

## Metadaten-Schema

```json
{
  "id": "SRC-TRANSCRIPT-DE-2024-001",
  "title": "Titel des Transkripts",
  "date": "2024-XX-XX",
  "region": "DE",
  "source_type": "podcast|vortrag|interview|diskussion",
  "format": "txt",
  "file_path": "transcripts/raw/SRC-TRANSCRIPT-DE-2024-001.txt",
  "speakers": ["Person A", "Person B"],
  "topics": ["religion", "gesellschaft", "krise"],
  "epistemic_role": "raw_source",
  "extraction_potential": [
    "zeitzeuge",
    "marker_candidate",
    "meta_pattern_candidate"
  ],
  "notes": "Kontextuelle Beschreibung (nicht wertend)",
  "derived_nodes": [],
  "confidence_level": "unknown",
  "status": "raw|processed|integrated",
  "created_at": "2026-02-02"
}
```

## Arbeitsprinzipien

### ❌ Was wir NICHT tun

- Keine Interpretation
- Keine Bewertung
- Keine inhaltliche Glättung
- Keine direkte Umwandlung in MGK-Module

### ✅ Was wir tun

- Kontextualisieren, nicht deuten
- Potenzial markieren, nicht entscheiden
- Strukturieren, dass spätere Module anschließen können

## Anschlusslogik

Transkripte werden **nicht direkt** umgewandelt in:
- Zeitzeugen (`data/zeitgeist_witnesses/`)
- Marker (`shared/markers/`)
- Patterns oder andere Module

Sie sind **Beobachtungsmaterial**, kein Erkenntnisknoten.

Die Verknüpfung geschieht über `derived_nodes` in der Metadaten-Datei, sobald echte Ableitungen existieren.

## Leitsatz

> "Ist das hier Quelle – oder schon Erkenntnis?"  
> Wenn unklar: **Quelle behandeln.**

## Integration

1. Transkript als TXT-Datei in `transcripts/raw/` ablegen
2. Metadaten-JSON in `transcripts/metadata/` erstellen
3. Eintrag in `index.json` hinzufügen
4. Status auf `raw` setzen
5. Erst später, bei Extraktion: `derived_nodes` aktualisieren

---

Erstellt: 2026-02-02  
Version: 1.0.0