n = int(input())
Frecv = {}

for i in range(n):
    x = int(input())
    if x in Frecv.keys():
        Frecv[x] += 1
    
    else:
        Frecv[x] = 1

# Căutăm minimul dintre valorile care apar o singură dată

minim = float('inf')
for val in Frecv:
    if Frecv[val] == 1 and val < minim:
        minim = val

print(minim)


