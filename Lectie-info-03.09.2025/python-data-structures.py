# what is a data-structure?

"""
Este o modalitate de a stoca si organiza datele 
-> de obicei se opteaza pentru cele mai eficiente modalitati de stocare
"""

"""
coada -> structura de date
stiva -> structura de date
vector -> o structura de date
"""

#list

lista_numere = [1 , 3, 4, 5]

print(lista_numere)

lista_numere.append(32)

print(lista_numere)

lista_numere.remove(3) # erase la prima aparitie a valorii date ca parametru

print(lista_numere)

lista_numere.pop() # remove la ultimul element

print(lista_numere)

lista_numere.append("Eric") # in python pot tine mai multe type-uri intr-o lista spre deosebire de cpp

print(lista_numere)

lista_numere.append(["alta lista", 1, 2, 3]) # putem avea si lista in lista

print(lista_numere)

for element in lista_numere:
    print(element, end = " ")

print("")
# Slicing operator

print(lista_numere[1:4]) #vreau elementele de la 1 pana la 3
print(lista_numere[:4]) # vreau elementele pana la 4 (pe toate de la st la dr)

print(lista_numere[1:4:2]) #vreau elementele de la 1 pana la 3

print(lista_numere[::2]) #vreau din 2 in 2

# slicing operator -> (start:end:step) -> merge de la start pana la end - 1 cu step


# String

#un sir -> cea mai lunga secventa formata din consoane

def isVowel(litera) -> bool:
    if litera == 'a' or litera == 'e' or litera == 'i' or litera == 'o' or litera == 'u':
        return True
    return False

cuv : str = "facem probleme de pe pbinfo cu consoane nnnccs"

curr_length = 0
max_lenght = 0

for letter in cuv:
    if not isVowel(letter) and letter != ' ':
        curr_length += 1
    else:
        curr_length = 0
    
    max_lenght = max(max_lenght, curr_length)

print(max_lenght)

print(cuv.find("p", 7))

# dict -> map in cpp
"""
 tine minte perechi de tipul keie, valoare
 
 tinem minte pentru fiecare om varsta
 pentru fiecare animal kilogramele
 pentru fiecare om tipul de masina
"""

# exemplu cheie de tip string
# valoare de tip int/float -> ce merge la varsta
# key : val

age_dict = {"andrei": 20, 
            "3": ["lista mea", 3]}

print(age_dict["andrei"])
print(age_dict["3"])

# cand iteram se itereaza direct prin chei
for cheie in age_dict:
    print(age_dict[cheie]) # printeaza 20, ["lista mea", 3]
    
for index in range(3):
    #cheie = input("cheie: ")
    #valoare = input("valoare: ")
    
    #age_dict[cheie] = valoare
    continue
    
print(age_dict)

# daca vreau sa printez o valoare de la o cheie inexistenta -> eroare!!!!!
if 200 in age_dict.keys():
    print(age_dict[200])
    
# queue : FIFO: first in firs out

from queue import Queue

q = Queue()

q.put("a")
q.put("b")
q.put("c")
q.put("d")

print(q.get())
print(q.get())

# deque -> stiva -> LIFO: last in first out

stack = []

#push

stack.append("a")
stack.append("b")
stack.append("c")
stack.append("d")

#topul stivei
print(stack[-1])

# pop

print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())


# split pe stringuri
propozitie = input("Introdu stringul: ")
print(propozitie.split(" "))