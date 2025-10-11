"""
    avem o biblioteca unde trebuie sa tinem contabilitatea cartilor
    
    carte: name
            autor
            pret
            editura

    operatii pe care le putem face
    - adaugam o carte
    - stergem o carte dupaname
    - updatam autor/pret/editura unei carti daca am numele ei
    - afisam toate cartile din biblioteca
    
    !!! nu avem voie sa folosim variabile globale!!!!!!
"""

class Book:
    def __init__(self,name, autor, pret, editura):
        self.name = name
        self.autor = autor
        self.pret = pret
        self.editura = editura

# Nu putem sa avem 2 carti cu acelasiname
# Daca avem 2 carti cu acelasiname, functia nu face nimic
def addBook(name: str, autor : str, pret : int, editura : str, bookLibrary: list):
    bookToBeAdded = Book(name, autor, pret, editura)
    for carte in bookLibrary:
        if carte.name == bookToBeAdded.name:
            return 
    
    bookLibrary.append(bookToBeAdded)

def deleteBook(name: str, bookLibrary):
    return

def updateBook(name: str, autor : str, pret : int, editura : str, bookLibrary):
    return

def printBooks(bookLibrary):
    for carte in bookLibrary:
        print(f"{carte.name} {carte.autor} {carte.pret} {carte.editura}")

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
            name = input("Alege numele: ")
            autor = input("Alege autorul: ")
            pret = int(input("Alege pretul: "))
            editura = input("Alege editura: ")
            addBook(name, autor, pret, editura, bookLibrary)
        
        elif op == 4:
            printBooks(bookLibrary)


