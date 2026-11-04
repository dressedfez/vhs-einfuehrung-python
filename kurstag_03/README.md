# Kurstag 3 · Funktionen, Klassen und Module

[![Folien in marimo öffnen](https://marimo.io/molab-shield.svg)](https://molab.marimo.io/github/dressedfez/vhs-einfuehrung-python/blob/main/kurstag_03/kurstag_03_folien.py)

Für Kurstag 3 gibt es zwei aufbereitete Notebooks:

| Datei | Für wen? | Gestaltung |
| --- | --- | --- |
| [kurstag_03_folien.py](kurstag_03_folien.py) | Dozent / gemeinsamer Unterricht | Präsentation mit Folien, Beispielen und Lösungsvorschlägen |
| [kurstag_03_teilnehmende.py](kurstag_03_teilnehmende.py) | Teilnehmende / Nacharbeiten | Arbeitsheft mit Erklärungen, ausführbaren Beispielen, vier Basisübungen und automatischer Rückmeldung |

Das ursprüngliche Notebook [kurstag_03.py](kurstag_03.py) bleibt als Ausgangsmaterial erhalten. Die beiden vorhandenen Packages `simple_math_package` und `kursverwaltung` werden als Beispiele für Importe und Modulaufbau verwendet.

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
