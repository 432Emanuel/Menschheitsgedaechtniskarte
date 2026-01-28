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

### DP-002: Epistemische Haltung

Siehe `DP-002-epistemische-haltung.json`

Dieses Prinzip beschreibt die erkenntnistheoretische Grundhaltung des Projekts:
- **Zweck**: Definiert nicht Inhalte, sondern die Art des Umgangs mit Inhalten
- **Grundannahmen**: Vier fundamentale Annahmen über Wahrheit, subjektive Erfahrung und emergente Erkenntnis
- **Grenzen**: Was die Karte NICHT tut (bewerten, entscheiden, anweisen) und was sie stattdessen tut
- **Zielwirkung**: Anstoß innerer Prozesse statt Überzeugung
- **Krisenbezug**: Krisen als Verdichtungsräume für Wahrheitsbildungsprozesse

## DP-003 – THORUS Operating Loop

THORUS ist das Meta-Interface / Betriebssystem-Prinzip der Menschheitsgeschichtenkarte:
ein zyklischer Erkenntnis- und Wirkprozess (Loop, kein Endzustand).

- Loop-Schritte: Ich bin → Ich beobachte → Ich lerne → Ich verstehe → Ich wirke
- Shutdown/Idle (separat, nicht Teil des Loops): „Ich bin Ich“

## Beziehung zu anderen Teilen des Projekts

- **Trennung von Konzept und Daten**: Architektur-Dokumente beschreiben das "Wie", nicht das "Was"
- **Interface-Spezifikationen**: Die UI-Views in `interface/` leiten sich direkt aus DP-001 ab
- **Epistemische Konsistenz**: Alle Module, Marker und Zeitzeugenberichte unterliegen DP-002
- **Zusammenwirken von DP-001 und DP-002**: DP-001 definiert das Interface (wie Wissen dargestellt wird), DP-002 definiert die Haltung (wie mit Wissen umgegangen wird)
- **Keine direkte Verknüpfung mit Konzept_Struktur.json**: Erkenntnisarchitektur und Wissensschema bleiben sauber getrennt

## Weiterentwicklung

Neue Designprinzipien folgen dem Muster `DP-XXX-name.json` und werden hier dokumentiert.
