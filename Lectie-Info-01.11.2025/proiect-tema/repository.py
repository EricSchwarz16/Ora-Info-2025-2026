from model import Medicine

#tine minte in memorie
class Repository:
    def __init__(self):
        self.medicineList = []
        self.loadData()
    
    def addMecicine(self, a: Medicine):
        self.medicineList.append(a)
        
        self.saveData()
        
    def saveMedicineList(newMedicineList : list[Medicine]):
        pass
    
    def deleteMedicine(self, a : Medicine): #implementeza overload la === pentru a putea face comparatii directe nu pe medicine.field
        #logica de delete
        
        self.saveData()
        pass
    
    def updateMedicine(self, name: str, newMedicine : Medicine): #implementeza overload la === pentru a putea face comparatii directe nu pe medicine.field
        #logica de update
        self.saveData()
        pass
    
    def getAllMedicine(self) -> list[Medicine]:
        return self.medicineList
    
    def loadData(self):
        pass

    def saveData(self):
        pass    

#tinem minte in fisier .txt
#Polymorfism -> un obiect poate avea mai multe forme
class TxtRepository(Repository):
    def __init__(self, file: str):
        self.file = file
        super().__init__()
        
    def loadData(self):
        with open(self.file) as file:
            for line in file:
                # name|concentration|quantity|price
                details = line.split("|")
                name = details[0]
                concentration = int(details[1])
                quantity = int(details[2])
                price = int(details[3])
                
                self.medicineList.append(Medicine(name, concentration, quantity, price))
        
    def saveData(self):
        with open(self.file, "w") as f:
            for medicine in self.medicineList:
                f.write(str(medicine))
                f.write("\n")

#Repository pentru CSV

#Repository pentru fisier JSON


