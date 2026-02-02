# Candidate Pool

Hier landen Fundstücke als **Kandidaten**, bevor sie in Module "promoted" werden.

- `items/` enthält einzelne Kandidaten-JSONs (`CAND-XXXXXX.json`)
- `candidate_index.json` ist die zentrale Liste
- Status-Workflow:
  - merkzettel → candidate → shortlisted → promoted → (optional) rejected

## Kandidaten-Typen

### `candidate_type`-Werte

- **`modul`**: Klassische Modul-Kandidaten (z.B. Urknotten-Patterns)
- **`zeitzeuge`**: Potenzielle Zeitzeugen für Phase 1
- **`knotenpunkt`**: Themen-Knotenpunkte und Brückenperspektiven (Phase 2+)

## Neue Felder

Für Zeitzeugen- und Knotenpunkt-Kandidaten:

- **`source_type`**: Art der Quelle (z.B. "video", "podcast", "artikel")
- **`speaker`**: Sprecher/Autor (wenn applicable)
- **`short_description`**: Kurze Inhaltsbeschreibung
- **`thematic_tags`**: Thematische Schlagworte
- **`potential_relevance`**: Potenzielle Relevanz für Module/Zeitzeugen
- **`phase_hint`**: Hinweis auf Einsatzphase (z.B. "Phase 2+")
- **`notes`**: Freie Notizen

## Status-Workflow Details

### merkzettel
Initiale Sammelphase. Noch keine Analyse oder Auswertung.
- Zweck: Beobachten, sammeln, reifen lassen
- Beispiel: CAND-REL-ECON-001 (Friedemann Voigt)

### candidate
Erste Sichtung erfolgt. Kandidat ist bekannt und dokumentiert.
- Übergang von merkzettel nach erster Bewertung

### shortlisted
Kandidat ist vielversprechend und wird aktiv geprüft.
- Detaillierte Analyse läuft

### promoted
Kandidat wurde in ein Modul/als Zeitzeuge überführt
- Status wird auf "rejected" gesetzt mit Verweis auf Ziel

### rejected
Kandidat wurde verworfen oder promoviert (mit Ziel-Referenz)
