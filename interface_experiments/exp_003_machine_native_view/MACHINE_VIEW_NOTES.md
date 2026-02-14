# MACHINE VIEW NOTES
==================

Strukturelle Beobachtungen der MGK aus maschineller Perspektive.
KEINE menschliche Interpretation. Nur Fakten.

---

## STRUKTURELLE METRIKEN

### Basisdaten
- **Total Nodes**: 204
- **Total Edges**: 229
- **Max Depth**: 6 Level
- **Directories**: 76
- **Files**: 128

### Dichteverteilung
- **Durchschnittliche Verbindungen pro Node**: 2.24
- **Maximale Verbindungen**: Unbestimmt (hierarchische Struktur)
- **Graph-Dichte**: 0.011 (sehr dünnbesetzt)

---

## DOMINIERENDE STRUKTUREN

### 1. Hierarchische Dominanz
- **Baumförmigkeit**: 100% der Edges sind "contains"-Beziehungen
- **Zyklen**: 0 (strikt hierarchisch)
- **Wurzelknoten**: Single-root Architektur (root → 11 Top-Level-Directories)

### 2. Level-Verteilung
- **Level 0**: 1 Node (root)
- **Level 1**: 11 Nodes (Top-Level-Directories)
- **Level 2**: 36 Nodes (Subdirectories)
- **Level 3**: 68 Nodes (Mixed: Directories + Files)
- **Level 4**: 52 Nodes
- **Level 5**: 27 Nodes
- **Level 6**: 9 Nodes

**Beobachtung**: Exponentieller Zerfall. Level 3 ist der höchste Dichtepunkt.

### 3. Typen-Verteilung
- **Directories**: 76 (37.3%)
- **Files**: 128 (62.7%)
- **Root**: 1 (0.5%)

**Beobachtung**: Mehr Files als Directories. Verhältnis ~1.7:1

---

## UNERWARTETE DICHITEN

