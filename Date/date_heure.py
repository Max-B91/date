from datetime import datetime, timedelta
import locale
import random

maintenant = datetime.now()
print(maintenant.year)
print(maintenant.month)
print(maintenant.day)
print(maintenant.strftime("%d/%m/%Y"))
print(maintenant.strftime("%B %d %Y %I:%M %p"))

locale.setlocale(locale.LC_ALL, "fr_CA.utf8") # Travailler en français

print(maintenant.strftime("%d %B %Y %I:%M %p")) # date -> str

date1 = datetime(200, 12, 25)
print(date1.date())
str_date = input("Entrer la date ex: 28/02/2026 ")
date2 = datetime.strptime(str_date, "%d/%m/%Y") # str -> date
print(date2.date())

# TODO Générer une heure aléatoire entre 0 h et 23 h, utiliser une variable de type datetime
# afficher l'heure, ex 17h42 et afficher si c'est le matin, l'après-midi, le soir ou la nuit.

heure = random.randint(0, 23)
minute = random.randint(0, 23)

heure_minute = datetime.strptime(str(heure) + "h" + str(minute), "%Hh%M")

print(heure_minute.strftime("%Hh%M"))

if heure_minute.hour < 12:
    print("Matin")
elif heure_minute.hour < 18:
    print("Après-midi")
elif heure_minute.hour < 20:
    print("Soir")
else:
    print("Nuit")


