# Kurstag 6 · Maschinelles Lernen mit Scikit-Learn

Für Kurstag 6 gibt es zwei aufbereitete Marimo-Notebooks:

| Datei | Für wen? | Inhalt |
| --- | --- | --- |
| [kurstag_06_folien.py](kurstag_06_folien.py) | Dozent / gemeinsamer Unterricht | Folien mit Beispielen, Trainingsablauf, Modellbewertung und Ziffernfoto-Demo |
| [kurstag_06_teilnehmende.py](kurstag_06_teilnehmende.py) | Teilnehmende / Nacharbeiten | Arbeitsheft mit ausführbaren Beispielen, vier Basisübungen und automatischer Rückmeldung |

Das ursprüngliche Notebook [kurstag_06.py](kurstag_06.py) sowie die Keynote- und PDF-Dateien bleiben als Ausgangsmaterial erhalten. Die neuen Notebooks verwenden den eingebauten Digits-Datensatz von Scikit-Learn und benötigen keinen Datendownload.

## Folien starten

Alle Befehle im Ordner `kurstag_06` ausführen. Voraussetzung ist eine installierte Version von [uv](https://docs.astral.sh/).

Präsentation starten:

```sh
uv run --script kurstag_06_folien.py
```

Für Live-Coding und die Folienansicht:

```sh
uvx --from "marimo==0.25.2" marimo edit --sandbox kurstag_06_folien.py
```

Der Sandbox-Modus bereitet eine getrennte Umgebung aus den Abhängigkeiten im Notebook-Kopf vor. Ohne ihn nutzt Marimo die Python-Umgebung, in der das Programm installiert wurde. Die Datei `layouts/kurstag_06_folien.slides.json` aktiviert das Folienlayout. Mit den Pfeiltasten blättern; **C** blendet den Code der aktuellen Folie ein.

## Arbeitsheft für Teilnehmende

```sh
uvx --from "marimo==0.25.2" marimo edit --sandbox kurstag_06_teilnehmende.py
```

Codezellen mit **Shift+Enter** ausführen. Die Übungen behandeln Modelltraining mit einer Pipeline, Vorhersagen, Accuracy und die Confusion Matrix. Im Zusatzteil können Teilnehmende ein eigenes Ziffernfoto hochladen. Auswahlfelder, Vorhersage und verarbeitetes Bild erscheinen gemeinsam auf derselben Notebook-Seite.

## HTML zum Weitergeben

```sh
uvx --from "marimo==0.25.2" marimo export html kurstag_06_folien.py -o kurstag_06_folien.html
uvx --from "marimo==0.25.2" marimo export html kurstag_06_teilnehmende.py -o kurstag_06_teilnehmende.html
```

Der statische Export enthält Texte und berechnete Beispiele. Für den Foto-Upload und das erneute Ausführen von Python die laufende Marimo-Anwendung verwenden.
