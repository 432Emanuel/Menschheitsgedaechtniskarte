# Repo Sync Report
**Datum:** 2026-01-28
**Generator:** AI Assistant

## Zusammenfassung der Aktualisierungen

Es wurden zwei zentrale Strukturdateien synchronisiert, um den aktuellen Projektstatus abzubilden:

### 1. `chatgpt_project_overview.json`
- **Status:** Aktualisiert
- **Änderungen:**
  - Versionsnummer auf `1.1.0` erhöht.
  - Generierungsdatum auf `2026-01-28` aktualisiert.
  - Überprüfung der strukturellen Konsistenz (Verzeichnisse vs. JSON).

### 2. `repo_structure_network.json`
- **Status:** Aktualisiert
- **Änderungen:**
  - Generierungsdatum auf `2026-01-28` aktualisiert.
  - **Nodes:** Hinzufügen von 35 neuen Nodes (insb. Templates, READMEs, Candidate-Items, Marker-Items und Gephi-Projektdatei), die in der Dateistruuktur vorhanden waren, aber fehlten.
  - **Edges:** Hinzufügen von 32 neuen Verbindungen (Kanten) für die neuen Nodes (Parent-Child-Beziehungen).
  - **Groups:** Aktualisierung der Kategorisierung (insb. Templates von 2 auf 10 erhöht).
  - **Statistics:** Aktualisierung aller Zähler (Total Nodes, Files, Template Files, Config Files).

## Projektstatistiken (Stand 28.1.2026)

Die aktualisierte `repo_structure_network.json` spiegelt folgendes Volumen wider:

### Gesamtübersicht
- **Gesamt Nodes:** 204
- **Gesamt Edges:** 229
- **Maximale Verzeichnistiefe:** 6 Levels

### Dateitypen
- **Verzeichnisse:** 76
- **Dateien:** 128

### Kategorien (nach Typ)
- **Index-Dateien:** 8 (z.B. family_index.json, Zeitgeist_index.json)
- **Schema-Dateien:** 9 (z.B. node_schema.json, .schema.json)
- **Daten-Dateien:** 27 (z.B. places_archaeoastronomy.json, candidate_items)
- **Template-Dateien:** 10 (z.B. example_person.json, template_candidate.json)
- **Dokumentations-Dateien:** 33 (READMEs, Berichte)
- **Code-Dateien:** 3 (Python Skripte)
- **Konfigurations-Dateien:** 8 (.gitignore, .gephi, Konzepte)
- **Modul-Verzeichnisse:** 10 (ZG-Module, FM-Module, Imperium, etc.)

## Strukturhinweise

### 1. Neue Template-Infrastruktur
Das Projekt enthält nun eine konsistente Template-Struktur in den Modulen `modules/imperium` und `modules/mythos_und_verwaltung`:
- `entities/persons/example_person.json`
- `entities/empires/example_empire.json`
- `patterns/example_pattern.json`
- `timelines/example_timeline.json`
- `comparisons/example_comparison.json`
- `narratives/example_narrative.json` (Nicht vorhanden, aber impliziert durch Struktur)

### 2. Vollständigkeit von Shared-Ressourcen
Das `shared`-Verzeichnis ist jetzt sehr detailliert abgebildet:
- `shared/candidates/items/`: Enthält 15 Mythen-/Kandidaten-Dateien (Enumaelish bis Hiawatha).
- `shared/markers/items/`: Enthält 6 Marker-Dateien (MARK-000001 bis MARK-000006) sowie `LM_CORONA_KI_001`.
- `shared/rubrics/`: Enthält Muster-Rubriken.
- `shared/schemas/resonance_strands/`: Enthält Schema-Definitionen für Resonanzstränge.

### 3. Data-Erweiterungen
Im `data`-Bereich wurden spezifische Analysedaten und Resonanz-Stränge hinzugefügt:
- `data/human_cartography/overlays/resonance_strands/`: Individuelle Resonanz-Stränge (Overlay).
- `data/crisis_analysis/covid_2020/`: Detaillierte Strukturmarker und Zeitzeugen-Daten (raw/index).

### 4. Tooling & Visualisierung
- `visual_gephi.gephi`: Eine Gephi-Projektdatei wurde auf Root-Ebene erkannt.

## Vorschläge zur Konsistenz

### 1. Schema-Konsistenz
Beobachtung: Es wurden neue Template-Dateien (`example_*.json`) hinzugefügt.
Empfehlung: Prüfen, ob diese Templates ein gemeinsames Schema verwenden (z.B. `$schema`-Referenz in JSON), um die Validierung durch das Skript `src/validate/validate_json.py` zu ermöglichen.

### 2. Index-Pflege
Beobachtung: Die Index-Dateien (`*_index.json`) sind in der `repo_structure_network.json` korrekt als Kategorie "index" markiert.
Empfehlung: Sicherstellen, dass *alle* referenzierten Dateien in den entsprechenden Index-Dateien auch tatsächlich gelistet sind (z.B. prüfen, ob alle `CAND-*.json` in `shared/candidates/candidate_index.json` stehen).

### 3. Verzeichnis- vs. Datei-Inhalts-Konsistenz
Beobachtung: `modules/imperium/entities/` enthält nur `example_person.json`, `example_empire.json`, `example_place.json`.
Empfehlung: Wenn diese Unterverzeichnisse existieren, sollten sie entweder gefüllt oder mit `.gitkeep` markiert werden, um in der VCS-Navigation konsistent zu bleiben (sofern noch keine echten Daten vorliegen).

### 4. Tiefen-Verschachtelung
Beobachtung: Die maximale Tiefe liegt bei 6 (z.B. `data/crisis_analysis/covid_2020/time_witness/raw/.gitkeep`).
Empfehlung: Dies ist für ein akademisches Dokumentationsprojekt akzeptabel. Für eine zukünftige Visualisierung (Gephi) sollte die Layout-Engine auf diese Tiefe (Force Directed) vorbereitet sein, um "Knoten-Salate" zu vermeiden.

## Nächste Schritte

1. **Validierung:** Skript `src/validate/validate_json.py` über die gesamte Struktur laufen lassen.
2. **Visualisierung:** Import von `repo_structure_network.json` in Gephi zur Graph-Analyse.
3. **Dokumentation:** Aktualisierung der Haupt-`README.md`, falls neue Verzeichnisse (Templates, Resonance Strands) erläuterungsbedürftig sind.

---

*Ende des Berichts*