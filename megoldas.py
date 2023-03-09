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
def volt_kevesebb_mint_5_hianyzas(hianyzasok):
    """Megvizsgálja, hogy volt-e ötnél kevesebb hiányzás."""
    hianyzas_db = 0
    for hianyzas in hianyzasok:
        if hianyzas < 0:
            raise ValueError("Hibás adat: negatív szám a hiányzások között.")
        if hianyzas > 0:
            hianyzas_db += 1
    return hianyzas_db <= 5

hianyzasok = [0, 0, 1, 0, 0, 0, 3, 2, 0, 0, 0, 0, 0, 0]
if volt_kevesebb_mint_5_hianyzas(hianyzasok):
    print("Volt ötnél kevesebb hiányzás.")
else:
    print("Legalább öt hiányzás volt.")

# 5. Hányadik héten volt egyetlen hiányzás?
hiányzások = [0, 1, 2, 0, 1, 0, 0, 3, 0, 1, 0, 0, 2, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# Hányadik héten volt egyetlen hiányzás?
for het, hiányzás in enumerate(hiányzások, 1):
    if hiányzás == 1:
        print(f"A(z) {het}. héten volt egyetlen hiányzás.")
        break
else:
    print("Nem volt egyetlen hiányzás sem az adatok között.")





# 4. Melyik héten volt a legtöbb hiányzás?
max_hianyzas = 0
het = 0

for i in range(len(hianyzasok)):
    hianyzas = sum(hianyzasok[i])
    if hianyzas > max_hianyzas:
        max_hianyzas = hianyzas
        het = i + 1
print(f"4. feladat: A legtöbb hiányzás a {het}. héten volt ({max_hianyzas})")