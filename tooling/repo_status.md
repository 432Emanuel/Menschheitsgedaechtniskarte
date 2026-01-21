# Repository-Status: Menschheitsgedächtniskarte

**Stand:** 2026-01-21  
**Version:** 0.2.0

---

## 1. Modul-Übersicht

### Hauptmodule

| Modul | Status | Entity-Typen | Datensatz |
|---------|---------|---------------|------------|
| **zeitgeist_module** | 5 Module aktiv (draft) | - | Vollständige Dokumentation |
| **modules/imperium** | Struktur vorhanden | persons, empires, places, patterns, timelines, comparisons | Nur Platzhalter |
| **modules/mythos_und_verwaltung** | Struktur vorhanden | narratives, institutions, documents, patterns | Nur Platzhalter |
| **family_module** | 1 Untermodul aktiv | - | Vollständige Markdown-Dokumentation |
| **ZG-CB-contemporary-cases** | Untermodul von ZG | cases (mit Schema) | 1 echter Fall |

### Entity-Kategorien pro Modul

**zeitgeist_module:** Keine Entity-JSONs (nur Markdown-Dokumentation)

**modules/imperium:**
- entities/persons/example_person.json
- entities/empires/example_empire.json
- entities/places/example_place.json
- patterns/example_pattern.json
- timelines/example_timeline.json
- comparisons/example_comparison.json

**modules/mythos_und_verwaltung:**
- narratives/example_myth.json
- institutions/example_institution.json
- documents/example_document.json
- patterns/example_pattern.json

**family_module:**
- FM-001-family-core (vollständige Markdown-Dokumentation)
- Keine Entity-JSONs

**knowledge/places:**
- places_archaeoastronomy.json (26 Nodes, L1/L2/L3 Layers)
- candidates_archaeoastronomy.json (Platzhalter)
- Verschiedene Reports (Markdown)

---

## 2. Relationships / Crosslinks

### Vorhandene Crosslink-Systeme

1. **modules/imperium/crosslinks/links.json**
   - 1 Platzhalter-Link: Trump → Greenland
   - Status: Keine echten Beziehungen

2. **shared/crosslinks/example_link.json**
   - Nur Beispiel-Schema
   - Keine echten Links

3. **knowledge/places/places_archaeoastronomy.json**
   - Nodes haben interne `links`-Arrays
   - Beziehungstypen: supports, contradicts, informs, analogous_to, inspired_by
   - Funktionales internes Link-System

4. **zeitgeist_module/Zeitgeist_index.json**
   - site_map verbindet Module mit archäologischen Orten
   - 9 Mappings: DE-GOS-001, GB-STO-001, IE-NEW-001, TR-GOB-001, FR-CAR-001, FR-LAS-001, GB-SIL-001, IQ-URU-001, IQ-AKK-001

---

## 3. Index-Dateien: Vorhanden vs. Fehlend

### ✅ Vorhanden

- `zeitgeist_module/Zeitgeist_index.json` - Vollständig, 5 Module, 9 Site-Mappings
- `knowledge/places/places_archaeoastronomy.json` - 26 Nodes, Metadata
- `zeitgeist_module/ZG-CB-contemporary-cases/index/ZG-CB_index.json` - 1 Case
- `modules/imperium/index.json` - **NEU** - Index aller entities/strukturen
- `modules/mythos_und_verwaltung/index.json` - **NEU** - Index aller entities/strukturen
- `family_module/index.json` - **NEU** - Index des family_module

### ❌ Fehlend

- `family_module/README.md` auf module-Ebene (nur FM-001/README.md vorhanden)
- `modules/imperium/README.md` und `modules/mythos_und_verwaltung/README.md` existieren auf module-Ebene

### ⚠️ Leere Metadaten-Dateien (behoben)

- ~~`modules/imperium/meta/module_meta.json`~~ - War leer, jetzt gefüllt ✅
- ~~`modules/mythos_und_verwaltung/meta/module_meta.json`~~ - War leer, jetzt gefüllt ✅

---

## 4. Platzhalter vs. Echte Inhalte

