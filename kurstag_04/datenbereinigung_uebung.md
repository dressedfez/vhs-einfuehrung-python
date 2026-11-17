# Ergänzung für Termin 6: Fehlende Werte untersuchen

Die Übung verwendet bewusst eine kleine Tabelle, in der Werte fehlen. So können die Teilnehmenden jeden Schritt nachvollziehen. Anschließend lassen sich die Methoden auf die Verkaufsdaten übertragen.

```python
import pandas as pd

bestellungen = pd.DataFrame({
    "Region": ["Dresden", "Leipzig", None, "Dresden", "Leipzig"],
    "Produkt": ["Buch", "Stift", "Buch", "Stift", "Buch"],
    "Menge": [2, 3, 1, None, 2],
    "Preis": [12.0, 2.5, 12.0, 2.5, 12.0],
})
```

## Aufgaben

1. Zeige mit `isna().sum()`, wie viele Werte je Spalte fehlen. Welche zwei Spalten sind betroffen?
2. Erstelle mit `dropna(subset=["Menge"])` eine neue Tabelle ohne Zeilen, deren Menge fehlt. Wie viele Zeilen bleiben?
3. Ersetze in einer **Kopie** die fehlende Region durch `"Unbekannt"`. Kontrolliere anschließend die Spalte mit `value_counts()`.
4. Berechne in der Tabelle aus Aufgabe 2 die Spalte `Umsatz` als `Menge * Preis`. Gruppiere den Umsatz nach `Produkt`.
5. Besprecht: Warum wäre es problematisch, die fehlende Menge ohne weitere Information durch `0` zu ersetzen?

## Hinweise für die Besprechung

Fehlende Werte bedeuten zunächst, dass die Information unbekannt ist. Welche Behandlung sinnvoll ist, hängt von der Fragestellung und vom Grund des Fehlens ab. `dropna` entfernt Daten; `fillna` ergänzt einen gewählten Ersatzwert. Beide Schritte sollten bewusst erfolgen und dokumentiert werden.

Für Aufgabe 4 ergeben sich 60 Euro Umsatz für Bücher und 7,50 Euro für Stifte. Die Zeile mit unbekannter Region kann dafür berücksichtigt werden, weil Menge und Preis vorhanden sind.