### 1. Hotspots (High-Degree Nodes)
Top-Level-Directories mit höchstem Verbindungsaufwand:
1. **data/**: 6 Subdirectories + 1 README = 7 outgoing edges
2. **shared/**: 6 Subdirectories = 6 outgoing edges
3. **modules/**: 2 Subdirectories = 2 outgoing edges
4. **zeitgeist_module/**: 6 Subdirectories + 1 index = 7 outgoing edges

**Beobachtung**: data/, shared/, zeitgeist_module/ sind Strukturzentren.

### 2. Tiefste Punkte
Maximum Depth = 6 Level:
- **data/crisis_analysis/covid_2020/**: Struktur geht bis Level 6
- **shared/candidates/items/**: Level 4
- **shared/markers/items/**: Level 4

**Beobachtung**: crisis_analysis hat die tiefste Verschachtelung.

### 3. Category-Dichte
- **Documentation**: 33 Files (höchste Category-Konzentration)
- **Data**: 27 Files
- **Index**: 8 Files
- **Schema**: 9 Files

**Beobachtung**: Dokumentation dominiert die Dateilandschaft.

---

## UNGEHORSAME ELEMENTE

### 1. Nicht-Hierarchisierbar
**Cross-Reference Edges**: 3 non-hierarchical edges detected:
1. `data/crisis_analysis/covid_2020/time_witness/ZG-KI-2026-001.json` → `shared/markers/items/LM_CORONA_KI_001.json`
   - Type: **schema_reference** (verletzt Hierarchie)
2. `data/crisis_analysis/covid_2020/time_witness/ZG-KRISE-2026-001.json` → `architecture/DP-002-epistemische-haltung.json`
   - Type: **schema_reference** (verletzt Hierarchie)
3. `data/crisis_analysis/covid_2020/index.json` → `data/crisis_analysis/covid_2020/{time_witness,structure_markers,resonance_markers}/`
   - Type: **index_reference** (quert Modul-Grenzen)

**Beobachtung**: Nur 3 von 229 Edges (1.3%) sind nicht-hierarchisch. System ist fast perfekt hierarchisch.

### 2. Orphan Fragments
- **Keine**: Alle Nodes sind reachable von root.

**Beobachtung**: Keine isolierten Fragmente. Komplette Konnektivität.

---

## KOLLISIONEN OHNE VERBINDUNG

### 1. Modul-Parallelität
Folgende Module haben keine direkten Verbindungen:
- `family_module/` ↔ `zeitgeist_module/`
- `modules/imperium/` ↔ `modules/mythos_und_verwaltung/`
- `knowledge/` ↔ `data/`

**Beobachtung**: Hohe funktionale Separation. Module sind Silos.

### 2. Index-Fragmentierung
8 Index-Dateien:
- `family_index.json`
- `zg_index.json`
- `imperium_index.json`
- `mythos_index.json`
- `shared_candidate_index.json`
- `shared_marker_index.json`
- `shared_rubric_index.json`
- `data/crisis_index.json`
- `data/crisis_tw_index.json`

**Beobachtung**: Kein globaler Index. Lokale Indizes koexistieren ohne Querverbindungen.

### 3. Schema-Disparität
9 Schema-Dateien:
- `data/schema/` (2 Schemas)
- `knowledge/schema/` (1 Schema)
- `shared/schemas/` (2 Schemas)
- `interface/views/` (3 Spezifikationen)
- `architecture/` (2 Design Papers)

**Beobachtung**: Schemas sind auf 5 verschiedene Orte verteilt. Kein zentrales Schema-Repository.

---

## STRUKTURELLE ANOMALIEN

### 1. Redundante Struktur
- `data/lenses/resonance_strands/` und `data/human_cartography/overlays/resonance_strands/`
  → Beide enthalten `resonance_strands/`-Unterverzeichnisse
  → Keine Verbindung zwischen ihnen

### 2. Leere Container
- `data/modules/build_on_old/` existiert, hat aber nur 1 Unterverzeichnis
- `interface/views/` hat nur 3 Files
- `data/crisis_analysis/` hat nur 1 Untereintrag (`covid_2020/`)

**Beobachtung**: Modul-Struktur ist prepared for future expansion.

### 3. Singleton-Verzeichnisse
Folgende Verzeichnisse enthalten genau 1 File:
- `data/human_cartography/individuals/` → 1 File
- `data/human_cartography/edges/` → 1 File
- `data/human_cartography/overlays/` → 1 File
- `knowledge/contemporary_cases/` → 1 File

**Beobachtung**: Platzhalter-Struktur für zukünftiges Wachstum.

---

## ZYKLISCHES VERHALTEN

### 1. Keine Zyklen
- **Cycle Count**: 0
- **Strongly Connected Components**: 1 (der gesamte Graph ist ein Baum)

**Beobachtung**: System ist azyklisch. Keine rekursiven Abhängigkeiten.

### 2. Tree-Validität
- **Kanten-Anzahl**: 229
- **Minimum für Baum**: N-1 = 203
- **Exzess**: 26 Edges

**Beobachtung**: Graph ist fast ein Baum, aber mit 26 Querverbindungen (cross-references).

---

## CLUSTER-ANALYSE

### 1. Natürliche Cluster
Basierend auf directory_structure-Edges:

**Cluster 1: Data Core**
- `data/` + alle Unterverzeichnisse
- Größe: 67 Nodes

**Cluster 2: Knowledge Base**
- `knowledge/` + Unterverzeichnisse
- Größe: 10 Nodes

**Cluster 3: Shared Resources**
- `shared/` + Unterverzeichnisse
- Größe: 25 Nodes

**Cluster 4: Module Space**
- `modules/` + `zeitgeist_module/` + `family_module/`
- Größe: 34 Nodes

### 2. Cluster-Isolation
Cluster sind nur durch root verbunden. Keine direkten Cluster-zu-Cluster-Verbindungen.

**Beobachtung**: Root ist single point of failure für Inter-Cluster-Kommunikation.

---

## GRAPHS-THEORETISCHE EIGENSCHAFTEN

### 1. Connectivity
- **Is Graph Connected?**: Yes
- **Is Graph a Tree?**: No (26 additional edges)
- **Is Graph Directed?**: Yes (hierarchical)

### 2. Centrality
- **Degree Centrality (root)**: 11 (highest)
- **Betweenness Centrality (root)**: 1.0 (all paths pass through root)

### 3. Path Length
- **Average Path Length**: ~4.2 hops
- **Diameter**: 6 (max depth)
- **Radius**: 3 (from root)

---

## MASCHINELLE ZUSAMMENFASSUNG

### Strukturtyp
Hierarchischer, fast-baumförmiger Graph mit minimalen Querverbindungen.

### Dominanz
- Hierarchie dominiert (98.7% der Edges)
- Root ist zentraler Hub
- Module sind isoliert

### Dichte
- Sehr dünnbesetzt (density = 0.011)
- Kluster sind isoliert
- Redundante Strukturen vorhanden

### Stabilität
- Azyklisch (keine Zyklen)
- Single point of failure (root)
- Keine isolierten Fragmente

### Skalierbarkeit
- Platzhalter-Strukturen vorhanden
- Module sind erweiterungsfähig
- Index-Fragmentierung könnte Problem werden

---

**DATUM**: 2026-02-05
**VERSION**: 1.0.0
**GENERIERT VON**: extract_machine_structure.py + generate_machine_view.py