"""
Kirjoita ohjelma, joka kysyy käyttäjältä kokonaisluvun ja ilmoittaa, onko se alkuluku.
Tässä tehtävässä alkulukuja ovat luvut, jotka ovat jaollisia vain ykkösellä ja itsellään.

Esimerkiksi luku 13 on alkuluku, koska se voidaan jakaa vain luvuilla 1 ja 13 siten, että jako menee tasan.
Toisaalta esimerkiksi luku 21 ei ole alkuluku, koska se voidaan jakaa tasan myös luvulla 3 tai luvulla 7.
"""
luvut = []
luku = luvut.append(int(input("Syötä kokonaisuluku: ")))

for luku in luvut:
    if luku < 2:
        print(f"{luku} ei ole alkuluku.")
    else:
        alkuluku = True
        jakaja = 2
        while jakaja < luku:
            if (luku % jakaja == 0) and (luku % 1 == 0) and (luku % luku == 0):
                alkuluku = False
                break
            jakaja += 1

        if alkuluku:
            print(f"{luku} on alkuluku.")
        else:
            print(f"{luku} ei ole alkuluku.")