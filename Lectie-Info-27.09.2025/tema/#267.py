n = int(input())
A = {}
unice = []
for i in range(n):
    x = int(input())
    if x in A.keys():
        A[x] += 1

    else:
        A[x] = 1

for key in A:
    if A[key] == 1:
       unice.append(key)

unice.sort()

for element in unice:
    print(element, end = " ")


    




