# Interface-Spezifikationen

Dieses Verzeichnis enthält UI-View-Spezifikationen für die Menschheitsgedächtniskarte, die direkt aus den Architektur-Designprinzipien abgeleitet sind.

## Überblick

Die Views basieren auf der anthropologischen Erkenntnisarchitektur (DP-001) und implementieren die drei Ebenen:

- **MapView** → Körper-Ebene (räumlich verkörpert)
- **GraphView** → Geist-Ebene (strukturell vernetzt)
- **ResonancePanel** → Seele-Ebene (sinnlich resonant)

## View-Struktur

```
interface/
├── views/
│   ├── map_view_spec.json         # Körper-Ebene: Orte und Features
│   ├── graph_view_spec.json       # Geist-Ebene: Netzwerk und Beziehungen
│   └── resonance_panel_spec.json  # Seele-Ebene: Perspektiven und Resonanz
└── README.md
```

## Zielsetzung

Jede View-Spezifikation beschreibt:
1. Mapping auf Designprinzip-Komponenten
2. Integration der Epistemischen Layer (L1-L4)
3. Integration der Resonanz-Layer (R0-R5)
4. UI-Pattern und Interaktionsprinzipien
5. Visuelle Unterscheidungsmerkmale

## Beziehung zu Architektur

Alle Views leiten sich direkt von `architecture/DP-001-anthropologische-erkenntnisarchitektur.json` ab. Die Architektur definiert das "Warum", die Views definieren das "Wie" der Implementierung.

## Navigation

Die drei Views sind gleichwertige Einstiegspunkte, die miteinander verknüpft sind:
- Von MapView → GraphView (Ort → Verbindungen)
- Von MapView → ResonancePanel (Ort → Perspektive)
- Von GraphView → MapView (Netzwerk → Ort)
- Von ResonancePanel → MapView/GraphView (Perspektive → Kontext)
