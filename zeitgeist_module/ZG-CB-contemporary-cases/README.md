# ZG-CB: Contemporary Cases

## Zweck des Moduls

Das **ZG-CB Contemporary Cases Modul** dient der systematischen Dokumentation und Analyse zeitgenössischer Fallbeispiele, die Auswirkungen des modernen Zeitgeists auf familiäre und soziale Strukturen zeigen.

### Kernziele

- **Perspektivoffene Dokumentation**: Fälle werden ohne moralische Urteile oder politische Bewertungen dokumentiert
- **Strukturanalyse**: Verknüpfung von zeitgenössischen Phänomenen mit den vier Strukturthemen (Ordnung/Ohnmacht, Bindung/Entbindung, Sinn/Ersatz, Gedächtnis/Vergessen)
- **Anthropologische Konstanten**: Identifikation wiederkehrender Muster in Familie, Ritual, Glaube, Übergang und Generation
- **Kulturübergreifende Vergleichbarkeit**: Struktur ermöglicht Aufnahme von Fällen aus verschiedenen Ländern und Kulturkreisen

## Abgrenzung zu anderen Zeitgeist-Modulen

### Unterschied zu ZG-001 bis ZG-005

| Aspekt | ZG-001 bis ZG-005 (Theoretische Module) | ZG-CB (Contemporary Cases) |
|--------|-----------------------------------------|-----------------------------|
| **Fokus** | Theoretische Konzepte und historische Muster | Konkrete zeitgenössische Fallbeispiele |
| **Material** | Historische Orte, anthropologische Studien | Interviews, Medienereignisse, Alltagsbeobachtungen |
| **Zeitebene** | Prähistorisch bis antike Moderne | Aktuelle Zeitgenossenschaft (21. Jahrhundert) |
| **Status** | Konzeptuelle Rahmenwerke | Empirische Beobachtungen |

### Beziehung zu Family-Modul (FM)

- **FM-001-family-core**: Theoretische Grundlagen zu familiären Resilienzvektoren
- **ZG-CB**: Konkrete Fallbeispiele, die familiäre Bruchlinien in der Praxis zeigen

### Verknüpfungsprinzip

Jeder Contemporary Case sollte mit mindestens einem theoretischen Modul verknüpft werden:
- ZG-002-order-powerlessness: Ohnmachtserfahrungen und Institutionen
- FM-001-family-core: Familiäre Resilienz und Bruchmuster
- ZG-003-ritual-relief: Ritualerfahrungen und Entlastung
- ZG-004-transition-initiation: Übergänge ohne kollektive Rituale
- ZG-005-mythos-administration: Mythenbildung und administrative Strukturen

## Struktur des Moduls

```
zeitgeist_module/ZG-CB-contemporary-cases/
├── schema/
│   ├── ZG-CB_case.schema.json        # JSON-Schema mit Validierung
│   └── ZG-CB_case.example.json       # Neutrales Beispiel ohne Wertungen
├── index/
│   └── ZG-CB_index.json             # Skalierbarer Länder-Index
├── cases/
│   ├── DE/                          # Länderordner (ISO-3166-1 Alpha-2)
│   │   ├── ZG-CB-DE-YYYY-NN.json   # Maschinenlesbare Fallbeschreibung
│   │   └── ZG-CB-DE-YYYY-NN.md     # Menschlich lesbare Fallbeschreibung
│   └── _INSTRUCTIONS.md             # Detaillierte Anweisungen
├── ZG-CB_template.md                # Markdown-Template für Fälle
├── ZG-CB_guidelines.md              # Guidelines für menschliche Mitwirkende
└── README.md                        # Diese Datei
```

## Status-System

Jeder Fall durchläuft vier Status:

1. **raw**: Rohmaterial, noch nicht reflektiert
2. **reflected**: Reflektiert und strukturiert
3. **comparable**: Für Vergleiche geeignet
4. **archived**: Archiviert, nicht mehr aktiv

## Hinweise für menschliche Mitwirkende

### Dokumentationsprinzipien

1. **Perspektivoffenheit**: Keine endgültigen Interpretationen. Multiple Perspektiven erfassen.
2. **Deskriptivität**: Beschreiben statt bewerten. Fakten vor Interpretationen.
3. **Neutralität**: Keine politischen, religiösen oder weltanschaulichen Urteile.
4. **Kontextsensibilität**: Kulturspezifische Kontexte beachten und dokumentieren.

### Verbotene Elemente

- ❌ Moralische Urteile
- ❌ Politische Stellungnahmen
- ❌ Identifikation realer Personen ohne Einwilligung
- ❌ Narrative festschreiben
- ❌ Absolute Wahrheitsansprüche

### Erlaubte Elemente

- ✅ Deskriptive Beobachtungen
- ✅ Multiple Perspektiven
- ✅ Offene Fragen
- ✅ Kulturspezifische Kontexte
- ✅ Alternative Deutungsmöglichkeiten

### Arbeitsablauf

1. **Quelle auswählen**: Interview, Medienereignis, Alltagsbeobachtung etc.
2. **Rohdaten sammeln**: Notizen, Transkripte, Materialien
3. **JSON strukturieren**: Ausfüllen nach Schema (ZG-CB_case.schema.json)
4. **Markdown ergänzen**: Menschlich lesbare Beschreibung (ZG-CB_template.md)
5. **Index aktualisieren**: Fall in ZG-CB_index.json eintragen
6. **Prüfen**: Schema-Validierung und Neutralitätsprüfung

### Felder für zukünftige Forschung

Folgende Felder sind explizit offen für zukünftige Forschung:

- `anthropological_constants`: Verknüpfungen zu anthropologischen Konstanten
- `perspective_openness`: Alternative Interpretationen und kulturspezifische Notizen
- `culture_specific_notes`: Kontexte für andere Länder und Kulturkreise

## Erweiterbarkeit

### Neue Länder hinzufügen

1. Ordnerstruktur anlegen: `cases/[ISO-CODE]/`
2. Fall nach Schema erstellen
3. Index aktualisieren: `index/ZG-CB_index.json`

### Neue Kontexttypen

Das Schema unterstützt folgende Kontexttypen:
- `interview`: Interviews oder Befragungen
- `everyday_observation`: Alltagsbeobachtungen
- `media_event`: Medienereignisse
- `personal_account`: Persönliche Erzählungen
- `institutional_event`: Institutionelle Ereignisse
- `other`: Andere Kontexte

## Referenzen

- **Schema**: `schema/ZG-CB_case.schema.json`
- **Beispiel**: `schema/ZG-CB_case.example.json`
- **Template**: `ZG-CB_template.md`
- **Guidelines**: `ZG-CB_guidelines.md`
- **Index**: `index/ZG-CB_index.json`

## Kontakt und Beiträge

Für Fragen oder Beiträge wenden Sie sich bitte an die Projektverwaltung.

---

*Zuletzt aktualisiert: 2026-01-21*
*Version: 0.2*
