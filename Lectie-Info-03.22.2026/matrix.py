import threading
import random
from datetime import datetime

#rulez pe matrice de 10 x 10
def generate_matrix(n, m):
    matrice = [[0 for _ in range (m)] for _ in range (n)]

    for i in range(0, n):
        for j in range(0, m):
            matrice[i][j] = random.randint(1, 100)
    
    return matrice

def print_matrix(matrix):
    for rand in matrix:
        for elem in rand:
            print(elem, end = ' ')
        
        print()

def sum_rand(matrix -> list[list[int]], n -> int, m -> int, nr_threads -> int):
    

if __name__ == "__main__":

    M1 = generate_matrix(10, 10)
    M2 = generate_matrix(100, 100)
    M3 = generate_matrix(1000, 1000)

    print_matrix(M1)
   # print_matrix(M2)
    #print_matrix(M3)

    
