class Animal:
    def __init__(self, nume: str, picioare: int, maini : int, kg: int):
        self._picioare = picioare
        self._maini = maini # _ -> protected -> se foloseste doar in clasa parinte si in mosteniri (mai mult conceptual deoarece in py se poate folosi peste tot din pacate)
        self._kg = kg # private -> nu ar trebui accesat decat aici
        self._nume = nume
        
    def sound(self):
        print("Un sunet de animal")
    
    
counter = 0
counter_german = 0

#Inheritance -> mostenire
class Caine(Animal):
    def alergare(self):
        print("Sunt un caine si alerg")
        
    def sound(self):
        global counter
        
        if counter == 0:
            print("Ham")
        else:
            super().sound() #cu super accesez clasa parinte
            
        counter += 1
        
class CiobanescGerman(Caine):
    def alergare(self):
        print("Sunt un ciobanesc german si alerg")
        
    def sound(self):
        global counter
        
        if counter == 0:
            print("Ham Ciobanesc")
        else:
            super().sound() #cu super accesez clasa parinte -> Caine
    


a = Caine("Azor", 4, 0, 45)
b = CiobanescGerman("g", 4, 0, 2)

a.sound()
a.sound()
b.sound()



class Biblioteca:
    #encapsulation -> incapsulare
    def __init__(self, nume):
        self.__nume = nume # privat
    
    def __loadCarti(self) -> str: # __ -> este privata
        pass
        
    def afisareCarti(self):
        self.__loadCarti() #permis
        
    def TradeStrategyX(self):
        pass


b = Biblioteca("Andrei")

