# Functie pentru cmmdc (algoritmul lui Euclid)
def cmmdc(a, b):
    while b != 0:
        a, b = b, a % b
    
    return a

# Functie pentru a verifica daca un numar este prim
def este_prim(x):
    if x < 2:
        return False
    
    elif x % 2 == 0:
        return False
    
    elif x == 2:
        return False

    div = 3
    while div * div <= x:
        if x % div == 0:
            return False
        
        div += 2
    
    return True

# Citim datele din fisier
strazi = []
with open("nyk.in", "r") as fin:
    n = int(fin.readline())         # numarul de strazi
    for i in range(n):
        linie = fin.readline().strip().split()
        m = int(linie[0])
        inaltimi = []
        for j in range(1, m + 1):
            inaltimi.append(int(linie[j]))
        strazi.append(inaltimi)

# Variabile pentru rezultat
cmmdc_max = 0
poz_strada = -1
poz_inaltime = -1
inaltime_max_prima = -1

#Parcurgem fiecare strada
for i in range(len(strazi)):
    cladirile = strazi[i]

    # calculam cmmdc-ul local
    cmmdc_local = cladirile[0]
    for j in range(1, len(cladirile)):
        cmmdc_local = cmmdc(cmmdc_local, cladirile[j])
    
    # cautam cea mai mare inaltime prima locala
    inaltime_prima_max = -1
    poz = -1

    for j in range(len(cladirile)):
        if este_prim(cladirile[j]):
            if(cladirile[j] >= inaltime_prima_max):
                inaltime_prima_max = cladirile[j]
                poz = j + 1     # 1-indexata
    
    # alegem strada cea mai buna
    if cmmdc_local > cmmdc_max:
        cmmdc_max = cmmdc_local
        poz_strada = i + 1
        inaltime_max_prima = inaltime_prima_max
        poz_inaltime = poz
    
    elif cmmdc_local == cmmdc_max and i + 1 > poz_strada:
        poz_strada = i + 1
        inaltime_max_prima = inaltime_prima_max
        poz_inaltime = poz
    
    # scriem rezultatul in fisierul de iesire
    with open("nyk.out", "w") as fout:
        if inaltime_max_prima == -1:
            fout.write(("Nu am gasit casa!"))

        else:
            fout.write(f"{poz_strada} {poz_inaltime}\n")
            fout.write(f"{inaltime_max_prima}")
    
    