### Platzhalter (Beispiel-Schemata)
**modules/imperium/entities/**:**
- example_person.json
- example_empire.json
- example_place.json
- example_pattern.json
- example_timeline.json
- example_comparison.json

**modules/mythos_und_verwaltung/**:**
- example_myth.json
- example_institution.json
- example_document.json
- example_pattern.json

**shared/crosslinks/**:**
- example_link.json

### Echte Inhalte

**Konzeptionell vollständig:**
- `Konzept_Struktur.json` - Vollständiges Konzept mit epistemischen und Resonanz-Layern
- `knowledge/schema/node_schema_v2.json` - Vollständiges Schema für alle Nodes
- `knowledge/layers/epistemic_layers.json` - L1-L4 definiert
- `knowledge/layers/resonance_layers.json` - R0-R5 definiert

**Datenbestände:**
- `knowledge/places/places_archaeoastronomy.json` - 26 archäoastronomische Orte
- Alle `zeitgeist_module/*` module_meta.json - 5 Module vollständig
- `zeitgeist_module/Zeitgeist_index.json` - Master-Index aller ZG-Module
- `family_module/FM-001-family-core/module_meta.json` - Vollständig
- `zeitgeist_module/ZG-CB-contemporary-cases/index/ZG-CB_index.json` - 1 echter Fall

**Zusammenfassung:**
- Knowledge- und Zeitgeist-Modulsystem sind konzeptionell fortgeschritten
- Imperium- und Mythos-Module sind Struktur-Skelette ohne echte Daten
- Family-Modul hat nur Markdown-Dokumentation
- Alle neu erstellten Index-Dateien vervollständigen die Navigation

---

## 5. Datierungs- und Versionsstatus

### Metadaten-Standards

| Datei-Typ | Version | Schema | Status |
|--------------|---------|--------|--------|
| Konzept | 0.2.0 | - | Stabil |
| node_schema_v2 | - | JSON Schema | Stabil |
| module_meta (alle) | 0.1.0 | JSON Schema | Draft |
| index (alle) | 0.1.0 | - | Draft |

---

## 6. Offene Strukturfragen

### 6.1 Crosslink-System-Integration

- Soll `modules/imperium/crosslinks/links.json` erweitert werden, um Beziehungen zwischen Imperium-Entities und anderen Modulen (z.B. zeitgeist_module) zu dokumentieren?
- Soll ein globales Crosslink-System unter `shared/crosslinks/` erstellt werden, das Modul-übergreifend funktioniert?

### 6.2 Entity-Konsistenz

- Sollen `modules/imperium/entities/` und `modules/mythos_und_verwaltung/entities/` dasselbe Schema wie `knowledge/places/places_archaeoastronomy.json` (node_schema_v2) verwenden?
- Oder haben imperiale/mythologische Entities spezifische Anforderungen, die vom allgemeinen Node-Schema abweichen?

### 6.3 Family-Modul-Entitäten

- Sollen für `family_module` Entity-JSONs erstellt werden (z.B. `family_entities.json`), oder bleibt das Modul Markdown-basiert?
- Wenn ja: Welche Entity-Typen (family, lineage, ritual, etc.)?

---

## 7. Architektur-Integrität

### Stärken

✅ **Klare Schichtung:** Epistemische Layer (L1-L4) + Resonanz-Layer (R0-R5)  
✅ **Modulare Trennung:** Zeitgeist-, Imperium-, Mythos- und Family-Module sind logisch getrennt  
✅ **Schema-Basiert:** Alle Strukturen folgen dem `node_schema_v2`  
✅ **Index-Konsistenz:** Zeitgeist- und Places-Module haben funktionierende Indices  
✅ **Meta-Struktur:** Alle Module haben (oder haben jetzt) module_meta.json mit standardisierten Feldern

### Schwächen / Lücken

⚠️ **Datenarmut:** Imperium- und Mythos-Module enthalten nur Platzhalter, keine echten historischen Daten  
⚠️ **Crosslink-Fragmentierung:** Kein globales System, verstreute Crosslink-Implementierungen  
⚠️ **Family-Entity-Lücke:** Keine Entity-JSONs im Family-Modul  
⚠️ **Meta-Dateien:** Waren leer (nun behoben)  
⚠️ **Top-Level README:** Keine zentrale Dokumentation auf module-Ebene

---

## 8. Empfehlung: Nächste 5 Schritte

### Priorität 1 (Kritisch für Daten-Integrität)

1. **Erste echte Imperium-Entity erstellen**
   - `modules/imperium/entities/persons/per_julius_caesar.json`
   - Orientierung an example_person.json, aber mit echtem historischen Bezug

2. **Erste echte Mythos-Narrative erstellen**
   - `modules/mythos_und_verwaltung/narratives/gilgamesh_epic.json`
   - Orientierung an example_myth.json, mit echtem mythologischen Inhalt

3. **Family-Entity-Schema definieren**
   - Erstelle `knowledge/schemas/family_entity_schema.json`
   - Definiere Entity-Typen für Family-Modul (family, lineage, ritual, etc.)

### Priorität 2 (Struktur-Integration)

4. **Globales Crosslink-System entwerfen**
   - Erstelle `shared/crosslinks/crosslinks_schema.json`
   - Definiere cross-module Beziehungen (z.B. imperium → zeitgeist)

5. **Erste echte Mythos-Institution erstellen**
   - `modules/mythos_und_verwaltung/institutions/temple_delphi.json`
   - Orientierung an example_institution.json, mit echtem historischem Bezug

---

## 9. Technische Metriken

| Metrik | Wert | Notiz |
|---------|-------|--------|
| Gesamtmodul | 4 | zeitgeist, imperium, mythos_und_verwaltung, family |
| Untermodul | 6 | 5 ZG-Module + 1 FM + 1 ZG-CB |
| JSON-Dateien | ~40 | Geschätzt |
| Markdown-Dateien | ~30 | Geschätzt |
| Index-Dateien | 6 | Davon 3 neu erstellt |
| Leere module_meta.json | 0 | Alle jetzt gefüllt ✅ |
| Echte Entity-Datensätze | 26 (places) + 1 (ZG-CB) = 27 | Platzhalter nicht mitgezählt |

---

**Zusammenfassung:** Das Repository hat eine solide konzeptionelle Basis mit vollständigen Schemata und klaren Layern. Die Hauptaufgabe besteht darin, echte Daten in die Struktur-Skelette (imperium, mythos_und_verwaltung) einzufügen und die Crosslink-Infrastruktur zu vereinheitlichen.
