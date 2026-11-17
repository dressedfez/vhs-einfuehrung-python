# Kurstag 7 · Datenvisualisierung

Für Kurstag 7 gibt es zwei aufbereitete Marimo-Notebooks:

| Datei | Für wen? | Inhalt |
| --- | --- | --- |
| [kurstag_07_folien.py](kurstag_07_folien.py) | Dozent / gemeinsamer Unterricht | Folien mit Matplotlib, Seaborn, Plotly, interaktiver Auswahl und Musterbeispiel |
| [kurstag_07_teilnehmende.py](kurstag_07_teilnehmende.py) | Teilnehmende / Nacharbeiten | Arbeitsheft mit Beispielen, vier Basisübungen und automatischer Rückmeldung |

Das ursprüngliche Notebook [kurstag_07.py](kurstag_07.py) und die vorhandenen Keynote- und PDF-Dateien bleiben als Ausgangsmaterial erhalten. Die Verkaufsdaten werden in Pandas I und II an Kurstag 5 und 6 eingeführt; eine lokale Kopie für die Diagrammübungen liegt unter `data/online_shop_verkaufsdaten.xlsx`.

## Folien starten

Alle Befehle im Ordner `kurstag_07` ausführen. Voraussetzung ist eine installierte Version von [uv](https://docs.astral.sh/).

Präsentation starten:

```sh
uv run --script kurstag_07_folien.py
```

Für Live-Coding und die Folienansicht:

```sh
uvx --from "marimo==0.25.2" marimo edit kurstag_07_folien.py
```

Die Datei `layouts/kurstag_07_folien.slides.json` aktiviert das Folienlayout. Mit den Pfeiltasten blättern; **C** blendet den Code der aktuellen Folie ein.

## Arbeitsheft für Teilnehmende

```sh
uvx --from "marimo==0.25.2" marimo edit kurstag_07_teilnehmende.py
```

Codezellen mit **Shift+Enter** ausführen. Die Basisübungen behandeln Monatsumsätze, den Umsatzvergleich nach Region, Histogramme und interaktive Plotly-Balkendiagramme. Das abschließende Projekt führt von einer selbst gewählten Verkaufsfrage bis zum beschrifteten Diagramm und einer kurzen Interpretation. Lösungen der Basisübungen stehen in der Folienpräsentation.

Das offizielle VHS-Dresden-Logo liegt unter `public/vhs-dresden-logo.png` und wird auf der farbigen Titelfolie verwendet.

## HTML zum Weitergeben

```sh
uvx --from "marimo==0.25.2" marimo export html kurstag_07_folien.py -o kurstag_07_folien.html
uvx --from "marimo==0.25.2" marimo export html kurstag_07_teilnehmende.py -o kurstag_07_teilnehmende.html
```

Der statische Export enthält Texte und berechnete Beispiele. Für interaktive Auswahlfelder und das erneute Ausführen von Python die laufende Marimo-Anwendung verwenden.
