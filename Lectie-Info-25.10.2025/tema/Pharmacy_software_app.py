from models import Medicine
from utils import *



if __name__ == "main":
    medicine_Inventory = []

    while True:
        print("""
            Choose the following operation:
            1: Add a medicine
            2: Delete medicine
            3: Update medicine
            4: See all available medicines
            5: See all available medicines in short supply
            6: Undo and redo functionality
            """)

        op = int(input())