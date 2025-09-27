cnt = 0
while True:
    n = int(input())
    if n == 0:
       break
    if n % 2 == 0 :
        cnt += 1

if cnt == 0:
    print("NU EXISTA")

else:
    print(cnt)
