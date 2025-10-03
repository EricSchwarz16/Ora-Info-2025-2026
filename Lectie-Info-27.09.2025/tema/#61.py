a = int(input())
b = int(input())

while a:
    r = b % a
    b = a
    a = r       # am calculat cmmdc care este salvat in b

for d in range(1, b + 1, 1):
    if b % d == 0:
        print(d, end = " ")



