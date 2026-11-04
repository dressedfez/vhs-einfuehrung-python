# Kurstag 5 · Datenvisualisierung

Für Kurstag 5 gibt es zwei aufbereitete Marimo-Notebooks:

| Datei | Für wen? | Inhalt |
| --- | --- | --- |
| [kurstag_05_folien.py](kurstag_05_folien.py) | Dozent / gemeinsamer Unterricht | Folien mit Matplotlib, Seaborn, Plotly, interaktiver Auswahl und Musterbeispiel |
| [kurstag_05_teilnehmende.py](kurstag_05_teilnehmende.py) | Teilnehmende / Nacharbeiten | Arbeitsheft mit Beispielen, vier Basisübungen und automatischer Rückmeldung |

Das ursprüngliche Notebook [kurstag_05.py](kurstag_05.py) und die vorhandenen Keynote- und PDF-Dateien bleiben als Ausgangsmaterial erhalten. Beide neuen Notebooks verwenden dieselben Verkaufsdaten wie Kurstag 4. Eine lokale Kopie liegt unter `data/online_shop_verkaufsdaten.xlsx`.

## Folien starten

Alle Befehle im Ordner `kurstag_05` ausführen. Voraussetzung ist eine installierte Version von [uv](https://docs.astral.sh/).

Präsentation starten:

```sh
uv run --script kurstag_05_folien.py
```

Für Live-Coding und die Folienansicht:

```sh
uvx --from "marimo==0.25.2" marimo edit kurstag_05_folien.py
```

Die Datei `layouts/kurstag_05_folien.slides.json` aktiviert das Folienlayout. Mit den Pfeiltasten blättern; **C** blendet den Code der aktuellen Folie ein.

## Arbeitsheft für Teilnehmende

```sh
uvx --from "marimo==0.25.2" marimo edit kurstag_05_teilnehmende.py
```

Codezellen mit **Shift+Enter** ausführen. Die Basisübungen behandeln Monatsumsätze, den Umsatzvergleich nach Region, Histogramme und interaktive Plotly-Balkendiagramme. Die Rückmeldungen prüfen die Ergebnisse und geben Hinweise. Lösungen stehen in der Folienpräsentation.

Das offizielle VHS-Dresden-Logo liegt unter `public/vhs-dresden-logo.png` und wird auf der farbigen Titelfolie verwendet.

## HTML zum Weitergeben

```sh
uvx --from "marimo==0.25.2" marimo export html kurstag_05_folien.py -o kurstag_05_folien.html
uvx --from "marimo==0.25.2" marimo export html kurstag_05_teilnehmende.py -o kurstag_05_teilnehmende.html
```

Der statische Export enthält Texte und berechnete Beispiele. Für interaktive Auswahlfelder und das erneute Ausführen von Python die laufende Marimo-Anwendung verwenden.
