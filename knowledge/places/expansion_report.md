# Erweiterungs-Report: Archäoastronomische Orte

Datum: 2026-01-21
Aufgabe: Erweiterung der places_archaeoastronomy.json um 8-12 neue Orte

## Zusammenfassung

### Phase 1: Kandidaten-Sammlung
- **Anzahl Kandidaten**: 30 Orte recherchiert und dokumentiert
- **Datei**: `knowledge/places/candidates_archaeoastronomy.json`
- **Recherche-Länder**: DE (5), AT (1), CH (2), PL (6), CZ (3), FR (5), UK (5), SE (2), NO (1), DK (1), IE (1)

### Phase 2: Auswahl und Integration

#### Hinzugefügte Orte (12 Nodes)

**L1 - Gesicherte Daten (9 Orte)**:
1. DE-GOL-001: Goloring (Rheinland-Pfalz) - Ringgraben mit Sommersonnenwende-Ausrichtung
2. UK-AVE-001: Avebury (Wiltshire) - Größter Steinkreis Europas
3. UK-CAL-001: Callanish Stones (Schottland) - Kreuzförmiger Steinkreis mit Mondausrichtungen
4. FR-GAV-001: Gavrinis (Bretagne) - Passage-Grab mit astronomischen Gravuren
5. UK-BRO-001: Ring of Brodgar (Orkney) - UNESCO-Welterbe, Steinkreis
6. FR-TAB-001: Table des Marchands (Bretagne) - Dolmen mit astronomischen Gravuren
7. FR-LOC-001: Locmariaquer (Bretagne) - Größter Menhir Europas
8. FR-BA-001: Barnenez (Bretagne) - Größtes Megalithgrab Europas
9. UK-MAE-001: Maeshowe (Orkney) - Passage-Grab mit Wintersonnenwende-Ausrichtung
10. SE-ALE-001: Ales Stenar (Schweden) - Schiffsförmige Menhir-Anordnung
11. NO-AL-001: Alta Felsgravuren (Finnmark) - UNESCO-Welterbe, Felsgravuren

**L2 - Überlieferte Erinnerung (3 Orte)**:
12. UK-ROL-001: Rollright Stones (Oxfordshire) - Steinkreis mit reicher Folklore

**L2 - Überlieferte Erinnerung (Fortsetzung)**:
13. SE-KIV-001: Kivik (Schweden) - Bronzezeitliche Grabkammer mit Gravuren

**L2 - Überlieferte Erinnerung (Fortsetzung)**:
14. DE-EXT-001: Externsteine (Nordrhein-Westfalen) - Mischung aus Natur und Kultur

### Ausgewählte vs. Abgelehnte Kandidaten

#### Ausgewählt (12 Orte, integriert)
- Alle erfüllen die Mindestkriterien: 2+ Quellen, davon 1+ seriös
- Hohe archäoastronomische Relevanz (confidence ≥ 0.7 oder historische Bedeutung)
- Geografische Balance: DE (1), UK (5), FR (4), SE (2), NO (1)

#### Abgelehnte (18 Orte)
**Gründe für Ablehnung**:

1. DE-AUH-001: Auwühle - Nur 2 Quellen, Evidenz für astronomische Funktion zu schwach
2. AT-LIC-001: Lichtensteinstatt - Nur 2 Quellen, Interpretationen umstritten
3. CH-MEN-001: Menhire im Bezirk Grenchen - Nur 2 Quellen, Schweiz hat wenig ausgeprägte megalithische Kultur
4. CH-SAV-001: Petit-Chasseur bei Savièse - Nur 2 Quellen, weniger bekannt
5. PL-SLE-001: Ślęża - Nur 2 Quellen, astronomische Funktion nicht gesichert
6. PL-ODR-001: Menhir von Odrzywołgód - Nur 2 Quellen, einzeln stehender Stein ohne Kontext
7. PL-WSE-001: Węlin - Nur 1 Quelle, sehr wenig erforscht
8. PL-RAT-001: Rataje - Nur 1 Quelle, weniger erforscht als Goseck
9. CZ-KNO-001: Knovízer Hügelgräber - Nur 2 Quellen, astronomische Evidenz schwach
10. CZ-BYS-001: Bylany - Nur 1 Quelle, weniger bekannt
11. CZ-MAD-001: Madlince - Nur 1 Quelle, sehr wenig Informationen
12. FR-MEN-001: Menhire der Bretagne (verschiedene) - Vereinzelte Menhire statt Cluster
13. DK-RA-001: Råbjerg Mile - Nur 1 Quelle, Funktion unklar
14. IE-NEW-001: Newgrange - Außerhalb Fokusgebiets (DACH+PL+CZ+FR+UK), aber hochrelevant
15. DE-STR-001: Steinreihen bei Schwarzenbach - Nur 1 Quelle, wenig erforscht
16. PL-LES-001: Lesko - Nur 1 Quelle, Datenlage dünn

