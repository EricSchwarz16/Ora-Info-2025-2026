n = int(input())
A = []
B = []
for i in range (n):
    A.append(int(input()))

m = int(input())
for i in range(m):
    B.append(int(input()))

i = j = 0
C = []

while i < n and j < m:
    if A[i] < B[j]:
        C.append(A[i])
        i += 1
    
    else:
        C.append(B[j])
        j += 1

while i < n:
    C.append(A[i])
    i += 1

while j < m:
    C.append(B[j])
    j += 1

for i in range (len(C)):
    print(C[i], end = " ")
    if i > 0 and i % 10 == 0:
        print('\n')
        