# Deschidem fișierul de intrare
with open("file.txt", "r") as fin:
    # Citim toate numerele ca un șir de caractere și le împărțim în lista de stringuri
    numere = fin.read().split()

# Convertim toate elementele în întregi și numărăm aparițiile
aparitii = [0] * 10  # Pentru cifrele de la 0 la 9

for nr in numere:
    cifra = int(nr)
    aparitii[cifra] += 1

# Numerele prime din intervalul [0, 9]
prime = [2, 3, 5, 7]

# Căutăm cel mai mare număr prim și numărul său de apariții
maxim_prim = -1
nr_aparitii = 0

for p in reversed(prime):  # Parcurgem de la cel mai mare la cel mai mic
    if aparitii[p] > 0:
        maxim_prim = p
        nr_aparitii = aparitii[p]
        break  # Găsim primul prim cel mai mare cu aparițiile lui

# Scriem rezultatul în fișierul de ieșire
with open("file2.txt", "w") as fout:
    fout.write(f"{maxim_prim} {nr_aparitii}")
