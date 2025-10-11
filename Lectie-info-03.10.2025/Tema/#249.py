X = int(input())
n = int(input())
A = []

for i in range(n):
    A.append(int(input()))

A.sort()
if X in A:
    print(A.index(X) + 1)

else:
    print("NU EXISTA")