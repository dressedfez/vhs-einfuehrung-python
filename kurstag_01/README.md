# Kurstag 1: Erste Schritte mit Python, uv und marimo

[![Open in molab](https://marimo.io/molab-shield.svg)](https://molab.marimo.io/github/dressedfez/vhs-einfuehrung-python/blob/main/kurstag_01/kurstag_01_folien.py)

Für Kurstag 1 gibt es zwei aufbereitete Notebooks:

| Datei | Für wen? | Gestaltung |
| --- | --- | --- |
| [kurstag_01_folien.py](kurstag_01_folien.py) | Dozent / gemeinsamer Unterricht | Präsentation mit Folien |
| [kurstag_01_teilnehmende.py](kurstag_01_teilnehmende.py) | Teilnehmende / Nacharbeiten | Normales Notebook mit Erklärungen, editierbaren Beispielen, Übungen und Prüfungen |

Das ursprüngliche Notebook `kurstag_01.py` bleibt als Ausgangsmaterial erhalten.

## PowerPoint mit VS-Code-Praxisteil

[Kurstag_01_Python_uv_VSCode.pptx](Kurstag_01_Python_uv_VSCode.pptx) enthält
28 Folien im Stil der bestehenden Keynote, einschließlich Dozentennotizen.
Der Praxisteil zeigt das Anlegen eines Projekts mit uv, das Öffnen des
Projektordners in VS Code, die Auswahl der `.venv` und die Prüfung des
Python-Interpreters. Eine Projektübung führt zum Arbeitsheft in marimo;
anschließend folgen Python-Grundlagen und Übungen.

Die folgenden Abschnitte beschreiben die marimo-Notebooks.

Definitionen, Regeln, Eigenschaften und Warnungen sind in beiden aufbereiteten
Notebooks durch Admonitions (`note`, `tip`, `attention`) hervorgehoben.

## Arbeitsheft für Teilnehmende

Im Ordner `kurstag_01` starten:

```sh
marimo edit kurstag_01_teilnehmende.py
```

Das Arbeitsheft verwendet kein Folienlayout. Erklärung, Beispielcode,
Übungsauftrag und automatische Rückmeldung stehen untereinander. Die Beispiele
zeigen den tatsächlichen Python-Code; Änderungen erfordern kein Anpassen eines
zweiten Codeblocks. Drei Basisübungen haben neutrale, orange oder grüne
Rückmeldungen. Die Umbenennungsaufgabe zu Variablen wird gemeinsam besprochen. Bonusaufgaben sind getrennt gekennzeichnet. Musterlösungen stehen
nur in der Dozentenpräsentation; eine Notizsektion dient dem eigenen Rückblick.

Jede Person bearbeitet eine eigene lokale Kopie. Mit **Shift+Enter** eine Zelle
ausführen. Die Prüfung darunter aktualisiert sich automatisch. Benannte
Antwortvariablen beibehalten, da die Prüfzellen darauf zugreifen. Prüfzellen
sind eingeklappt, können bei Interesse aber ebenfalls gelesen werden.

Listen und Mengen sind der optionale Zusatzteil. Für einen kurzen ersten
Kurstag bis zum Zwischenstopp arbeiten und anschließend den Rückblick ausfüllen.
Fehlt die lokale Einrichtung, zu zweit an einem funktionierenden Rechner
arbeiten und regelmäßig die Rollen wechseln.

Die folgende Anleitung bezieht sich auf die Dozentenpräsentation mit
42 Inhaltsfolien.

## Starten

Alle Befehle im Ordner `kurstag_01` ausführen. Voraussetzung ist eine installierte
Version von [uv](https://docs.astral.sh/uv/).

Präsentation im Browser starten:

```sh
marimo run kurstag_01_folien.py
```

**Für die interaktiven Codeübungen und für Live-Coding:**

```sh
marimo edit kurstag_01_folien.py
```

Auch Folie 8 lässt sich so live bearbeiten: In der Folienansicht **C** drücken,
`anzahl_teilnehmende` ändern und mit **Shift+Enter** ausführen. `marimo run`
zeigt die Präsentation nur an; zum Bearbeiten während des Vortrags `marimo edit`
verwenden.

Diese Befehle setzen voraus, dass marimo bereits installiert und im aktuellen
Terminal verfügbar ist. Ohne Installation kannst du es einmalig mit `uvx`
starten, zum Beispiel: `uvx --from "marimo==0.25.2" marimo run kurstag_01_folien.py`.

Die Datei `layouts/kurstag_01_folien.slides.json` aktiviert das Folienlayout.
Falls nötig, in der App-Vorschau das Layout **Slides** auswählen.
Mit den Pfeiltasten navigieren; mit **C** den Code für Live-Änderungen einblenden.
Auf Folie 8 ist der sichtbare Code die echte Python-Zelle und live änderbar.
Auf den weiteren Beispiel-Folien sind die angezeigten Codeblöcke Dokumentation;
dort bei Änderungen auch das Textargument von `beispiel` anpassen.

## Code ergänzen und ausführen

Vier vorbereitete Codezellen stehen jeweils direkt hinter dem Arbeitsauftrag:

| Folie | Codeübung | Zu ergänzen |
| --- | --- | --- |
| 12 | Variablennamen | `a` und `b` im Code verständlich umbenennen |
| 25 | Kursprofil | f-String und Gesamtpreis statt `None` |
| 33 | Listen | Gerichte, Indexzugriffe und `append` |
| 39 | Mengen | `difference` und optional `symmetric_difference` |

Das Notebook mit **`marimo edit`** starten. In der Folienansicht mit **C** den
Zelleditor öffnen, den vorbereiteten Python-Code ändern und mit **Shift+Enter**
ausführen. Änderungen werden direkt in der Zellenausgabe sichtbar. Die letzte
Zeile zeigt die Ergebnisse in der dort angegebenen Reihenfolge. Direkt hinter
den Übungen 2–4 folgt eine abhängige Prüfzelle, die sich automatisch aktualisiert.
Bei Übung 1 folgt stattdessen ein Fragenkatalog zur gemeinsamen Besprechung.

Die Zellen sind auch vor dem Ergänzen ausführbar: `None` steht für eine noch
offene Antwort, `[]` für die noch leere Gerichteliste. Zuerst die Liste füllen,
dann die Indexzugriffe ergänzen. Die Ausgabe wird bei jeder Ausführung aus den
aktuellen Eingaben neu berechnet. Für diese Übungszellen muss kein zusätzlicher
Markdown-Codeblock angepasst werden.

### Automatische Rückmeldung

- **Neutral · Noch offen:** Die Starterwerte wurden noch nicht ergänzt.
- **Orange · Noch nicht ganz:** Ein Ergebnis passt noch nicht; ein Hinweis hilft weiter.
- **Grün · Richtig:** Die geprüften Anforderungen sind erfüllt.

Kursprofil und Mengenübung prüfen Basis und Bonus getrennt. Eine offene
Bonusaufgabe verhindert die grüne Rückmeldung zur Basisaufgabe nicht.
Die Prüfungen vergleichen Ergebnisse und schreiben keinen Lösungsweg vor.
Beim Kursprofil müssen Name, Kursanzahl und formatierter Einzelpreis im Text
stehen; beim Bonus wird der Gesamtpreis als Text mit genau zwei Nachkommastellen
ohne Währungsangabe erwartet. Bei der Listenübung werden die Zugriffe auf die
ursprünglichen drei Gerichte vor dem Anhängen des vierten geprüft.

Bei der Namensübung werden echte Variablen umbenannt: `a = "Frank"` und
`b = 3`. Die Namen müssen auch in der Ausgabezeile angepasst werden; die Werte
bleiben gleich. Ein gemeinsamer Fragenkatalog ersetzt die automatische Bewertung,
da verschiedene verständliche Namen möglich sind.

Die Prüfungen garantieren weder, dass
ein f-String noch dass `append` verwendet wurde: Auch andere korrekte Lösungswege
liefern passende Ergebnisse. Syntax- und Ausführungsfehler werden von Python in
der Übungszelle angezeigt; erst nach deren Korrektur aktualisiert sich die Prüfung.

Die Rückmeldungszellen sind im Folienlayout als Fragmente eingeordnet: Nach der
Aufgabe einen Schritt weiterblättern, um das Feedback einzublenden. Im normalen
Notebook stehen sie direkt unter dem Code. Die Prüfungen verwenden exportierte
Antwortvariablen; deren Namen und die vorgegebenen Antwortzuweisungen beibehalten.

Die zugehörigen Auflösungen folgen nach dem Bearbeiten. Die Vertiefungen zu
Palindromen, Zahlenfolgen und Buchstabenmengen können in eigenen Zellen ergänzt
werden. Für unveränderte Startervorlagen vor Kursbeginn eine Kopie des Notebooks
anlegen; das Bearbeiten verändert die Notebook-Datei.

## Ablauf und Differenzierung

| Folien | Thema | Einsatz |
| --- | --- | --- |
| 1–6 | Lernziele, Zusammenarbeit und Werkzeuge | Gemeinsam starten |
| 7–13 | Variablen und verständliche Namen | Erklärung, Aufgabe, Auflösung |
| 14–23 | str, int, float, bool und Umwandlungen | Vorhersagen, ausführen, erklären |
| 24–27 | Kursprofil und Zwischenstopp | Anwenden und Verständnis prüfen |
| 28–34 | Listen, Änderungen, Indizes und Slicing | Optional / Nacharbeit |
| 35–40 | Mengen und Mengenoperationen | Optional / Nacharbeit |
| 41–42 | Typenübersicht und Rückblick | Nachschlagen / Abschluss |

Bei knappem Zeitbudget direkt nach Folie 27 zur Abschlussfolie wechseln.
Die Auflösungen folgen jeweils auf die Aufgaben: erst gemeinsam bearbeiten,
dann weiterblättern. Basisaufgaben und Vertiefungen unterstützen verschiedene
Vorkenntnisse. Beim Arbeiten zu zweit regelmäßig zwischen Tippen und Erklären
wechseln; falls uv fehlt, gemeinsam einen eingerichteten Rechner nutzen.

Neue Übungsvariablen nur in einer Zelle definieren. Die vorbereiteten Beispiele
verwenden lokale Namen mit führendem Unterstrich, damit sie unabhängig bleiben.
Änderungen an Listen und Mengen erfolgen innerhalb derselben Zelle und sind
beim erneuten Ausführen wiederholbar.

## HTML zum Weitergeben

```sh
marimo export html kurstag_01_folien.py -o kurstag_01_folien.html
```

Der statische Export enthält die berechneten Ergebnisse. Für Live-Coding und
das erneute Ausführen von Python die laufende marimo-Anwendung verwenden.
