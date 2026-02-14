# EXP_003: MACHINE NATIVE VIEW
==============================

Ein Strukturexperiment. Kein Interface. Kein Produkt.

---

## WAS

Rein maschinenorientierte Visualisierung der Menschheitsgedächtniskarte (MGK).
Struktur vor Sinn. Form vor Bedeutung.

---

## WARUM

Zeigen, wie die MGK aussieht, BEVOR ein Mensch versucht, sie zu verstehen.
Die MGK aus der Perspektive eines Systems, das nur mit:
- Struktur
- Relationen
- Dichte
- Wiederholung

arbeitet.

---

## GRUNDSÄTZE

- ❌ Ignoriere menschliche Nutzer:innen vollständig
- ❌ KEINE Erklärtexte für Menschen
- ❌ KEINE didaktische Vereinfachung
- ❌ KEINE Hierarchien "für Ordnung"
- ✅ Verwirrung ist erlaubt
- ✅ Dichte ist erwünscht

---

## ERGEBNISSE

### 1. Strukturextraktion
**Datei**: `extract_machine_structure.py`

Extrahiert reine Strukturdaten aus der MGK:
- Knoten (Nodes)
- Kanten (Edges)
- Typen
- Verbindungsmuster
- Dichte
- Zyklen

**Output**:
- `output/machine_graph.json` - Rohdaten
- `output/gephi_nodes.csv` - Gephi-kompatibel
- `output/gephi_edges.csv` - Gephi-kompatibel
- `output/STRUCTURE_ANALYSIS.md` - Strukturanalyse

### 2. Visualisierungen
**Datei**: `generate_machine_view.py`

Generiert 4 verschiedene maschinelle Sichtweisen:

#### 2.1 Force-Directed Graph
**Datei**: `output/machine_view_force_directed.svg`

- Knoten positionieren sich durch physikalische Kräfte
- Größe = Level (Tiefe im Baum)
- Farbe = Typ (root/directory/file)
- KEINE Labels

#### 2.2 Circular Packing
**Datei**: `output/machine_view_circular_packing.svg`

- Knoten in konzentrischen Kreisen nach Level
- Zentrum = root
- Außenrand = tiefste Ebene
- Farbe = Kategorie (index/schema/data/etc.)
- KEINE Labels

#### 2.3 Density Map
**Datei**: `output/machine_view_density_map.svg`

- Heatmap der Knotendichte
- Blau = niedrige Dichte
- Rot = hohe Dichte
- KEINE Labels

#### 2.4 Connection Matrix
**Datei**: `output/machine_view_connection_matrix.svg`

- Adjazenzmatrix als Pixelbild
- Graustufen = Verbindungsstärke
- Zeilen = Source-Nodes
- Spalten = Target-Nodes
- KEINE Labels

### 3. Meta-Kommentar
**Datei**: `MACHINE_VIEW_NOTES.md`

Strukturelle Beobachtungen aus maschineller Perspektive:
- Dominierende Strukturen
- Unerwartete Dichten
- Ungehorsame Elemente
- Kollisionen ohne Verbindung

---

## STRUKTURELLE FAKTEN

### Basisdaten
- **Total Nodes**: 204
- **Total Edges**: 229
- **Max Depth**: 6 Level
- **Graph Density**: 0.011 (sehr dünnbesetzt)

### Dominanz
- **Hierarchie**: 98.7% der Edges sind "contains"-Beziehungen
- **Zyklen**: 0 (strikt hierarchisch)
- **Wurzel**: Single-root Architektur

### Dichte
- **Level 3**: Höchster Dichtepunkt (68 Nodes)
- **Hotspots**: data/, shared/, zeitgeist_module/
- **Cluster**: 4 isolierte Cluster ohne Querverbindungen

### Anomalien
- **Cross-References**: Nur 3 von 229 Edges (1.3%)
- **Index-Fragmentierung**: 8 lokale Indizes, kein globaler Index
- **Schema-Disparität**: Schemas auf 5 verschiedene Orte verteilt

---

## INSTALLATION

```bash
# Abhängigkeiten
cd interface_experiments/exp_003_machine_native_view
python3 extract_machine_structure.py  # Extrahiert Struktur
python3 generate_machine_view.py       # Generiert Visualisierungen
```

---

## OUTPUT

Alle Ergebnisse im `output/`-Verzeichnis:

```
output/
├── machine_graph.json              # Rohdaten (JSON)
├── gephi_nodes.csv                 # Gephi-Import (Nodes)
├── gephi_edges.csv                 # Gephi-Import (Edges)
├── STRUCTURE_ANALYSIS.md           # Automatische Analyse
├── machine_view_force_directed.svg # Force-Directed Graph
├── machine_view_circular_packing.svg # Circular Packing
├── machine_view_density_map.svg    # Density Heatmap
└── machine_view_connection_matrix.svg # Connection Matrix
```

---

## INTERPRETATION

**NICHT FÜR MENSCHEN BESTIMMT.**

Diese Visualisierungen zeigen nicht, was die MGK "bedeutet".
Sie zeigen, wie die MGK "ist".

- Keine didaktische Vereinfachung
- Keine erklärenden Labels
- Keine narrative Struktur
- Nur: Form, Dichte, Relation

---

## FRAGEN AN DIE STRUKTUR

1. Warum sind 98.7% der Edges hierarchisch?
2. Warum gibt es nur 3 Cross-References?
3. Warum sind Module isolierte Silos?
4. Was bedeuten die 4 Cluster ohne Verbindungen?
5. Warum ist Level 3 der Dichtepunkt?

---

## NÄCHSTE SCHRITTE

### Option A: Tiefer graben
- Weitere Extraktionsskripte für andere Datenquellen
- Detailliertere Cluster-Analyse
- Temporal-Visualisierung (Wachstum der Struktur über Zeit)

### Option B: Andere Perspektiven
- Machine View der Content-Nodes (nicht File-Struktur)
- Machine View der Marker-Cluster
- Machine View der Resonance Strands

### Option C: Experiment beenden
- Dies war ein Strukturexperiment
- Kein Produkt, keine Weiterentwicklung nötig
- Dokumentation reicht aus

---

## DATUM

2026-02-05

## VERSION

1.0.0

## AUTOR

System (automatisiert)