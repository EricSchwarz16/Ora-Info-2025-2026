from model import Medicine

#tine minte in memorie
class Repository:
    def __init__(self):
        self.medicineList = []
        self.loadData()
    
    def addMedicine(self, a: Medicine):
        self.medicineList.append(a)
        
        self.saveData()
        
    def saveMedicineList(self, newMedicineList : list[Medicine]):
        self.medicineList = newMedicineList
        
        self.saveData()
    
    def deleteMedicine(self, name : str): 
        for m in self.medicineList:
            if m.name == name:
                self.medicineList.remove(m)

        self.saveData()
    
    def updateMedicine(self, name: str, newMedicine : Medicine): 
        for i, m in enumerate(self.medicineList):
            if m.name == name:
                self.medicineList[i] = newMedicine
                break

        self.saveData()
    
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
        pass
        #with open(self.file, "w") as f:
        #   for medicine in self.medicineList:
        #      f.write(str(medicine))
        #     f.write("\n")

#Repository pentru CSV -> exista si aici, dar poti usor si de mana

#Repository pentru fisier JSON -> exista librarie care sa parseze direct


