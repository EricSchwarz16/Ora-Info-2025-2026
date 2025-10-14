# Functia pentru cautare in fereastra
def count_secvk_distincte(N, K, numere):
    frecventa = {}      # dictionar pentru frecventele din fereastra curenta
    distincte = 0
    total = 0

    for i in range(N):
        val = numere[i]
        # adaugam valoarea in fereastra
        if val in frecventa:
            frecventa[val] += 1
        
        else:
            frecventa[val] = 1
            distincte += 1
        # scoatem elementul care iese din fereastra
        if i >= K:
            iesire = numere[i - K]
            frecventa[iesire] -= 1
            if frecventa[iesire] == 0:
                del frecventa[iesire]
                distincte -= 1
        
        # verificam daca avem exact K elemente distincte
        if i >= K - 1 and distincte == K:
            total += 1
    
    return total




# Citim datele din fisier
with open("secv_fb.in", "r") as fin:
    linie1 = fin.readline().strip().split()
    N = int(linie1[0])
    K = int(linie1[1])
    linie2 = fin.readline().strip().split()
    numere = [int(x) for x in linie2]

# Calcul
rezultat = count_secvk_distincte(N, K, numere)

# Scriere in fisier
with open("secv_fb.out", "w") as fout:
    fout.write(str(rezultat))


