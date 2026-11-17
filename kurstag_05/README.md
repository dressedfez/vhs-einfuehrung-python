# Kurstag 5 · Pandas I: Tabellen laden und filtern

Für diesen Termin gibt es eigene Folien und ein Teilnehmer-Arbeitsheft:

| Datei | Einsatz |
| --- | --- |
| [Folien](kurstag_05_folien.py) | Gemeinsamer Unterricht mit Beispielen, Ausgaben und interaktiver Filterauswahl |
| [Arbeitsheft](kurstag_05_teilnehmende.py) | Erklärungen, ausführbare Schritte und zwei Übungen mit automatischer Rückmeldung |

Die Beispieldaten liegen lokal unter `online_shop_verkaufsdaten.xlsx`.

## Inhalte

Series und DataFrames, Tabellen aus Excel laden und prüfen, Spalten auswählen,
`loc` und `iloc`, boolesche Filter, mehrere Bedingungen und interaktive
Auswahlfelder. Die Übungen wenden Spaltenauswahl und kombinierte Filter an.
Diagramme aus `public/` veranschaulichen Series und DataFrames sowie die Auswahl
von Spalten und Zeilen.

## Starten

Im Ordner `kurstag_05`:

```sh
uv run --script kurstag_05_folien.py
uvx --from "marimo==0.25.2" marimo edit kurstag_05_teilnehmende.py
```

Die Datei `layouts/kurstag_05_folien.slides.json` aktiviert die Folienansicht.
Mit den Pfeiltasten blättern; **C** blendet den Code der aktuellen Folie ein.

Die Dateien `kurstag_05.py`, `Kurstag_05.key` und `Kurstag_05.pdf` stammen aus
der früheren Kursfassung. Visualisierung wird im überarbeiteten Acht-Termine-Kurs
an Tag 7 behandelt; die aktuellen Unterlagen stehen in
[Kurstag 7](../kurstag_07/README.md).
