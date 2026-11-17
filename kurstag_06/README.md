# Kurstag 6 · Pandas II: Daten bereinigen und auswerten

Für diesen Termin gibt es eigene Folien und ein Teilnehmer-Arbeitsheft:

| Datei | Einsatz |
| --- | --- |
| [Folien](kurstag_06_folien.py) | Gemeinsamer Unterricht mit Beispielen, Berechnungen und Pivot-Tabellen |
| [Arbeitsheft](kurstag_06_teilnehmende.py) | Ausführbare Beispiele und Basisübungen zu Spalten, Gruppierungen und Pivot-Tabellen |
| [Übung zu fehlenden Werten](datenbereinigung_uebung.md) | Kleine Tabelle zum Untersuchen, Bereinigen und begründeten Umgang mit fehlenden Angaben |

Die Beispieldaten liegen lokal unter `online_shop_verkaufsdaten.xlsx`.

## Inhalte

Fehlende Werte erkennen und bewusst behandeln, neue Spalten mit Berechnungen
anlegen, Kennzahlen aggregieren, mit `groupby` vergleichen sowie `pivot` und
`pivot_table` unterscheiden. Die Übung zu fehlenden Werten ergänzt das
Arbeitsheft um eine nachvollziehbare Bereinigungsaufgabe.
Diagramme aus `public/` zeigen neue Spalten, Aggregationen, Häufigkeiten und
Pivot-Tabellen.

## Starten

Im Ordner `kurstag_06`:

```sh
uv run --script kurstag_06_folien.py
uvx --from "marimo==0.25.2" marimo edit kurstag_06_teilnehmende.py
```

Die Datei `layouts/kurstag_06_folien.slides.json` aktiviert die Folienansicht.
Mit den Pfeiltasten blättern; **C** blendet den Code der aktuellen Folie ein.

Die Dateien `kurstag_06.py`, `Kurstag_06.key` und `Kurstag_06.pdf` stammen aus
der früheren Kursfassung. Maschinelles Lernen wird im überarbeiteten
Acht-Termine-Kurs an Tag 8 behandelt; die aktuellen Unterlagen stehen in
[Kurstag 8](../kurstag_08/README.md).
