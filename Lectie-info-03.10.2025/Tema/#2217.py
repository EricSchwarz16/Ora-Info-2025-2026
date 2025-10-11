n = int(input())
sir = []
A = {}
rezultat = []

for i in range(n):
    sir.append(int(input()))

for elem in sir:
    if elem in A:
        A[elem] += 1
    
    else:
        A[elem] = 1
    
    rezultat.append(A[elem])

print(*rezultat)