stundenlohn = input('Bitte gebe deinen Stundenlohn ein: ')
tag = 8 * int(stundenlohn)
monat = 20 * tag
jahr =  12 * monat

print('Dein Stundenlohn beträgt '+ str(stundenlohn) + '€.')
print('Du verdienst ' + str(tag) + '€ pro Tag.')
print('Du verdienst ' + str(monat) + '€ pro Monat.')
print('Du hast ein Jahresgehalt von ' +str(jahr) + '€.')

input('Drücke eine beliebige Taste...')