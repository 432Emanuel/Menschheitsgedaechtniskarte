# Gedächtnistopologie

## Definition

Gedächtnistopologie modelliert die strukturelle Verbindung zwischen faktischen historischen Ereignissen und narrativen Verdichtungen über sogenannte Projektionsknoten.

Projektionsknoten sind keine historischen Orte, sondern **Verdichtungsstellen kollektiver Verarbeitung**, an denen reale Umbrüche in symbolische Narrative transformiert werden.

## Die drei Layer

### 1. Factual Layer (factual_events.json)

Enthält faktische historische Ereignisse mit:
- Eindeutiger Ereignis-ID
- Zeitangaben
- Geographische Region
- Ereignistyp (Naturkatastrophe, Machtwechsel, Klimabruch, etc.)
- Quellenangaben
- Sicherheitsgrad der historischen Rekonstruktion

**Wertebereich certainty_level:** `high | medium | low | unknown`

### 2. Narrative Layer (narrative_structures.json)

Enthält narrative Verdichtungen und Mythen mit:
- Eindeutiger Narrativ-ID
- Titel der Erzählung
- Kulturraum
- Entstehungszeitpunkt
- Kernmotive
- Symbolische Funktionen
- Primäre Quellen
- Narrativer Typus

### 3. Projection Nodes (projection_nodes.json)

Projektionsknoten sind Verdichtungsstellen, an denen Fakt und Narrativ über Transformationsprozesse gekoppelt werden. Sie enthalten:
- Eindeutige Knoten-ID
- Konzept/Begriff (z.B. Atlantis)
- Erste bekannte Quelle
- Projektkategorien (Verlust, Goldene Zeit, Technologie, etc.)
- Wiederkehrende Motive
- Geographische Flexibilität
- Identitätsladung
- Anmerkungen

## Transformation Links

Transformation_links beschreiben die vermutete Verarbeitungsdynamik zwischen factual_layer, narrative_layer und projection_nodes.

**Struktur:**
- Eindeutige Link-ID
- Referenz auf projection_node_id
- Referenz auf factual_event_id
- Referenz auf narrative_id
- Transformationstyp
- Verarbeitungshypothese
- Konfidenzniveau

**Wertebereich confidence_level:** `high | medium | low | speculative`

**Erlaubte transformation_type Werte:**
- `trauma_compression` - Traumakomprimierung
- `moral_parable` - Moralische Parabel
- `identity_stabilization` - Identitätsstabilisierung
- `power_legitimation` - Machlegitimation
- `memory_distortion` - Gedächtnisverzerrung
- `symbolic_elevation` - Symbolische Erhöhung
- `mythic_synthesis` - Mythische Synthese
- `speculative` - Spekulativ

## Unterschied zum Mythos-Modul

Dieses Modul ist **keine Sammlung von Mythen**. Es ist ein **Analysemodul für Transformationsdynamiken** zwischen Fakt und Narrativ.

Während das Mythos-Modul (`modules/mythos_und_verwaltung`) Mythen als kulturelle Phänomene dokumentiert, analysiert die Gedächtnistopologie **wie und warum** faktische Ereignisse in narrative Formen transformiert werden.

## Forschungshypothese

> "Projektionsknoten treten gehäuft in historischen Umbruchphasen auf und dienen als narrative Verdichtungsstellen kollektiver Verarbeitung."

Diese Hypothese wird durch das Modul systematisch überprüfbar gemacht, indem:
1. Faktische Ereignisse dokumentiert werden
2. Narrative Strukturen erfasst werden
3. Projektionsknoten als Transformationsorte identifiziert werden
4. Die Verbindungsdynamik explizit modelliert wird

## Verwendung

Das Modul ermöglicht es, Pilotfälle (z.B. Atlantis) systematisch einzupflegen und die Transformationsdynamik zwischen Fakt und Narrativ sichtbar zu machen.

**Status:** PROTOTYPE

**Version:** 0.1.0

**Letztes Update:** 2026-02-16