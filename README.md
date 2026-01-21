# Menschheitsgedächtniskarte

## Ein strukturelles Forschungsprojekt zur kollektiven Erinnerung der Menschheit

Die **Menschheitsgedächtniskarte** ist ein interdisziplinäres, modular aufgebautes Forschungs- und Strukturprojekt.  
Ziel ist es, wiederkehrende Muster menschlicher Erfahrung, Erinnerung, Ordnung und Sinnstiftung systematisch zu erfassen, zu vergleichen und dokumentierbar zu machen – über Zeiträume, Kulturen und Kontexte hinweg.

Im Fokus stehen dabei **keine Bewertungen**, sondern **Strukturen**, **Übergänge**, **Bruchlinien** und **Resonanzen**.

---

## Projektidee

Viele gesellschaftliche Phänomene erscheinen isoliert, zufällig oder rein zeitgebunden.  
Dieses Projekt geht von der Annahme aus, dass sich bestimmte Muster immer wieder zeigen:

- Verlust von Orientierung
- Übergangsphasen und Initiationen
- Macht- und Ohnmachtserfahrungen
- Rituale, Mythen und kollektive Narrative
- familiäre und soziale Prägungen

Die Menschheitsgedächtniskarte versucht, diese Muster **sichtbar, vergleichbar und erforschbar** zu machen.

---

## Projektstruktur

Das Repository ist modular aufgebaut:

### 🧠 Zeitgeist-Module (`zeitgeist_module`)
Zeitgenössische Muster und Phänomene, z. B.:
- Memory Loss
- Order & Powerlessness
- Ritual Relief
- Transition & Initiation
- Mythos Administration

Diese Module dienen als analytische Raster für aktuelle Fallbeispiele.

### 👨‍👩‍👧‍👦 Familienmodul (`family_module`)
Untersuchung der Rolle von Familie als:
- anthropologische Konstante
- Stabilitätsfaktor
- Bruchlinie
- Initiationsraum

Mit historischem (z. B. neolithischem) und modernem Kontext.

### 📚 Wissensschichten (`knowledge`)
Strukturierte Ebenen für:
- Orte
- kulturelle Kontexte
- semantische Schichten
- Schema-Definitionen

---

## Zeitgenössische Fallbeispiele

Ein zentrales Element sind **zeitgenössische Fallbeispiele** (Contemporary Cases), die:
- beobachtend statt wertend sind
- unterschiedliche Perspektiven offenhalten
- explizit Raum für Unsicherheit lassen

Diese Fallbeispiele können perspektivisch **international** ergänzt werden.

---

## Mitwirkung & Offenheit

Dieses Projekt ist bewusst so angelegt, dass es:
- später kollaborativ erweiterbar ist
- sowohl menschlichen Input als auch technische Auswertung zulässt
- kulturelle Perspektiven nicht vereinheitlicht

Die Menschheitsgedächtniskarte versteht sich als **offenes Forschungsgerüst**, nicht als abgeschlossenes Weltbild.

---

## Status

🟢 Strukturphase  
🟡 Inhalte im Aufbau  
🔵 Erweiterung & internationale Perspektiven geplant

---

## Technische Struktur

- `architecture/` - Architektur- und Designprinzipien (Meta-Rahmen für Interface-Entscheidungen)
- `interface/` - UI-View-Spezifikationen (MapView, GraphView, ResonancePanel)
- `modules/` - Enthält alle thematischen Module
- `knowledge/` - Wissens-Schema und Daten (epistemische Layer, Resonanz-Layer, Nodes)
- `shared/` - Gemeinsame Ressourcen (Schemas, Vokabulare, Querverweise)
- `tooling/` - Dokumentation und Hinweise für die Arbeit mit den Daten

## Architektur-Prinzip

Das Projekt basiert auf der **Anthropologischen Erkenntnisarchitektur** (DP-001):

- **Körper-Ebene** (MapView): Räumliche Verkörperung von Wissen
- **Geist-Ebene** (GraphView): Strukturelle Vernetzung von Wissen
- **Seele-Ebene** (ResonancePanel): Sinnliche Resonanz und individuelle Sinnbildung

Siehe `architecture/DP-001-anthropologische-erkenntnisarchitektur.json` für Details.

## Prinzipien

- Keine Business-Logik
- Keine Datenvalidierung oder -normalisierung
- Reine Datensammlung in JSON-Form
- Modular und erweiterbar
- Trennung von Erkenntnisarchitektur und Wissensschema

## Verwendung

Fügen Sie neue JSON-Dateien in die entsprechenden Module ein. Diese können von anderen Modulen (Analyse, Visualisierung, KI-Agenten) gelesen werden.

## Licensing

Dieses Projekt verwendet eine **Dual-Lizenz**:

- **MIT License** für Code und Software-Komponenten (.json-Dateien, Schemas, UI-Spezifikationen)
- **Creative Commons Attribution 4.0 International (CC BY 4.0)** für Dokumentation und Inhalt (.md-Dateien, Wissensmodule, historische/mythologische Inhalte)

### Lizenzdetails

- **Code-Bereich**: Freie Nutzung, Modifikation und Distribution unter MIT-Lizenzbedingungen
- **Content-Bereich**: Freies Teilen und Anpassen unter Namensnennung (Attribution)
- **Attribution**: Bei Nutzung von Content bitte "Menschheitsgedächtniskarte by Emanuel" mit Projekt-Link angeben

Vollständige Lizenzdetails siehe [LICENSE](LICENSE) Datei.

### Design & Architektur

Detaillierte Design-Prinzipien und Architektur-Dokumentation finden Sie im `/architecture/` Verzeichnis:
- Anthropologische Erkenntnisarchitektur (Körper-Geist-Seele Modell)
- UI-View-Spezifikationen für Map-, Graph- und Resonance-Views

### Neue Architektur-Dokumente

Architektur- und Interface-Dokumente folgen dem Muster:
- Designprinzipien: `architecture/DP-XXX-name.json`
- UI-Spezifikationen: `interface/views/XXX_view_spec.json`

---

# Humanity Memory Map

## A structural research project on collective human memory

The **Humanity Memory Map** is a modular, interdisciplinary research project.  
Its purpose is to identify, structure, and compare recurring patterns of human experience across time, cultures, and societal contexts.

The focus lies not on judgment or ideology, but on:
- structures
- transitions
- ruptures
- resonance patterns

---

## Concept

Many societal phenomena appear isolated or purely contemporary.  
This project is based on assumption that certain human patterns recur:

- loss of orientation
- initiation and transition phases
- power and powerlessness
- ritual and myth
- familial and social imprinting

The Humanity Memory Map aims to make these patterns **visible, comparable, and researchable**.

---

## Structure

### 🧠 Zeitgeist Modules
Analytical frameworks for contemporary phenomena.

### 👨‍👩‍👧‍👦 Family Module
Family as an anthropological constant, stabilizer, and fracture line.

### 📚 Knowledge Layers
Structured semantic and contextual layers.

---

## Contemporary Case Studies

Observed, non-judgmental case studies form a central component.  
They are designed to be expandable across cultures and regions.

---

## Collaboration

The project is designed to remain:
- open
- extensible
- culturally sensitive

It is intended as a **research framework**, not a closed narrative.

---

## Status

🟢 Structural phase  
🟡 Content development ongoing  
🔵 International expansion planned
