n = int(input())
m = int(input())
x = n * m

"""
while x >= m:
    print(x)
    x = x - m
"""

for i in range (n * m, m - 1, - m):
        print(i)