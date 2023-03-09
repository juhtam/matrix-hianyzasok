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

# 2. Volt-e olyan hét, amikor nem volt hiányzó?
i = 0
while i < len(hianyzasok):
    if 0 not in hianyzasok[i]:
        van_hianyzo = True
    i += 1

if van_hianyzo:
    print("2. feladat: Nem volt olyan hét, amikor nem volt hiányzó.")
else:
    print("2. feladat: Volt olyan hét, amikor nem volt hiányzó")

# 3. Volt-e olyan hét, amikor ötnél kevesebb hiányzás volt



# 4. Melyik héten volt a legtöbb hiányzás?
max_hianyzas = 0
het = 0

for i in range(len(hianyzasok)):
    hianyzas = sum(hianyzasok[i])
    if hianyzas > max_hianyzas:
        max_hianyzas = hianyzas
        het = i + 1
print(f"4. feladat: A legtöbb hiányzás a {het}. héten volt ({max_hianyzas})")