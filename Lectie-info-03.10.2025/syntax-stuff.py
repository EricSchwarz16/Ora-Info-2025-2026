"""
- Slicing operator (after we look at lists)

- Ternary operator
- break/continue
- functions and type hints
"""

# cond if (if condition is true) else (if condition is false)

age = 20

#status = what if says if the condition is true
#else status = what the else block returns
status = "Adult" if age >= 20 else "Minor"

print(status)


# break/continue

cnt = 0

while True:
    cnt += 1
    
    # Iese din loop (poate iesi si din while si din for)
    if cnt == 3:
        break

cnt = 0

while cnt < 10:
    cnt += 1
    
    # Iese din loop (poate iesi si din while si din for)
    if cnt == 3:
        continue

    print(cnt)

# type hints
def computePriceAfterDiscount(val: float) -> float:
    # : type -> type checking pentru parametri
    # : type -> type checking pentru valoarea returnata
    return val * 0.8


print (computePriceAfterDiscount(10.2))