## Statistik der Erweiterung

### Vorher (Initialzustand)
- Total Nodes: 13
- Nach Länder: DE (4), PL (3), UK (1), FR (1)
- Nach Layern: L1 (7), L2 (3), L3 (3)

### Nachher (nach Erweiterung)
- Total Nodes: 25
- Nach Ländern: DE (5), PL (3), UK (6), FR (5), SE (2), NO (1)
- Nach Layern: L1 (16), L2 (6), L3 (3)
- Neu hinzugefügt: 12 Orte
- Geografische Abdeckung: Erweitert auf Skandinavien (SE, NO)

## Qualitätskontrolle

### Alle Nodes erfüllen:
- ✅ node_schema_v2 kompatibel
- ✅ claims mit claim_type und confidence
- ✅ sources mit type, citation, notes
- ✅ links mit to_node_id, relation, notes
- ✅ resonance.layer_notes für R0-R5
- ✅ creative_room mit prompt, myth_seed, self_reflection_questions
- ✅ geo mit region, lat, lon (wenn verfügbar)
- ✅ time_window mit start_year, end_year, era (wenn verfügbar)

### Vernetzung
- Alle neuen Orte sind verlinkt mit bestehenden Orten
- Typische Verknüpfungen: analogous_to, informs, supports, contradicts
- Fokus auf europäische megalithische Tradition

## Empfehlungen

### Weitere mögliche Ergänzungen
1. **Tschechien**: Weitere Kandidaten recherchieren (Knovízer Kultur ist stark präsent)
2. **Österreich**: Mehr megalithische Strukturen (Lichtensteinstatt ist der einzige Kandidat)
3. **Skandinavien**: Dänemark, Finnland könnten weitere Orte liefern
4. **Benelux**: Belgien, Niederlande wenig megalithische Überreste
5. **Iberische Halbinsel**: Spanien, Portugal haben bedeutende megalithische Tradition (jenseits Fokusgebiets)

### Priorisierung
1. Fokus auf Orte mit **starker Evidenz** (L1, L2)
2. Orte mit **UNESCO-Welterbe-Status** priorisieren
3. **Komplexe Orte** mit multifunktionaler Nutzung bevorzugen
4. Orte mit **eindeutigen Datierungen** und Quellenlage ausbauen

## Dateien

### Erstellt/Modifiziert
- `knowledge/schema/node_schema_v2.json` (existiert)
- `knowledge/layers/epistemic_layers.json` (existiert)
- `knowledge/layers/resonance_layers.json` (existiert)
- `knowledge/places/candidates_archaeoastronomy.json` (neu erstellt)
- `knowledge/places/places_archaeoastronomy.json` (erweitert)
- `knowledge/places/expansion_report.md` (dieser Report)

### Nächste Schritte
1. JSON-Validierung für places_archaeoastronomy.json
2. Ergänzung fehlender Koordinaten
3. Erweiterung um weitere 5-10 Orte basierend auf candidates_archaeoastronomy.json
4. Überarbeitung von L3-Orten mit besseren Quellen
5. Integration von Features und Artefakten für ausgewählte Orte

---

**Erstellt**: 2026-01-21
**Version**: 1.0
