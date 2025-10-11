n = int(input())

suma_totala = n * (n + 1) // 2
tinta = suma_totala // 2

grup1 = []
grup2 = []

suma_curenta = 0

# Adăugăm numere în grup1 de la n la 1, cât timp nu depășim tinta
for numar in range(n, 0, -1):
    if suma_curenta + numar <= tinta:
        grup1.append(numar)
        suma_curenta += numar
    else:
        grup2.append(numar)

# Afișăm grupurile
print(*grup1)
print(*grup2)

