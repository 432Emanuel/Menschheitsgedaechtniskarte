# Imperiale Präsenz als Overlay-Pattern

## Zweck

Dieses Dokument erklärt, wie das Pattern "Imperiale Präsenz" (PAT-IMPERIAL-PRESENCE-0001) in die Gedächtnistopologie integriert wird.

## Abgrenzung

### Imperium ≠ Haupterzählung

Imperium ist in der MGK kein eigenständiger Gegenstand ("Spotlight"), sondern ein analytisches Werkzeug zur Identifikation faktischer imperialer Wirksamkeit. Es tritt nur dort auf, wo archäologische, schriftliche oder onomastische Quellen imperialer Präsenz bezeugen.

### Factual Events

Imperiale Präsenz kann als **factual_event** erfasst werden, wenn ein spezifisches Ereignis imperialer Wirksamkeit belegt ist (z.B. Gründung eines Kastells, Erlass eines Gesetzes, Münzreform).

Beispielstruktur:

```json
{
  "event_id": "GT-FAC-IMPERIAL-[LOKATION]-[JAHR]",
  "title": "Gründung des Kastells [NAME]",
  "time_range": "[ZEITRAUM]",
  "region": "[REGION]",
  "event_type": "military_foundation",
  "imperial_pattern": "PAT-IMPERIAL-PRESENCE-0001",
  "detection_axes": ["military", "roads"],
  "evidence_modes": ["archaeology", "written_sources"]
}
```

### Projection Nodes

Imperiale Präsenz kann als **projection_node** auftreten, wenn spätere narrative Projektionen auf frühere imperiale Strukturen zurückgehen (z.B. "Heiliges Römisches Reich" als Projektion auf das antike Rom).

Beispielstruktur:

```json
{
  "node_id": "GT-PROJ-IMPERIAL-[PROJEKTION]",
  "title": "[PROJEKTIONSNAME]",
  "projected_onto": "[ORIGINAL-KONTEXT]",
  "imperial_pattern_reference": "PAT-IMPERIAL-PRESENCE-0001",
  "projection_type": "symbolic_projection"
}
```

### Transformation Links

Imperiale Präsenz kann als **transformation_link** Wirksamkeit entfalten, wenn imperial Strukturen in nach-imperiale Zeit transformiert werden (z.B. die Ausbreitung des Christentums in Europa als Transformation römischer Straßeninfrastruktur).

## Anwendungshinweise

### Wann anwenden

- Bei Orten mit nachweislicher imperialer Infrastruktur
- Bei Ereignissen, die durch imperiale Verwaltung ausgelöst wurden
- Bei narrativen Projektionen, die auf imperiale Strukturen referenzieren

### Wann NICHT anwenden

- Bei rein kulturellem Austausch ohne politische Herrschaft
- Bei späterer Architektur im imperiale Stil ohne faktische Verbindung
- Bei nominellen Herrschaftsansprüchen ohne Wirksamkeit

## Integration mit anderen Modulen

- **Mythos & Verwaltung**: Imperial Overlays können Mythos-Verwaltungs-Patterns erklären
- **Zeitgeist-Module**: Imperiale Präsenz als Kontext für zeitgenössische Bruchlinien
- **Candidates**: Imperial Overlays können Kandidaten kontextualisieren

## Epistemische Haltung

Dieses Pattern folgt dem MGK-Prinzip: Keine Bewertungen, keine "Großmannssucht"-Erzählungen, keine teleologischen Imperiums-Geschichten. Imperiale Präsenz wird dort identifiziert, wo sie faktisch wirksam war – unabhängig von moralischer Bewertung.
