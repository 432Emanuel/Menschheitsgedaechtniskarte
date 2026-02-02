# Zeitzeugenberichte - KI und digitaler Wandel

Dieses Verzeichnis enthält Zeitzeugenberichte zu KI-relevanten Themen, die aus Podcast-Transkripten extrahiert wurden.

## Struktur

```
data/zeitgeist_witnesses/
├── README.md                           # Diese Datei
├── index.json                          # Index aller Berichte
├── ZG-KI-2026-001.json                 # Vollständiger Podcast-Transkript-Bericht
├── ZG-KI-2026-002.json bis 008.json    # Extrahierte Einzelberichte
```

## Quelle

- **Primärquelle**: Podcast "Engel & Dämonen - Home Office #616"
- **Upload-Methode**: TurboScribe transcript upload
- **Sprache**: Deutsch
- **Extraktionsfokus**: KI-relevante Aussagen (Algorithmus, Aufmerksamkeit, Bildung, Kompetenzverschiebung, Technikambivalenz)

## Sprecher

- **Robert**: Host/Co-Host (pragmatisch, technikrelativierend, zeitgeist-orientiert)
- **Frank**: Host/Co-Host (kritisch, bildungsskeptisch, aufmerksamkeitskritisch)
- **Elias Sasek**: Guest (christlich/OCG-nahe, verantwortungsethisch, skeptisch gegen Entfremdung)

## Position-Cluster

Die Berichte sind 5 thematischen Clustern zugeordnet:

1. **LENS_ALGO_ATTENTION_001** - KI/Algorithmus als Aufmerksamkeitslenker
2. **LENS_VIRTUAL_INSTINCT_001** - Virtualisierung → Realitätsentkopplung / Instinktverlust
3. **LENS_EDUCATION_OBSOLESCENCE_001** - KI/Roboter → Bildungs-Obsoleszenz
4. **LENS_TOOL_NEUTRALITY_001** - KI/Digitales als neutrales Werkzeug
5. **LENS_TECH_AMBIVALENCE_001** - Technikfaszination + Kritik

## Verknüpfungen

- **Source-Node**: `data/sources/podcast_transcripts/engel_daemonen_home_office_616_source.json`
- **Pattern-Lenses**: `data/lenses/zeitgeist_patterns/`
- **Crosslinks**: `zeitgeist_module/ZG-CB-contemporary-cases/`

## Epistemischer Status

Die Berichte verwenden verschiedene epistemische Status-Marker:
- `first_person_experience`: Direkte Selbsterfahrung
- `reported_claim`: Berichtete Aussagen von Experten/Dritten
- `interpretive_claim`: Interpretative Schlussfolgerungen
- `analyst_note`: Meta-Beobachtungen des Analysten

## Multiperspektivität

Die Sammlung bewahrt die Pluralität der Positionen - opposing views werden nicht zusammengeführt, sondern als separate Zeitzeugenberichte geführt (z.B. Defizit-These vs. Kompetenzverschiebungs-These).

## Pflege und Erweiterung

Neue Zeitzeugenberichte sollten:
1. Das gleiche Schema verwenden
2. Eindeutige cluster_lenses zuordnen
3. Epistemischen Status angeben
4. Crosslink-Vorschläge enthalten
5. Im Index (`index.json`) eingetragen werden

## Stand

- **Erstellt**: 2026-02-01
- **Anzahl Berichte**: 8 (1 Volltext, 7 Extrakte)
- **Status**: Active