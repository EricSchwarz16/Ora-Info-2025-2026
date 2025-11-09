from repository import Repository, TxtRepository
from model import Medicine
from copy import deepcopy

class Service:
    def __init__(self):
        self.repo = TxtRepository("medicine.txt")
        self.undoRedoService = UndoRedoService()
    
    def getAllMedicines(self) ->  list[Medicine]:
        return self.repo.getAllMedicine()
    
    def addMedicine(self, a: Medicine):
        self.undoRedoService.addToUndoStack(deepcopy(self.repo.getAllMedicine()))
        self.repo.addMedicine(a)

    def deleteMedicine(self, a: Medicine):
        self.undoRedoService.addToUndoStack(deepcopy(self.repo.getAllMedicine()))
        self.repo.deleteMedicine(a)
    
    def updateMedicine(self, name: str, a : Medicine):
        self.undoRedoService.addToUndoStack(deepcopy(self.repo.getAllMedicine()))
        self.repo.updateMedicine(name, a)
    
    def Undo(self):
        listAfterUndo = self.undoRedoService.undo(deepcopy(self.repo.getAllMedicine()))
        self.repo.saveMedicineList(listAfterUndo)
        print(listAfterUndo)
        
    def Redo(self):
        self.repo.saveMedicineList(deepcopy(self.undoRedoService.redo(self.getAllMedicines())))
    
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
    
    def undo(self, stateBeforeUndo: list[Medicine]):
        #operatia, elementul | sau tot array-ul
        if not self.undoStack or len(self.undoStack) == 0:
            raise Exception("Stacul e gol")
        
        newState = deepcopy(self.undoStack[-1])
        self.undoStack.pop()
        self.addToRedoStack(stateBeforeUndo)
        
        return newState

    def redo(self, stateBeforeRedo: list[Medicine]):
        newState = deepcopy(self.redoStack[-1])
        self.redoStack.pop()
        self.addToRedoStack(stateBeforeRedo)
        
        return newState
        

    def addToUndoStack(self, currentState: list[Medicine]):
        self.undoStack.append(currentState)
        print(currentState)
    
    def addToRedoStack(self, currentState):
        self.redoStack.append(currentState)