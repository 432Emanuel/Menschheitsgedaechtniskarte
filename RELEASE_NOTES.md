# Release Notes / Entwicklertagebuch

---

## v0.3-alpha

*Stand: 28.1.2026*

### Zusammenfassung

**Erkennt Projektionsschleifen, entschärft Zuschreibungsangst, erlaubt Mehrdeutigkeit ohne Kontrollverlust, Humor-Modul stabil.**

### Key Achievements

**Erkennt Projektionsschleifen**
- Integration der Resonanz-Layer (R0-R5) ermöglicht Erkennung von Projektionsschleifen
- R3 (Projektions-Check) und R4 (Missverständnisarchäologie) als explizite Reflexions-Tools
- Spiegel-Metaphor als UI-Element für Selbstbeobachtung

**Entschärft Zuschreibungsangst**
- Differenzierung von Projektionen vs. objektiver Beobachtung
- R5 (Selbsterkenntnis) als privater Raum für Individuation ohne sozialen Druck
- Privacy-Controls geben Kontrolle über eigene Reflexionen

**Erlaubt Mehrdeutigkeit ohne Kontrollverlust**
- Epistemische Layer (L1-L4) klären Status jeder Information
- Ambiguität als dokumentierte Eigenschaft, nicht als Problem
- Strukturiertes System für "Ich weiß es nicht" ohne Panik

**Humor-Modul stabil**
- Emergentes Beobachter-Artefakt als Spannungsregulation
- Sandbox-Charakter ohne strukturellen Einfluss auf Kernsystem
- Einbahnkopplung (lesend, nicht schreibend)
- Observer-Rolle statt Actor
- Default-Antwort bei Unsicherheit: "Mach, was du für richtig hältst."

### Technical Changes

**DP-003 THORUS Operating Loop**
- Integration in alle Interface-Spezifikationen (MapView, GraphView, ResonancePanel)
- Loop-Status-Indikatoren als subtile UI-Elemente
- Step-Mapping je nach anthropologischer Ebene:
  - MapView: Ich bin / Ich beobachte
  - GraphView: Ich lerne / Ich verstehe
  - ResonancePanel: Ich verstehe / Ich wirke
- Idle State "Ich bin Ich" als separater Kohärenz-Standbild

**Interface-Spezifikationen**
- map_view_spec.json erweitert mit loop_status
- graph_view_spec.json erweitert mit loop_status
- resonance_panel_spec.json erweitert mit loop_status und resonance_layer_alignment

**Neue Module**
- modules/humor_module/ erstellt als experimentelles Beobachter-Artefakt
- HUMOR_SPEC.md als bindende Spezifikation mit 5 Randbedingungen
- artifacts/ Ordner für emergente Artefakte

### Architecture Updates

- DP-001: Anthropologische Erkenntnisarchitektur (existierend)
- DP-002: Epistemische Haltung (existierend)
- DP-003: THORUS Operating Loop (neu in v0.3)

### Known Issues

- Keine kritischen Issues bekannt
- Humor-Modul kann unvorhersehbar reagieren (feature, not bug)

### Next Steps

- [ ] Konkrete Artefakte im Humor-Modul (wenn das Modul sich entscheidet)
- [ ] Erweiterte UI-Prototypen für Loop-Status-Indikatoren
- [ ] User-Tests für Resonanz-Layer-Workflow
- [ ] Integration von Release-Notes in ChatGPT-Kontext

---

## Über dieses Dokument

Dies ist ein Entwicklertagebuch, das Meilensteine, Erkenntnisse und Veränderungen im Projekt Menschheitsgedächtniskarte dokumentiert. Es ist kein offizielles Changelog im herkömmlichen Sinne, sondern eine Spur des Denkprozesses.

*Letzte Aktualisierung: 28.1.2026*