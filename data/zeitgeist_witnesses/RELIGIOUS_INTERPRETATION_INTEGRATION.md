# Integration: Religiöse Deutungsformen

## Überblick

Dieses Dokument beschreibt die Integration der neuen Komponenten für die Analyse religiöser Deutungsformen in der Menschheitsgedächtniskarte.

## Neue Architekturelemente

### 1. Zeitzeugen mit Perspektiv-Typisierung

**Dateien:**
- `data/zeitgeist_witnesses/TZ-REL-RBT.json` (Robert)
- `data/zeitgeist_witnesses/TZ-REL-ELS.json` (Elias)
- `data/zeitgeist_witnesses/TZ-REL-DE-2026-002.json` (Dritter Zeitzeuge)
- `data/zeitgeist_witnesses/TZ-REL-ENGAGED-REFORM-DE-2026.json` (Kirchlich Engagierte Reformkraft)
- `data/zeitgeist_witnesses/TZ-REL-VALUES-EXIT-DE-2026.json` (Wertebasierter Austritt)

**Neues Feld:** `perspective_type`
- Definiert die Deutungsform des Zeugen
- Verweist auf Meta-Layer-Definitionen
- Ermöglicht konsistente Klassifizierung

**Perspektivtypen:**
- `religious_reinterpretation`: Religiös-kosmologische Gegenwartsdeutung (innen)
- `institutional_religion_critique`: Strukturelle Religions- und Organisationskritik (außen/kritisch)
- `value_based_outside`: Wertebasierte Außenperspektive - Werte außerhalb der Institution leben (gehen)
- `institutional_engagement_for_reform`: Kirchlich engagierte Reformperspektive - Kritisch-verbundene Haltung mit Fokus auf Reform von innen heraus
- `value_based_exit`: Wertebasierter Austritt - Austritt als Akt moralischer Kohärenz und Werte-Treue (gehen)

### 2. Meta-Layer (Entpersonalisiert)

**Datei:** `data/layers/meta/L-META-REL-DEUTUNG-001.json`

**Funktion:**
- Definiert Perspektivtypen ohne Personenreferenz
- Stellt Vergleichsachsen zur Verfügung
- Bietet Analyseprotokolle

**Architekturprinzip:** Trennung von Struktur (Meta-Layer) und Instanz (Zeitzeuge)

### 3. Meta-Agenten

**Datei:** `data/meta_agents/META-FRK-001.json`

**Kategorie:** Epistemic Trigger

**Funktion:**
- Destabilisiert Deutungsrahmen durch Fragen
- Macht implizierte Annahmen sichtbar
- Operiert auf Meta-Ebene, nicht Content-Ebene

**Unterscheidung:** Kein Zeitzeuge, weil kein eigener religiöser Standpunkt vertreten wird

### 4. Marker-System mit Klassifizierung

**Dateien:**
- `shared/markers/items/MARK-000007.json`: Geschlossene Erkenntnisschleife
- `shared/markers/items/MARK-000008.json`: Projektionscontainer
- `shared/markers/items/MARK-000009.json`: Symbolische Überfrachtung
- `shared/markers/items/MARK-000010.json`: Institutionelle Selbstkritik als Verantwortung
- `shared/markers/items/MARK-000011.json`: Prozessuale Hoffnung
- `shared/markers/items/MARK-000012.json`: Zweifel als Reifeprozess
- `shared/markers/items/MARK-000013.json`: Moralischer Austritt
- `shared/markers/items/MARK-000014.json`: Post-institutionelle Wertebindung

**Neues Feld:** `epistemic_classification`
- `category`: Art des Markers (z.B. epistemic_risk_pattern)
- `severity`: Schweregrad
- `mechanism`: Funktionsweise
- `domain`: Anwendungsbereich

**Neue Marker-Kategorien:**
- `responsibility_pattern`: Institutionelle Selbstkritik als Reformimpuls (MARK-000010)
- `hope_mechanism`: Prozessuale Hoffnung auf konkrete Reformschritte (MARK-000011)
- `doubt_mechanism`: Zweifel als integraler Bestandteil von Glaubensentwicklung (MARK-000012)
- `moral_exit_pattern`: Austritt aus institutioneller Religion als Akt moralischer Kohärenz (MARK-000013)
- `post_institutional_value_binding`: Fortführung christlicher Werte außerhalb institutioneller Strukturen (MARK-000014)

## Integrationspunkte

### Meta-Layer ↔ Zeitzeugen

