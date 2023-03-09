#0. feladat. A hianyzasok.txt beolvasás a listában a listákba

hianyzasok = []
with open("./adatok/hianyzasok.txt", "r", encoding="utf-8") as fm:
    for sor in fm:
        segedlista = sor. strip(). split(",")
        # l = []
        # for szam in segedlista:
        #    l.append(int(szam))
        # hianyzasok.append(l) 
        hianyzasok.append(list(map(int, segedlista)))

print("a beolvasott mátrix: ")
print(hianyzasok)

# 1. Hány óra hiányzás volt összesen?
osszeg=0
for het in hianyzasok:
    osszeg+=sum(het)
print(f"1. feladat: {osszeg} óra hiányzás volt összesen")

# 3. Volt-e olyan hét, amikor ötnél kevesebb hiányzás volt
print(f"3. feladat: Volt olyan hét, amikor ötnél kevesebb hiányzó volt")
