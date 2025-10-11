"""
    avem o biblioteca unde trebuie sa tinem contabilitatea cartilor
    
    carte:  nume
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
    def __init__(self, nume, autor, pret, editura):
        self.nume = nume
        self.autor = autor
        self.pret = pret
        self.editura = editura

def addBook(name: str, autor : str, pret : int, editura : str, bookLibrary):
    return

def deleteBook(name: str, bookLibrary):
    return

def updateBook(name: str, autor : str, pret : int, editura : str, bookLibrary):
    return

def printBooks(bookLibrary):
    return

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