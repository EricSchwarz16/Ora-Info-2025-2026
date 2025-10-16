"""
    avem o biblioteca unde trebuie sa tinem contabilitatea cartilor
    
    carte: nume
            autor
            pret
            editura

    operatii pe care le putem face
    - adaugam o carte
    - stergem o carte dupa nume
    - updatam autor/pret/editura unei carti daca am numele ei
    - afisam toate cartile din biblioteca
    
    !!! nu avem voie sa folosim variabile globale!!!!!!
"""

class Book:
    def __init__(self,nume, autor, pret, editura):
        self.nume = nume
        self.autor = autor
        self.pret = pret
        self.editura = editura

# Nu putem sa avem 2 carti cu acelasi nume
# Daca avem 2 carti cu acelasi nume, functia nu face nimic
def addBook(nume: str, autor : str, pret : int, editura : str, bookLibrary: list):
    bookToBeAdded = Book(nume, autor, pret, editura)
    for carte in bookLibrary:
        if carte.nume == bookToBeAdded.nume:
            return 
    
    bookLibrary.append(bookToBeAdded)

def deleteBookByIndex(index: int, bookLibrary: list):
    if 0 <= index < len(bookLibrary):
        del bookLibrary[index]
    else:
        print("Index invalid! Nu exista carte cu acest indice.")


def updateBookByIndex(index: int, autor: str, pret: int, editura: str, bookLibrary: list):
    if 0 <= index < len(bookLibrary):
        bookLibrary[index].autor = autor
        bookLibrary[index].pret = pret
        bookLibrary[index].editura = editura
    else:
        print("Index invalid! Nu exista carte cu acest indice.")


def printBooks(bookLibrary):
    for carte in bookLibrary:
        print(f"{carte.nume} {carte.autor} {carte.pret} {carte.editura}")

if __name__ == "__main__":
    bookLibrary = [] #tinem minte toate cartile si lucram pe acest vector
    
    while True:
        print("""
Alege operatia dorita:
1: Adauga carte
2: Update carte
3: Delete carte
4: Afiseaza toate cartile
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
        
        else:
            printBooks(bookLibrary)


