"""
Kirjoita ohjelma, joka kysyy käyttäjältä viiden kaupungin nimet yksi kerrallaan
(käytä for-toistorakennetta nimien kysymiseen) ja tallentaa ne listarakenteeseen.
Lopuksi ohjelma tulostaa kaupunkien nimet yksi kerrallaan allekkain samassa
järjestyksessä kuin ne syötettiin. käytä for-toistorakennetta nimien kysymiseen
ja for/in toistorakennetta niiden läpikäymiseen.
"""
kaupungit = []

for i in range(1, 6):
    kaupunki = input(f"Anna {i}. kaupungin nimi: ")
    kaupungit.append(kaupunki)

print("Kaupungit:")
for kaupunki in kaupungit:
    print(kaupunki)