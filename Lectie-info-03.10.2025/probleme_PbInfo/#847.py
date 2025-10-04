prop = input()


#1 Separarea fiecarui cuvant

lista_cuv = sorted(prop.split(" "))
#2 Numararea fiecarui cuvant in parte asemanator vector frecv (dict)

ord_cuv = {}
for cuv in lista_cuv:
    if cuv in ord_cuv.keys():
        ord_cuv[cuv] += 1
    
    else:
        ord_cuv[cuv] = 1

     
#3 Ordonare lexicografica si afisare cheie si valoare

print(ord_cuv)