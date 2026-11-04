# Kurstag 2 · Rechnen, entscheiden und wiederholen

[![Folien in marimo öffnen](https://marimo.io/molab-shield.svg)](https://molab.marimo.io/github/dressedfez/vhs-einfuehrung-python/blob/main/kurstag_02/kurstag_02_folien.py)

Für Kurstag 2 gibt es zwei aufbereitete Notebooks:

| Datei | Für wen? | Gestaltung |
| --- | --- | --- |
| [kurstag_02_folien.py](kurstag_02_folien.py) | Dozent / gemeinsamer Unterricht | Präsentation mit Folien, Beispielen und Lösungsvorschlägen |
| [kurstag_02_teilnehmende.py](kurstag_02_teilnehmende.py) | Teilnehmende / Nacharbeiten | Arbeitsheft mit Erklärungen, editierbaren Beispielen, vier Basisübungen und automatischer Rückmeldung |

Das ursprüngliche Notebook [kurstag_02.py](kurstag_02.py) bleibt als Ausgangsmaterial erhalten.

## Folien starten

Alle Befehle im Ordner `kurstag_02` ausführen. Voraussetzung ist eine installierte Version von [uv](https://docs.astral.sh/uv/).

Präsentation starten:

```sh
uv run --script kurstag_02_folien.py
```

Für Live-Coding und die Folienansicht:

```sh
uvx --from "marimo==0.25.2" marimo edit kurstag_02_folien.py
```

Die Datei `layouts/kurstag_02_folien.slides.json` aktiviert das Folienlayout. Falls nötig, in der App-Vorschau das Layout **Slides** auswählen. Mit den Pfeiltasten navigieren; mit **C** den Code der aktuellen Zelle einblenden. Jedes Beispiel steht auf einer eigenen Folie. Erklärung, Python-Code und Ergebnis sind untereinander angeordnet.

## Arbeitsheft für Teilnehmende

Im Ordner `kurstag_02` starten:

```sh
uvx --from "marimo==0.25.2" marimo edit kurstag_02_teilnehmende.py
```

Die Codezellen mit **Shift+Enter** ausführen. Die vier Basisübungen behandeln Ganzzahldivision und Rest, Bedingungen, eine `for`-Schleife mit Akkumulator und eine `while`-Schleife. Die Rückmeldungen prüfen Ergebnisse und geben Hinweise, ohne einen bestimmten Lösungsweg vorzuschreiben. Musterlösungen stehen in der Folienpräsentation.

## Ablauf und Zusatzteile

Der gemeinsame Grundteil führt durch Operatoren, Vergleiche und Bedingungen, `while`- und `for`-Schleifen sowie interaktive marimo-Elemente. Die Abschnitte **Zusatzteil** können je nach Lerntempo nach der jeweiligen Einführung bearbeitet oder zur Nacharbeit genutzt werden. Sie behandeln `break` und `continue`, Schleifen mit `else`, List Comprehensions, komplexe Zahlen und den Umgang mit Eingabefehlern.

Der Pillow-Bildausschnitt ist ebenfalls freiwillig und benötigt das Zusatzpaket. Zum Öffnen des Arbeitshefts mit Pillow:

```sh
uvx --with "pillow==12.1.1" --from "marimo==0.25.2" marimo edit kurstag_02_teilnehmende.py
```

## HTML zum Weitergeben

```sh
uvx --from "marimo==0.25.2" marimo export html kurstag_02_folien.py -o kurstag_02_folien.html
uvx --from "marimo==0.25.2" marimo export html kurstag_02_teilnehmende.py -o kurstag_02_teilnehmende.html
```

Der statische Export enthält die Textinhalte und berechneten Beispiele. Für interaktive Eingaben und das erneute Ausführen von Python die laufende marimo-Anwendung verwenden.
