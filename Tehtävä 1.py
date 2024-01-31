"""
Kirjoita ohjelma, joka kysyy käyttäjältä arpakuutioiden lukumäärän.
Ohjelma heittää kerran kaikkia arpakuutioita ja tulostaa silmälukujen summan.
Käytä for-toistorakennetta.
"""
import random

noppien_lkm = int(input("Anna noppien määrä: "))
tulokset = []
heitot = 0
summa = 0

while heitot < noppien_lkm:
    heitto = random.randint(1, 6)
    tulokset.append(heitto)
    heitot += 1

for tulos in tulokset:
    summa += tulos

print(f"Noppien summa on {summa}")