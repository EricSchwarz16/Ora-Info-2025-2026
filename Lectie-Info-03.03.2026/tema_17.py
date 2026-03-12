import random
import threading


"""
Scrieti un program C care citeste de la tastatura un numar N si creeaza 2 thread-uri. 
Unul dintre thread-uri va genera un numar par si il va insera intr-un sir primit ca parametru.
Celalalt thread va genera un numar impar si il va insera in acelasi sir de numere primit ca parametru.
Implementati un mecanism de sincronizare intre cele 2 thread-uri astfel incat alterneaza in 
inserarea de numere in sir, pana cand sirul contine N numere.
"""
class SharedData:
    def __init__(self, n):
        self.n = n
        self.arr = [0] * n
        self.index = 0
        self.cond = threading.Condition()
    
def print_partial(prefix, arr, count):
    print(f"{prefix}: ", *arr[:count])

def thread_even(shared):
    with shared.cond:
        while shared.index % 2 != 0:
            shared.cond.wait()
    
        while shared.index < shared.n:
            value = random.randrange(0, 51) * 2
            shared.arr[shared.index] = value
            shared.index += 1
        
            print_partial('T1', shared.arr, shared.index)

            shared.cond.notify()

            while shared.index % 2 != 0 and shared.index < shared.n:
                shared.cond.wait()
        
        shared.cond.notify()

def thread_odd(shared):
    with shared.cond:
        while shared.index % 2 != 1:
            shared.cond.wait()
        
        while shared.index < shared.n:
            value = random.randrange(0, 50) * 2 + 1
            shared.arr[shared.index] = value
            shared.index += 1

            print_partial('T2', shared.arr, shared.index)

            shared.cond.notify()

            while shared.index % 2 != 1 and shared.index < shared.n:
                shared.cond.wait()
        
        shared.cond.notify()

def main():
    n = int(input("N =").strip())
    if n <= 0:
        print("N trebuie sa fie pozitiv!")
    
    shared = SharedData(n)

    t1 = threading.Thread(target = thread_even, args = (shared,))
    t2 = threading.Thread(target = thread_odd, args = (shared,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Sir final: ", *shared.arr)

if __name__ == "__main__":
    main()