import random

# random alege un numar random/ alege random dintr-un array etc.
# in general implementeaza operatii de random :D

"""
titlu -> string
autor -> string
editura -> string
pret -> numar
"""

#alege un numar random in intervalul [a,b] -> [0,100] in cazul nostru
print(random.randint(0, 100))

titluri_random = ["test", "test1", "Harap", "Negru", "Alb", "Alice", "Minune", "Tara", "PbInfo", "Tastatura", "Hey", "trt"] # 6 * 13

print(random.choice(titluri_random) + " " + random.choice(titluri_random))


editura_random = ["Arthur", "Gazeta Matematica", "Humanitas"]

autor_random = ["Andrei", "Mihai"]

print(random.choice(titluri_random) + " " + random.choice(titluri_random))
