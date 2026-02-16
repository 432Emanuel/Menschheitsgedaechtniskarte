# Gedächtnistopologie

## Definition

Gedächtnistopologie untersucht die **strukturellen Rückkopplungen** zwischen realen historischen Brüchen (faktischer Layer) und narrativen Verdichtungen (narrativer Layer).

Projektionsknoten sind **Verdichtungsstellen**, an denen reale Umbrüche symbolisch transformiert, reguliert oder identitätsstabilisierend verarbeitet werden.

**WICHTIG:** Gedächtnistopologie ist kein Mythensammler. Es ist ein **Forschungsinstrument zur Analyse der Rückkopplung zwischen faktischer Ebene und narrativer Ebene**.

---

## KERNHYPOTHESE

> **Narrative Verdichtungen entstehen gehäuft in historischen Umbruchphasen und dienen der kollektiven Selbstregulation.**

Langfristiges Ziel: Transparenz der Dynamik zwischen Fakt und Narrativ zur Förderung von Differenzierung und Konfliktlösung durch Erkenntnis.

---

## Zwei Ebenen + Dynamik

### 1. Faktischer Layer (factual_events.json)

Enthält historisch rekonstruierbare Ereignisse:
- Ereignisse, Brüche, Transformationen
- Mit Quellenbeleg und Zeit-Raum-Verortung
- Certainty-Level explizit ausweisbar

**Wertebereich certainty_level:** `high | medium | low | unknown`

### 2. Narrativer Layer (narrative_structures.json)

Enthält kulturelle Verdichtungsformen:
- Mythen, Legenden, symbolische Deutungen
- Kernmotive und symbolische Funktionen
- Kulturräume und Emergenzzeiten

### 3. Die Analyse-Dynamik

Gedächtnistopologie analysiert die **Transformationsdynamik** zwischen diesen Ebenen.

---

## Funktion von Narrativen

Narrative werden nicht als wahr oder falsch klassifiziert, sondern als **regulatorische Strukturen** verstanden.

### Transformationsfunktionen

Das Modul untersucht folgende Transformationsmechanismen:

| Funktion | Beschreibung |
|----------|--------------|
| `trauma_compression` | Katastrophale Ereignisse werden in verdichtete Symbolik transformiert |
| `moral_parable` | Historische Ereignisse werden zu moralischen Lehrgeschichten umgeformt |
| `identity_stabilization` | Ereignisse werden zur Selbstvergewisserung einer Gruppe narrativiert |
| `power_legitimation` | Machtverhältnisse werden durch mythische Erzählungen gerechtfertigt |
| `symbolic_elevation` | Profane Ereignisse werden in sakralisierte Symbolik transformiert |
| `mythic_synthesis` | Mehrere faktische Ereignisse werden zu einer mythischen Erzählung verschmolzen |
| `memory_distortion` | Ungünstige Fakten werden durch narrativ günstigere Versionen ersetzt |

**Wertebereich confidence_level:** `high | medium | low | speculative`

---

## WICHTIGE Unterscheidung

### Was das Modul dient zu:

- ✓ Fakt und Narrativ unterscheidbar zu machen
- ✓ Ihre Wechselwirkung sichtbar zu machen
- ✓ Projektionen als solche erkennbar zu machen
- ✓ Transformationsdynamiken analysierbar zu machen

### Was das Modul NICHT dient zu:

- ✗ Mythen zu widerlegen
- ✗ Wahrheitsansprüche zu bewerten
- ✗ Alternative Geschichtsthesen zu beweisen
- ✗ Narrative als "falsch" zu entlarven

---

## Struktur des Moduls

### Projection Nodes (projection_nodes.json)

Projektionsknoten sind Verdichtungsstellen, an denen Fakt und Narrativ gekoppelt werden:

- Eindeutige Knoten-ID
- Konzept/Begriff (z.B. Atlantis)
- Erste bekannte Quelle
- Projektkategorien (Verlust, Goldene Zeit, Technologie, etc.)
- Wiederkehrende Motive
- Geographische Flexibilität
- Identitätsladung
- Anmerkungen

### Transformation Links (transformation_links.json)

Beschreiben die vermutete Verarbeitungsdynamik zwischen den Layern:

- Eindeutige Link-ID
- Referenz auf projection_node_id
- Referenz auf factual_event_id
- Referenz auf narrative_id
- Transformationstyp
- Verarbeitungshypothese
- Konfidenzniveau

---

## Forschungsausrichtung

### Phase 1: Forschungsinstrument

Das Modul dient primär als **Forschungsinstrument zur Modellierung kollektiver Selbstregulationsprozesse**.

Es ermöglicht:
- Systematisches Tracking von Ereignis-Narrativ-Paaren
- Longitudinalanalyse von Projektionsknoten-Dichten
- Cross-cultural comparison von Transformationsmustern

### Langfristige Perspektive: Bewusstseinswerkzeug

**Erkenntnisbasierte Differenzierung als Beitrag zur Konfliktlösung**

Durch die strukturelle Analyse der Dynamik zwischen Fakt und Narrativ soll:
- Die Unterscheidbarkeit von Fakt und Projektion geschärft werden
- Die regulatorischen Funktionen von Narrativen transparent werden
- Ein Beitrag zur Konfliktlösung durch Differenzierung geleistet werden

---

## Abgrenzung zu anderen Modulen

### vs. Mythos-Modul (`modules/mythos_und_verwaltung`)

- **Mythos-Modul:** Dokumentiert Mythen als kulturelle Phänomene
- **Gedächtnistopologie:** Analysiert die Transformationsdynamik zwischen Fakt und Narrativ

### vs. Krisenanalyse (`data/crisis_analysis/`)

- **Krisenanalyse:** Identifiziert pre-disruptive tension periods
- **Gedächtnistopologie:** Untersucht, wie diese Phasen narrative Verdichtungen erzeugen

---

## Verwendung

Das Modul ermöglicht es, Pilotfälle (z.B. Atlantis) systematisch einzupflegen und die Transformationsdynamik zwischen Fakt und Narrativ sichtbar zu machen.

**Architektur-Referenz:** `architecture/DP-006-gedaechtnistopologie.json`

---

**Status:** PROTOTYPE

**Version:** 0.2.0

**Letztes Update:** 2026-02-16