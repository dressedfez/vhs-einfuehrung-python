# Aufgabe 3: Benutzereingabe mit Schleife
# Schreiben Sie ein Python-Programm, das den Benutzer auffordert, eine Zahl einzugeben.
# Das Programm soll die eingegebene Zahl anzeigen und den Benutzer erneut zur Eingabe auffordern,
# bis der Benutzer die Zahl 0 eingibt.
# Wenn der Benutzer eine negative Zahl eingibt, soll eine Fehlermeldung
# angezeigt werden und der Benutzer erneut zur Eingabe aufgefordert werden.
# Sobald der Benutzer die Zahl 0 eingibt, soll eine Dankesnachricht ausgegeben werden und das Programm beendet werden.

condition = True
while condition:
    eingabe = int(input("Geben Sie eine Zahl ein (0 zum Beenden): "))
    if eingabe == 0:
        condition = False
    elif eingabe < 0:
        print("Bitte eine positive Zahl eingeben.")
    else:
        print(f"Die eingegebene Zahl ist: {eingabe}")
else:
    print("Danke für die Eingabe!")
