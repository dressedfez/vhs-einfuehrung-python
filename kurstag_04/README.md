# Kurstag 4 · Datenanalyse mit Pandas

Für Kurstag 4 gibt es zwei aufbereitete Marimo-Notebooks:

| Datei | Für wen? | Inhalt |
| --- | --- | --- |
| [kurstag_04_folien.py](kurstag_04_folien.py) | Dozent / gemeinsamer Unterricht | Folien mit Beispielen, interaktiver Auswahl und Musterlösungen |
| [kurstag_04_teilnehmende.py](kurstag_04_teilnehmende.py) | Teilnehmende / Nacharbeiten | Arbeitsheft mit Beispielen, vier Basisübungen und automatischer Rückmeldung |

Das ursprüngliche Notebook [kurstag_04.py](kurstag_04.py) und die vorhandenen Quelldateien bleiben erhalten. Die neuen Notebooks verwenden `online_shop_verkaufsdaten.xlsx` als gemeinsame Beispieldatei.

## Folien starten

Alle Befehle im Ordner `kurstag_04` ausführen. Voraussetzung ist eine installierte Version von [uv](https://docs.astral.sh/).

Präsentation starten:

```sh
uv run --script kurstag_04_folien.py
```

Für Live-Coding und die Folienansicht:

```sh
uvx --from "marimo==0.25.2" marimo edit kurstag_04_folien.py
```

Die Datei `layouts/kurstag_04_folien.slides.json` aktiviert das Folienlayout. Mit den Pfeiltasten blättern; **C** blendet den Code der aktuellen Zelle ein.

## Arbeitsheft für Teilnehmende

```sh
uvx --from "marimo==0.25.2" marimo edit kurstag_04_teilnehmende.py
```

Codezellen mit **Shift+Enter** ausführen. Die Basisübungen behandeln die Auswahl von Zeilen und Spalten, das Berechnen einer Spalte, `groupby` und `pivot_table`. Rückmeldungen prüfen die Ergebnisse und geben Hinweise, ohne einen bestimmten Lösungsweg vorzuschreiben. Lösungen stehen in der Folienpräsentation.

Das offizielle VHS-Dresden-Logo liegt als lokale Datei unter `public/vhs-dresden-logo.png` und wird für die Titelfolie verwendet.

## HTML zum Weitergeben

```sh
uvx --from "marimo==0.25.2" marimo export html kurstag_04_folien.py -o kurstag_04_folien.html
uvx --from "marimo==0.25.2" marimo export html kurstag_04_teilnehmende.py -o kurstag_04_teilnehmende.html
```

Der HTML-Export enthält die berechneten Beispiele. Für interaktive Auswahlen und das erneute Ausführen von Python die laufende Marimo-Anwendung verwenden.
