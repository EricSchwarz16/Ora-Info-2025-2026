#from utils import * #din fisierul utils importa tot -> nu trebuie sa specific utils.x/y/z
"""
import utils
from utils import generate_Books
from utils import addBook
"""
from utils import * # * -> tot

"""
    avem o biblioteca unde trebuie sa tinem contabilitatea cartilor
    
    carte: nume
            autor
            pret
            editura

    O sa avem o selectie de carti generate automat.
    
    operatii pe care le putem face
    - adaugam o carte
    - stergem o carte dupanume
    - updatam autor/pret/editura unei carti daca am numele ei
    - afisam toate cartile din biblioteca
    - Pentu fiecare pret afisam cartile care au pretul respectiv

    !!! nu avem voie sa folosim variabile globale!!!!!!
"""
    
if __name__ == "__main__":      #(?)
    bookLibrary = [] #tinem minte toate cartile si lucram pe acest vector

    generate_Books(bookLibrary, 100)


    while True:
        print("""
Alege operatia dorita:
1: Adauga carte
2: Update carte
3: Delete carte
4: Afiseaza toate cartile
5: Afisare dupa pret
            """)
        

        op = int(input())

        if op == 1:
            nume = input("Alege numele: ")
            autor = input("Alege autorul: ")
            pret = int(input("Alege pretul: "))
            editura = input("Alege editura: ")
            addBook(nume, autor, pret, editura, bookLibrary)
        
        elif op == 2:
            print("Cartile disponibile: ")
            for i, carte in enumerate(bookLibrary):
                print(f"{i + 1}: {carte.nume} {carte.autor} {carte.pret} {carte.editura}")
            index = int(input("Alege indicele cartii pe care vrei sa o actualizezi: "))
            autor = input("Noul autor: ")
            pret = int(input("Noul pret: "))
            editura = input("Noua editura: ")
            updateBookByIndex(index - 1, autor, pret, editura, bookLibrary)

        elif op == 3:
            print("Cartile disponibile:")
            for i, carte in enumerate(bookLibrary):
                print(f"{i + 1}: {carte.nume} {carte.autor} {carte.pret} {carte.editura}")
            index = int(input("Alege indicele cartii pe care vrei sa o stergi: "))
            deleteBookByIndex(index - 1, bookLibrary)
        
        elif op == 4:
            printBooks(bookLibrary)
        
        else:
            afisare_dupa_pret(bookLibrary)


