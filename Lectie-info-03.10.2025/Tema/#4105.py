n = int(input())
D = {}

def nr_div(x):
    cnt = 0
    d = 1
    while d * d <= x:
        if x % d == 0:
            cnt += 1
            if x / d != d:
                cnt += 1
        
        d += 1
    
    return cnt
        
    

for i in range(n):
    x = int(input())
    D[x] = nr_div(x)

ans = 0
for i in D:
    keys = list(D.keys())
    index = keys.index(i)
    
    for j in keys[index+1:]:
        if D[i] == D[j]:
            ans += 1


print(ans)



