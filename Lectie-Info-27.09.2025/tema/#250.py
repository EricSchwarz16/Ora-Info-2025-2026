n = int(input())
A = []

for i in range(n):
    A.append(int(input()))

m = int(input())
B = []
for i in range(m):
    B.append(int(input()))

i = j = 0
C = []
while(i < n and j < m):
    if A[i] < B[j]:
        if len(C) == 0 or C[-1] != A[i]:
            C.append(A[i])
            i += 1
        
        else:
            i += 1
        
    else:
        if len(C) == 0 or C[-1] != B[j]:
            C.append(B[j])
            j += 1
        
        else:
            j += 1

while i < n:
    if len(C) == 0 or C[-1] != A[i]:
        C.append(A[i])
        i += 1
    
    else:
        i += 1

while j < m:
    if len(C) == 0 or C[-1] != B[j]:
        C.append(B[j])
        j += 1
    
    else:
        j += 1

for i in range(len(C)):
    print(C[i], end = " ")
    if i != 0 and i % 9 == 0:
        print('\n')


