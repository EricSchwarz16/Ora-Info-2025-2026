def sum_cif(x):
    sum = 0
    while x:
        sum = sum + x % 10
        x = int(x / 10)
    
    return sum

n = int(input())

min = max = 0
sum_min = 91
sum_max = 1


for i in range(n):
    x = int(input())
    sum = sum_cif(x)

    if sum < sum_min:
        sum_min = sum
        min = x
    
    if sum > sum_max:
        sum_max = sum
        max = x

print(min)
print(max)
 
