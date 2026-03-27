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
            rows += 1
            left_rows -= 1
        
        th = threading.Thread(target=sum_rand_t, args=((matrix, start_row, rows)))
        threads.append(th)
        start_row += rows
    
    for th in threads:
        th.start()
        
    for th in threads:
        th.join()

def sum_coloane_t(matrix: list[list[int]], n: int,  start_col: int, size: int):
    global suma
    
    for i in range(size):
        col_sum = 0
        for j in range(n):
            col_sum += matrix[j][start_col + i]
        
        lock.acquire()
        suma += col_sum
        lock.release()

def sum_coloane(matrix: list[list[int]], n: int, m : int, nr_threads : int) -> int:
    global suma
    suma = 0
    threads = []
    min_cols = m // nr_threads
    left_cols = m % nr_threads
    start_col = 0

    for _ in range(nr_threads):
        cols = min_cols

        if left_cols > 0:
            cols += 1
            left_cols -= 1
        
        th = threading.Thread(target = sum_coloane_t, args = (matrix, n, start_col, cols))
        threads.append(th)
        start_col += cols
    
    for th in threads:
        th.start()
    
    for th in threads:
        th.join()

def sum_elemente_t(matrix: list[list[int]], n: int, m: int, start_elem: int, size: int):
    global suma
    local_sum = 0
    
    for k in range(size):
        elem_pos = start_elem + k
        i = elem_pos // m
        j = elem_pos % m
        local_sum += matrix[i][j]
    
    lock.acquire()
    suma += local_sum
    lock.release()

def sum_elemente(matrix: list[list[int]], n: int, m: int, nr_threads: int) -> int:
    global suma
    suma = 0
    threads = []
    total_elems = n * m
    min_elems = total_elems // nr_threads
    left_elems = total_elems % nr_threads
    start_elem = 0
    
    for _ in range(nr_threads):
        elems = min_elems
        
        if left_elems > 0:
            elems += 1
            left_elems -= 1
        
        th = threading.Thread(target=sum_elemente_t, args=(matrix, n, m, start_elem, elems))
        threads.append(th)
        start_elem += elems
    
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
    #M4 = generate_matrix(8000, 8000)

    print("Testam pentru suma pe linii")
    print("_____________________________________________________")
    count_time_for(M1, 10, 10, 5, sum_rand)
    count_time_for(M2, 100, 100, 5, sum_rand)
    count_time_for(M3, 1000, 1000, 5, sum_rand)
    #count_time_for(M4, 8000, 8000, 5, sum_rand)
    
    print("_____________________________________________________")
    print("Testam pentru suma pe coloane")
    count_time_for(M1, 10, 10, 5, sum_coloane)
    count_time_for(M2, 100, 100, 5, sum_coloane)
    count_time_for(M3, 1000, 1000, 5, sum_coloane) 
    #count_time_for(M4, 8000, 8000, 5, sum_coloane)
    
    print("_____________________________________________________")
    print("Testam pentru suma pe elemente (stanga-dreapta, sus-jos)")
    count_time_for(M1, 10, 10, 5, sum_elemente)
    count_time_for(M2, 100, 100, 5, sum_elemente)
    count_time_for(M3, 1000, 1000, 5, sum_elemente)
    #count_time_for(M4, 8000, 8000, 5, sum_elemente)