```
L-META-REL-DEUTUNG-001 (definiert)
    ↓ perspective_type
TZ-REL-RBT.json / TZ-REL-ELS.json (verweisen)
```

### Marker ↔ Zeitzeugen

```
MARK-000007, MARK-000008, MARK-000009 (definieren Risiken)
    ↓ risk_markers
TZ-REL-RBT.json / TZ-REL-ELS.json (listen zutreffende Marker)
```

### Meta-Layer ↔ Analyse-Lenses

```
L-META-REL-DEUTUNG-001
    ↓ integration_points.meta_layers
L-META-PRJ-001 (Skalierung & Projektion)
```

### Meta-Agenten ↔ Kontext

```
META-FRK-001 (Frank)
    ↓ epistemic_trigger
Gespräche mit TZ-REL-RBT, TZ-REL-ELS
```

## Verwendungsszenarien

### Szenario 1: Analyse eines religiösen Zeitzeugen

1. Zeitzuge erstellen mit `perspective_type`
2. Meta-Layer für Definition konsultieren
3. Marker für Risikoidentifikation anwenden
4. Analyse-Lenses für Bewertung nutzen

### Szenario 2: Vergleich zwischen Perspektiven

1. Meta-Layer für Vergleichsachsen nutzen
2. Verschiedene Zeitzeugen gleichen Typs vergleichen
3. Marker-Analyse für Risikoprofile erstellen

### Szenario 3: Meta-Agent in Gesprächen

1. Frank als epistemischen Trigger einsetzen
2. Deutungsrahmen destabilisieren
3. Implizierte Annahmen sichtbar machen

## Epistemische Haltung

Alle Komponenten folgen dem Prinzip:

**Analyse von Form und Mechanik, nicht Bewertung von Wahrheitsgehalten**

- Marker beschreiben strukturelle Risiken, keine inhaltlichen Fehler
- Meta-Layer definieren Typologien, keine Wertungen
- Zeitzeugen werden phänomenologisch dokumentiert

## Crosslinking

### Verwandte Module

- `ZG-005-mythos-administration`: Historische Parallelen
- `modules/imperium`: Machtstrukturen
- `modules/mythos_und_verwaltung`: Institutionenanalyse

### Verwandte Marker

- `MARK-000001`: Projektionsresonanz
- `MARK-000003`: Epistemischer Reflexionsmarker

### Verwandte Lenses

- `L-META-PRJ-001`: Skalierung & Projektion
- Andere Meta-Pattern-Lenses

## Wartung und Erweiterung

### Neue Perspektivtypen hinzufügen

1. Typ in `L-META-REL-DEUTUNG-001` definieren
2. Neue Zeitzeugen mit diesem `perspective_type` erstellen

### Neue Marker hinzufügen

1. Marker-Datei in `shared/markers/items/` erstellen
2. `epistemic_classification` einfügen
3. In betroffenen Zeitzeugen referenzieren

### Neue Meta-Agenten

1. Agent in `data/meta_agents/` erstellen
2. Kategorisierung und Funktion definieren
3. README aktualisieren

## Dateistruktur

```
data/
├── zeitgeist_witnesses/
│   ├── TZ-REL-RBT.json
│   ├── TZ-REL-ELS.json
│   ├── TZ-REL-DE-2026-002.json
│   ├── TZ-REL-ENGAGED-REFORM-DE-2026.json
│   ├── TZ-REL-VALUES-EXIT-DE-2026.json
│   ├── index.json (aktualisiert)
│   └── RELIGIOUS_INTERPRETATION_INTEGRATION.md (dieses Dokument)
├── layers/
│   └── meta/
│       ├── L-META-REL-DEUTUNG-001.json
│       └── README.md
├── meta_agents/
│   ├── META-FRK-001.json
│   └── README.md
└── lenses/
    └── meta_patterns/
        └── L-META-PRJ-001.json (bereits existent)

shared/
└── markers/
    └── items/
        ├── MARK-000007.json
        ├── MARK-000008.json
        ├── MARK-000009.json
        ├── MARK-000010.json
        ├── MARK-000011.json
        ├── MARK-000012.json
        ├── MARK-000013.json
        └── MARK-000014.json
```

## Versionshinweise

- **Erstellt:** 2026-02-01
- **Status:** Aktiv
- **Architektur:** Entpersonalisiert, erweiterbar, konsistent

## Kontakt und Support

Bei Fragen zur Integration oder Erweiterung siehe:
- `data/layers/meta/README.md` (Meta-Layers)
- `data/meta_agents/README.md` (Meta-Agenten)
- `shared/markers/README.md` (Marker-System)