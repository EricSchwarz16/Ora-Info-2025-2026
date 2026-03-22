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

lock = threading.Lock()
suma = 0

def sum_rand_t(matrix : list[list[int]], start_row : int, size: int):
    global suma
    
    for i in range(size):
        row_sum = sum(matrix[start_row + i])
        
        lock.acquire()
        suma += row_sum
        lock.release()

def sum_rand(matrix : list[list[int]], n : int, m : int, nr_threads : int) -> int:
    global suma
    suma = 0
    threads = []
    min_rows = n // nr_threads
    left_rows = n % nr_threads
    start_row = 0
    
    for _ in range(nr_threads):
        rows = min_rows
        
        if left_rows > 0:
            rows + 1
            left_rows -= 1
        
        th = threading.Thread(target=sum_rand_t, args=((matrix, start_row, rows)))
        threads.append(th)
        start_row += rows
    
    for th in threads:
        th.start()
        
    for th in threads:
        th.join()
    
def count_time_for(matrix : list[list[int]], n : int, m : int, nr_threads : int, f):
    global suma
    start_time = datetime.now()
    f(matrix, n, m, nr_threads)
    duration = datetime.now() - start_time
    print(f"Am terminat simularea pentru o matrice {n} x {m}: {duration}")
    print(f"Suma este {suma}")

if __name__ == "__main__":
    nr_threads = 5
    M1 = generate_matrix(10, 10)
    M2 = generate_matrix(100, 100)
    M3 = generate_matrix(1000, 1000)
    M4 = generate_matrix(8000, 8000)

    print("Testam pentru suma pe linii")
    print("_____________________________________________________")
    count_time_for(M1, 10, 10, 5, sum_rand)
    count_time_for(M2, 100, 100, 5, sum_rand)
    count_time_for(M3, 1000, 1000, 5, sum_rand)
    count_time_for(M4, 8000, 8000, 5, sum_rand)
    
    print("_____________________________________________________")
    
