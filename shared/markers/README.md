# Marker Pool

## Was ist der Marker Pool?

Der Marker Pool ist ein **neutrales, erweiterbares Resonanzarchiv** für Denk- und Beobachtungsanker.

Hier haben Gedanken noch keine Verpflichtung.

---

## Philosophie

### Grundhaltung

Marker sind:
- **Beobachtungsanker**, keine Thesen
- **Gleichwertig** – ohne Hierarchie oder Bewertung
- **Unscharf erlaubt** – Unklarheit ist kein Fehler
- **Widersprüchlich erlaubt** – Konflikte bleiben stehen

Marker sind **nicht**:
- ein Bewertungssystem
- ein Theorieraum
- ein Entscheidungsinstrument

### Der Pool als

- **Resonanzarchiv**: Orte, an denen Gedanken widerhallen können
- **Denk-Spielplatz**: Raum zum Ausprobieren ohne Konsequenzen
- **Projektionssammler**: Wo sich Muster zeigen, noch bevor sie Muster sind

### Prinzipien

1. **Keine Relationen erzwingen**: Marker stehen für sich allein. Verbindungen entstehen erst durch spätere Reflexion.
2. **Keine Gewichtung**: Jeder Marker ist gleich wichtig.
3. **Keine Wahrheitsebenen**: Es gibt kein "wahrer" oder "falscher", nur beobachtet.
4. **Bestand statt Verwerfung**: Marker bleiben bestehen, auch wenn sie sich später als unpassend oder widersprüchlich erweisen.

---

## Struktur

### Marker-Format

Ein Marker enthält minimal:
- `id`: Eindeutige Kennung (MARK-XXXXXX)
- `name`: Bezeichnung des Markers
- `short_description`: 1-3 Sätze, was beobachtet wird (ohne Interpretation)
- `tags`: Freie Tags, optional
- `status`: roh | angetestet | kombinierbar
- `meta`: Optionale Notizen

### Status-Werte

- **roh**: Neue Beobachtung, noch nicht in Kontexte eingebunden
- **angetestet**: In mindestens einem Kontext verwendet
- **kombinierbar**: Zeigt Verbindbarkeit zu anderen Markern

Wichtig: Der Status wird **ausschließlich manuell** gesetzt. Es gibt keine automatische Änderung durch Nutzung oder Häufigkeit. Der Status bleibt eine bewusste Reflexionsentscheidung.

---

## Verwendung

### Marker erstellen

1. Kopiere `template_marker.json` als `MARK-XXXXXX.json` in `items/`
2. Fülle die Felder aus – bleibe neutral und beschreibend
3. Vergib eine eindeutige ID

### Marker verwenden

Marker können:
- in anderen Modulen referenziert werden
- als Inspirationsanker dienen
- miteinander kombiniert werden
- ignoriert oder neu interpretiert werden

Es gibt keine Verpflichtung, Marker zu verwenden. Es gibt keine Strafe für widersprüchliche Marker.

---

## Unterschied zum Candidate Pool

| Marker Pool | Candidate Pool |
|-------------|----------------|
| Neutraler Resonanzraum | Workflow-gesteuert |
| Keine Promotion | candidate → shortlisted → promoted |
| Marker bleiben bestehen | Können rejected werden |
| Beobachtungsanker | Kandidaten für Module |
| Keine Hierarchie | Klare Ziel-Ordnung |

---

## Index

`marker_index.json` ist rein technisch und dient der Übersicht und Auffindbarkeit. Er enthält keine Ordnung, keine Gewichtung und keine implizite Struktur. Die einzelnen Marker-JSONs sind konzeptionell primär.

---

## Haltung

Der Marker Pool ist der Ort, an dem Gedanken noch keine Verpflichtung haben.

Hier darf:
- unscharf sein
- widersprüchlich sein
- später verworfen oder umgedeutet werden

Hier ist Platz für:
- Beobachtungen ohne Beweis
- Intuitionen ohne Begründung
- Musterentdeckung ohne Theorie

---

## Erweiterung

Der Pool ist offen und erweiterbar. Marker können jederzeit hinzugefügt werden. Es gibt keine Beschränkung auf Themen, Epochen oder Kulturen.

Die einzige Grenze ist die Neutralität der Formulierung: Marker beschreiben, sie bewerten nicht.
