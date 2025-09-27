"""
inainte sa rulez un program trebuie sa il compilez
in cpp compilarea se face pe tot programul => daca am o greseala nu pot sa rulez programul
in python compilarea se face linie cu linie => pot rula programul pana ajung la o greseala
- interpretor -> face compilarea in python(linie cu linie)
"""

"""
in c++ ca sa ramanem in scope-ul unui for/if/while fom folosi acolada {}
pythonul e putin mai special deoarece nu are nevoie de acolade -> ca sa ramai in scope-ul unei
instructiuni se foloseste indentarea

if 1 > 0:
 print("1 > 0")
   print("test")

-> codul de mai sus nu functioneaza deoarece indentarea printurilor nu este la fel => eroare

if 1 > 0:
 print("1 > 0")
 print("test")
 
-> indentare la fel => functioneaza corect
"""

#if, else, elif

n = int(input("Introdu un numar: "))

if n == 1:
    print("1")
else:
    print("nu este unu")
    

n = int(input("Introdu alt numar: "))

if n == 1:
    print("1")
elif n == 2:
    print("2")
else:
    print("nu este 1 sau 2")

# while si for

# **for**

"""
CPP
for(int i = 1; i <= 20; ++i) {
    instructiuni
}
"""

for i in range(20): #in python se face automat indexarea de la 0 si merge pana la target - 1 => forul nostru merge de la 0 la 19
    print(i)
    
for i in range(10, 20): # de la 10 la 19
    print(i)
    
for i in range(10, 20, 2): # de la 10 la 19 din 2 in 2
    print(i)
    
for i in range(20, 10, -1): # aici mergem invers de la 20 la 11  
    print(i)
    
"""
CPP:

while(conditie) {
    instructiuni
}
"""

while 1 > 0: #whileul se comporta la fel ca in cpp
    print("1 > 0")