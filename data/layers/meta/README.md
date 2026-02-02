# Meta-Layers

## Überblick

Meta-Layers sind entpersonalisierte Analyse-Layer, die strukturelle Muster und Deutungsformen definieren, ohne auf konkrete Personen oder Zeitzeugen zu referenzieren.

## Architekturprinzip

**Entpersonalisierung:** Meta-Layers enthalten keine konkreten Zeitzeugen-IDs oder Personennamen. Sie definieren nur Strukturen, Typen, Achsen und Protokolle.

## Verwendung

Die Zuordnung zu konkreten Zeitzeugen erfolgt ausschließlich in den individuellen Zeitzeugen-Dateien über das Feld `perspective_type`.

Beispiel:
- **Meta-Layer:** Definiert `perspective_type: "religious_reinterpretation"` mit allen Eigenschaften
- **Zeitzeuge:** Verweist auf `"perspective_type": "religious_reinterpretation"`

## Vorteile

1. **Trennung von Struktur und Instanz:** Meta-Layers sind universell wiederverwendbar
2. **Erweiterbarkeit:** Neue Perspektivtypen können hinzugefügt werden, ohne bestehende Layer zu modifizieren
3. **Konsistenz:** Alle Zeitzeugen gleichen Typs werden konsistent klassifiziert
4. **Analysemöglichkeit:** Vergleich zwischen Typen statt zwischen Individuen

## Struktur

Jeder Meta-Layer enthält:

- `layer_id`: Eindeutige Identifikation
- `perspective_types`: Liste der definierten Deutungstypen
- `comparison_axes`: Vergleichsdimensionen für Analyse
- `analysis_protocols`: Methodische Vorgehensweisen
- `integration_points`: Verknüpfungen zu anderen Layern und Modulen

## Beispiele

- **L-META-REL-DEUTUNG-001:** Religiöse Deutungsformen der Gegenwart
- **L-META-PRJ-001:** Skalierung & Projektion

## Integration

Meta-Layers verknüpfen sich mit:
- Zeitzeugen (über `perspective_type`)
- Analyse-Lenses (über `integration_points`)
- Modulen (über thematische Bezüge)