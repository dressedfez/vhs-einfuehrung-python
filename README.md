# Python für Daten und KI

Ein Einführungskurs der Volkshochschule Dresden. Die acht Termine führen von den
ersten Python-Programmen über Datenanalyse bis zu Visualisierung und
maschinellem Lernen.

## Kursmaterialien für acht Termine

Jeder Kurstag hat Folien für den gemeinsamen Unterricht und ein Arbeitsheft für
die Teilnehmenden. Die jeweiligen README-Dateien enthalten Startanleitungen.

| Termin | Schwerpunkt | Folien | Arbeitsheft |
| --- | --- | --- | --- |
| 1 | Python, uv, marimo, Variablen und Datentypen | [Kurstag 1](kurstag_01/kurstag_01_folien.py) | [Arbeitsheft](kurstag_01/kurstag_01_teilnehmende.py) |
| 2 | Bedingungen, Schleifen, interaktive Elemente, Listen und Dictionaries | [Kurstag 2](kurstag_02/kurstag_02_folien.py) | [Arbeitsheft](kurstag_02/kurstag_02_teilnehmende.py) |
| 3 | Funktionen, Parameter, Rückgabewerte, `map` und `filter` | [Folien](kurstag_03/kurstag_03_folien.py) | [Arbeitsheft](kurstag_03/kurstag_03_teilnehmende.py) |
| 4 | Klassen, Module und Packages; Fehlermeldungen lesen | [Folien](kurstag_03/kurstag_03_folien.py) | [Arbeitsheft](kurstag_03/kurstag_03_teilnehmende.py) |
| 5 | Pandas I: Tabellen laden, prüfen, auswählen und filtern | [Folien](kurstag_05/kurstag_05_folien.py) | [Arbeitsheft](kurstag_05/kurstag_05_teilnehmende.py) |
| 6 | Pandas II: fehlende Werte, Berechnungen, Gruppierungen und Pivot-Tabellen | [Folien](kurstag_06/kurstag_06_folien.py) | [Arbeitsheft](kurstag_06/kurstag_06_teilnehmende.py) · [Datenbereinigungsübung](kurstag_06/datenbereinigung_uebung.md) |
| 7 | Visualisierung und Datenprojekt | [Kurstag 7](kurstag_07/kurstag_07_folien.py) | [Arbeitsheft](kurstag_07/kurstag_07_teilnehmende.py) |
| 8 | Maschinelles Lernen mit Scikit-Learn | [Kurstag 8](kurstag_08/kurstag_08_folien.py) | [Arbeitsheft](kurstag_08/kurstag_08_teilnehmende.py) |

Die Termine 3 und 4 stehen als getrennte Abschnitte in den gemeinsamen
Materialien von [Kurstag 3](kurstag_03/README.md). Für Termine 5 und 6 gibt es
jetzt jeweils eigene Verzeichnisse mit eigenen Folien und Arbeitsheften:
[Kurstag 5](kurstag_05/README.md) · [Kurstag 6](kurstag_06/README.md). Auch
[Kurstag 7](kurstag_07/README.md) und [Kurstag 8](kurstag_08/README.md) haben
eigene Materialien und Startanleitungen.

## Werkzeuge

Der Kurs verwendet [uv](https://docs.astral.sh/uv/) für Python und Pakete sowie
[marimo](https://docs.marimo.io) als reaktives Notebook. Wenn marimo installiert
ist, startet `marimo run` die Folienpräsentation im Browser; `marimo edit` öffnet
das Notebook zum Bearbeiten und für Live-Coding. Die jeweilige README enthält
den passenden Befehl.

```sh
cd kurstag_01
marimo run kurstag_01_folien.py
```

Ohne installierte marimo-Version lässt sich derselbe Befehl einmalig mit uvx
ausführen: `uvx --from "marimo==0.25.2" marimo run kurstag_01_folien.py`.

Die ursprünglichen Dateien und Präsentationen bleiben in den Kursordnern als
Ausgangsmaterial erhalten. Die aufbereiteten Marimo-Dateien tragen die Endungen
`_folien.py` und `_teilnehmende.py`.
