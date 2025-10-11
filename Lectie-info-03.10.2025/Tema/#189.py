def este_munte(numar):
    cifre = [int(c) for c in str(numar)]
    n = len(cifre)

    if n < 3:
        return 0  # Trebuie minim 3 cifre pentru a avea o creștere și o scădere

    i = 0

    # Creștere strictă
    while i + 1 < n and cifre[i] < cifre[i + 1]:
        i += 1

    # Dacă nu am avut nicio creștere sau suntem la capăt => nu e munte
    if i == 0 or i == n - 1:
        return 0

    # Scădere strictă
    while i + 1 < n and cifre[i] > cifre[i + 1]:
        i += 1

    # Dacă am ajuns la final, numărul e munte
    return 1 if i == n - 1 else 0


# Citire de la tastatură
n = int(input())
sir = []

for i in range(n):
    sir.append(int(input()))

for numar in sir:
    print(este_munte(numar))
