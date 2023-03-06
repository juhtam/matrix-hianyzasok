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

print(hianyzasok)