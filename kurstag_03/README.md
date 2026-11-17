# Kurstag 3 · Funktionen, Klassen und Module

[![Folien in marimo öffnen](https://marimo.io/molab-shield.svg)](https://molab.marimo.io/github/dressedfez/vhs-einfuehrung-python/blob/main/kurstag_03/kurstag_03_folien.py)

Für Kurstag 3 gibt es zwei aufbereitete Notebooks:

| Datei | Für wen? | Gestaltung |
| --- | --- | --- |
| [kurstag_03_folien.py](kurstag_03_folien.py) | Dozent / gemeinsamer Unterricht | Präsentation mit Folien, Beispielen und Lösungsvorschlägen |
| [kurstag_03_teilnehmende.py](kurstag_03_teilnehmende.py) | Teilnehmende / Nacharbeiten | Arbeitsheft mit Erklärungen, ausführbaren Beispielen, vier Basisübungen und automatischer Rückmeldung |

Das ursprüngliche Notebook [kurstag_03.py](kurstag_03.py) bleibt als Ausgangsmaterial erhalten. Die beiden vorhandenen Packages `simple_math_package` und `kursverwaltung` werden als Beispiele für Importe und Modulaufbau verwendet.

## Einsatz an zwei Terminen

- **Termin 3:** Abschnitte „Funktionen“, „Parameter und Argumente“, „Rückgabewerte“, „Lambda-Funktionen“ sowie `map` und `filter`. Mit den ersten beiden Basisübungen abschließen.
- **Termin 4:** Mit „Klassen und Objekte“ fortfahren, dann Vererbung/Polymorphismus und Module/Packages bearbeiten. Die Übungen zu Kleingruppen und austauschbarem Verhalten dienen als Praxisaufgabe. `reduce`, innere Funktionen und tiefe Vererbungsbeispiele bleiben Zusatzstoff.

So bleibt Zeit, Funktionen selbst zu schreiben und die Fehlerausgaben gemeinsam zu lesen, bevor Klassen und Dateistruktur dazukommen.

Im Abschnitt zu Termin 4 zeigen die Folien und das Arbeitsheft zwei lokale
Abbildungen aus `public/`: `Klassendiagramm.png` ordnet Klassenname,
Eigenschaften und Methoden ein; `KlassendiagrammVererbung.png` veranschaulicht
die Ist-ein- und Hat-ein-Beziehungen.

## Folien starten

Alle Befehle im Ordner `kurstag_03` ausführen. Voraussetzung ist eine installierte Version von [uv](https://docs.astral.sh/).

Präsentation starten:

```sh
uv run --script kurstag_03_folien.py
```

Für Live-Coding und die Folienansicht:

```sh
uvx --from "marimo==0.25.2" marimo edit kurstag_03_folien.py
```

Die Datei `layouts/kurstag_03_folien.slides.json` aktiviert das Folienlayout. Falls nötig, in der App-Vorschau das Layout **Slides** auswählen. Mit den Pfeiltasten blättern; **C** blendet den Code der aktuellen Zelle ein. Jedes Beispiel steht auf einer eigenen Folie.

## Arbeitsheft für Teilnehmende

Im Ordner `kurstag_03` starten:

```sh
uvx --from "marimo==0.25.2" marimo edit kurstag_03_teilnehmende.py
```

Die Codezellen mit **Shift+Enter** ausführen. Die vier Basisübungen behandeln Standardwerte und Rückgabewerte, `map` und `filter`, Klassenmethoden und Polymorphismus. Die Rückmeldungen prüfen Ergebnisse und geben Hinweise, ohne einen bestimmten Lösungsweg vorzuschreiben. Musterlösungen stehen in der Folienpräsentation.

Die Abschnitte **Zusatzteil** vertiefen innere Funktionen und `reduce`. Die Module `simple_math_package` und `kursverwaltung` lassen sich aus dem Arbeitsheft importieren, wenn der Startbefehl im Ordner `kurstag_03` ausgeführt wird.

## HTML zum Weitergeben

```sh
uvx --from "marimo==0.25.2" marimo export html kurstag_03_folien.py -o kurstag_03_folien.html
uvx --from "marimo==0.25.2" marimo export html kurstag_03_teilnehmende.py -o kurstag_03_teilnehmende.html
```

Der statische Export enthält die Textinhalte und berechneten Beispiele. Für das erneute Ausführen von Python die laufende marimo-Anwendung verwenden.
