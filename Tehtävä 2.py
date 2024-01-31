"""
Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka,
kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
Lopuksi ohjelma tulostaa saaduista luvuista viisi suurinta suuruusjärjestyksessä
suurimmasta alkaen. Vihje: listan alkioiden lajittelujärjestyksen voi kääntää
antamalla sort-metodille argumentiksi reverse=True.
"""
luvut = []

while True:
    luku = input("Anna luku (Enter lopettaa ohjelman):\n")
    if luku == "":
        print("Ohjelma loppuu.")
        break
    if luku != "":
        luvut.append(int(luku))

luvut.sort(reverse=True)
for i in range(5):
    print(luvut[i])