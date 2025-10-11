#Citire date de la tastatură
n = int(input())
A = []

for i in range(n):
    A.append(int(input()))

#Găsim valorile unice și le sortăm
valori_distincte = sorted(set(A))  # set pentru unicitate, sort pentru rang

#Creăm un dicționar valoare → rang
rang = {valoare: i + 1 for i, valoare in enumerate(valori_distincte)}

#Construim vectorul b
B = [rang[x] for x in A]

# Afișăm rezultatul
print(*B)
