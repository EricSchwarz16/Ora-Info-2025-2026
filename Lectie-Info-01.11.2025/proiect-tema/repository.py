from model import Medicine

class Repository:
    def __init__(self):
        self.medicineList = []
    
    def addMecicine(self, a: Medicine):
        self.medicineList.append(a)
    
    def deleteMedicine(self, a : Medicine): #implementeza overload la === pentru a putea face comparatii directe nu pe medicine.field
        pass
    
    def updateMedicine(self, name: str, newMedicine : Medicine): #implementeza overload la === pentru a putea face comparatii directe nu pe medicine.field
        pass
    
    def getAllMedicine(self) -> list[Medicine]:
        return self.medicineList