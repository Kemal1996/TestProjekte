auswahl = input('Bitte gebe 1 für Pfannkuchen, 2 für Waffeln oder 3 für Käsekuchen ein: ')
portions = input('Bitte gebe die Anzahl der benötigen Portionen an: ')

if auswahl == "1":
    for x in [str(int(portions) * 0.5) +" Eier ", str(int(portions) * 0.5 * 100) + "g Mehl", str(int(portions) * 0.5 * 100) + "ml Milch"]:
        print(x)
elif auswahl == "2":
    for x in [str(int(portions) * 2.5) +" Eier ", str(int(portions) * 2.5 * 100) + "g Mehl", str(int(portions) * 2.5 * 100) + "ml Milch"]:
        print(x)
elif auswahl == "3":
    for x in [str(int(portions) * 6) +" Eier ", str(int(portions) * 6 * 100) + "g Mehl", str(int(portions) * 6 * 100) + "ml Milch"]:
        print(x)
else:
    print('Bitte nur die Zahlen 1 für Pfannkuchen, 2 für Waffeln oder 3 für Käsekuchen verwenden!')

input('Bitte beliebige Taste drücken...')
