"""
dam enter dupa fiecare
a = int(input())
b = int(input())
semn = input()
"""

line = input()

a, b = line.split(" ")
semn = input()

a = int(a)
b = int(b)

if a < b:
    aux = a
    a = b
    b = aux

if  semn == "*":
    print(a * b)
elif semn == "+":
    print(a + b)
elif semn == "-":
    print(a - b)
elif semn == "/":
    print(int(a / b))