from repository import Repository, TxtRepository
from model import Medicine

class Service:
    def __init__(self):
        self.repo = TxtRepository("medicine.txt")
        self.undoRedoService = UndoRedoService()
    
    def getAllMedicines(self) ->  list[Medicine]:
        return self.repo.getAllMedicine()
    
    def addMedicine(self, a: Medicine):
        self.undoRedoService.addToUndoStack("add", self.repo.getAllMedicine())
        self.repo.addMedicine(a)

    def deleteMedicine(self, a: Medicine):
        self.repo.deleteMedicine(a)
    
    def updateMedicine(self, name: str, a : Medicine):
        self.repo.updateMedicine(name, a)
    
    def Undo(self):
        pass
    
    def Redo(self):
        pass
    
    def getMedicinesWithAPriceLowerThan(self, price):
        medicineList = self.repo.getAllMedicine()
        resultList = []
        for medicine in medicineList:
            if medicine.price < int(price):
                resultList.append(medicine)
        
        return resultList
    
class UndoRedoService:
    def __init__(self):
        self.undoStack = []
        self.redoStack = []
    
    def undo(self):
        #operatia, elementul | sau tot array-ul
        pass

    def redo(self):
        pass

    def addToUndoStack(self, operationName, currentState):
        pass
    
    def addToRedoStack(self, operationName, currentState):
        pass