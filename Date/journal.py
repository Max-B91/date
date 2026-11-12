import hashlib
import random
import time
from datetime import datetime, date


maintenant = datetime.now()
# date -> str -> bytes -> hasher
hash_maint = hashlib.sha256(str(maintenant).encode()).hexdigest()
print(hash_maint)
hash_maint = hashlib.sha256(str(maintenant).encode()).hexdigest()
print(hash_maint)   # même valeur = même hash

time.sleep(1)
maintenant = datetime.now()
# date -> str -> bytes -> hasher
hash_maint = hashlib.sha256(str(maintenant).encode()).hexdigest()
print(hash_maint)   # différence valeur de now() : hash différents

# TODO modifier la variable datetime pour créer un mot de passe valide une journée

# utiliser une variable datetime pour créer un mot de passe valide une journée
password = input("Entrez votre mot de passe : ")
temps = datetime.now().strftime("%d/%m/%Y")
hash_password = hashlib.sha256((password + temps).encode()).hexdigest()
print(hash_password)
time.sleep(1)
password_connexion = input("Entrez votre mot de passe pour vous connecter : ")
temps = datetime.now().strftime("%d/%m/%Y")
hash_password_connexion = hashlib.sha256((password_connexion + temps).encode()).hexdigest()
print(hash_password_connexion)

date2 = datetime(2026, 11, 13).strftime("%d/%m/%Y")
hash_password_demain = hashlib.sha256((password_connexion + date2).encode()).hexdigest()
print(hash_password_demain)