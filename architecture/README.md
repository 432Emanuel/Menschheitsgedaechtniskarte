# Architektur-Dokumentation

Dieses Verzeichnis enthält Architektur- und Designprinzipien der Menschheitsgedächtniskarte.

## Zweck

Die Architektur-Dokumente definieren die konzeptionellen Grundlagen und metaphysischen Rahmenbedingungen des Projekts. Sie dienen als Meta-Rahmen für UX- und Frontend-Entscheidungen, sind aber getrennt von der fachlichen Datenstruktur (`knowledge/`, `modules/`, etc.).

## Designprinzipien

### DP-001: Anthropologische Erkenntnisarchitektur

Siehe `DP-001-anthropologische-erkenntnisarchitektur.json`

Dieses Prinzip beschreibt ein Interface, das wie menschliche Erkenntnis funktioniert:
- **Körper-Ebene**: Räumlich verkörpert (Ort) → MapView
- **Geist-Ebene**: Strukturell vernetzt (Thema) → GraphView  
- **Seele-Ebene**: Sinnlich resonant (Netzwerk) → ResonancePanel

## Beziehung zu anderen Teilen des Projekts

- **Trennung von Konzept und Daten**: Architektur-Dokumente beschreiben das "Wie", nicht das "Was"
- **Interface-Spezifikationen**: Die UI-Views in `interface/` leiten sich direkt aus DP-001 ab
- **Keine direkte Verknüpfung mit Konzept_Struktur.json**: Erkenntnisarchitektur und Wissensschema bleiben sauber getrennt

## Weiterentwicklung

Neue Designprinzipien folgen dem Muster `DP-XXX-name.json` und werden hier dokumentiert.
