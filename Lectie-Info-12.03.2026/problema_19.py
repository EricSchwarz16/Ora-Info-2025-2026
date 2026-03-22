"""
Scrieti un program C care primeste ca argument la linia de comanda un intreg N, apoi citeste de la tastatura N intregi 
si ii stocheaza intr-un sir. Programul calculeaza suma tuturor intregilor cititi folosind thread-uri care respecta ierarhia 
prezentata in imagine. Pentru orice N, sirul de intregi trebuie extins cu valori de 0 astfel incat numarul de elemente din sir 
sa fie o putere a lui 2 (fie numarul acesta M). Numarul de thread-uri necesare va fi M - 1, vom aloca cate un ID intre 1 si M - 1 
fiecarui thread. Conform imaginii, thread-urile cu ID >= M / 2 vor calcula suma a doua numere de pe pozitii consecutive din sir. 
Thread-urile cu ID < M / 2 trebuie sa astepte dupa alte 2 thread-uri si apoi vor aduna rezultatul produs de cele 2 thread-uri.

"""
import threading

numbers = []
threads = []
barrier = None
max_count = 0

def add(idx):
    global numbers
    barrier.wait()

    if idx < max_count // 2:
        threads[2 * idx].join()
        threads[2 * idx + 1].join()
    
    j = max_count
    while j > idx and j > 1:
        j //= 2
    
    i = j
    l = 0

    while i < idx:
        i += 1
        l += max_count // j
    
    r = l + max_count // j // 2
    numbers[l] += numbers[r]

if __name__ == "__main__":

    n = int(input("N = "))
    max_count = 1

    while max_count < n:
        max_count *= 2
    
    for i in range(max_count):
        if i < n:
            numbers.append(int(input(f"a[{i}]= ")))
        
        else:
            numbers.append(0)
    
    if max_count == 1:
        print(numbers[0])
        exit()
    
    barrier = threading.Barrier(max_count - 1)
    threads = [None] * max_count

    for i in range(1, max_count):
        threads[i] = threading.Thread(target = add, args = (i,))
        threads[i].start()
    

    threads[1].join()
    print(numbers[0])