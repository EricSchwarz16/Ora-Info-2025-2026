from models import Book #din fisierul models importa clasa book
#import models #dau import la toate lucrurile din acel fisier

def generate_Books(bookLibrary, nr_carti_generate):
    import random
    nume_random = ['Book1', 'Book2', 'Book3', 'Book4', 'Book5', 'Jurnal', 'Revista', 'Atlas', 'Ghid', 'Comic', 'Fabula', 'Cronica', 'Manual de instructiuni', 'Dosar penal', 'Caiet pentru scoala']
    autor_random = ['Eric1', 'Eric2', 'Eric_junior', 'Eric_senior', 'Eric_sef']
    editura_random = ['Arthur', 'Humanitas', 'Veritas']
    
    for i in range(nr_carti_generate):
        nume = random.choice(nume_random) + ' ' + random.choice(nume_random)
        autor = random.choice(autor_random)
        pret =  random.randint(1, 100)
        editura = random.choice(editura_random)

        addBook(nume, autor, pret, editura, bookLibrary)       

# Nu putem sa avem 2 carti cu acelasi nume
# Daca avem 2 carti cu acelasi nume, functia nu face nimic
def addBook(nume: str, autor : str, pret : int, editura : str, bookLibrary: list):
    # bookToBeAdded = models.Book(nume, autor, pret, editura) cand dau import la toate lucrurile din acel fisier
    bookToBeAdded = Book(nume, autor, pret, editura) # cand din fisierul models importa clasa book
    
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

def afisare_dupa_pret(bookLibrary: list):
    dict = {}

    for carte in bookLibrary:
        if carte.pret not in dict.keys():
            dict[carte.pret] = [carte]
        
        else:
            dict[carte.pret].append(carte)
    
    for pret in sorted(dict.keys()):
        print(f'{pret}: ', end = ' ')
        for carte in dict[pret]:            # revenim la sorted(dict[pret]) cand avansam in clase in python !!!
            print(carte.nume, end = ' | ')

        print()    

def printBooks(bookLibrary):
    for carte in bookLibrary:
        print(f"{carte.nume} {carte.autor} {carte.pret} {carte.editura}")