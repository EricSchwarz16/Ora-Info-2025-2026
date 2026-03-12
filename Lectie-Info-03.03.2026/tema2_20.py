import random
import sys
import threading
import time


"""
Scrieti un program C care primeste ca argumente la linia de comanda 
2 numere: N si M. Programul va simula o cursa intre N thread-uri care 
trebuie sa treaca prin M puncte de control. Prin fiecare punct de control 
thread-urile trebuie sa treaca pe rand (nu se poate ca 2 thread-uri sa fie 
simultan in acelasi punct de control). Fiecare thread care intra intr-un punct 
de control va astepta intre 100 si 200 de milisecunde (usleep(100000) face 
ca un thread sau proces sa astepte 100 de milisecunde) si va afisa un mesaj care 
va contine numarul thread-ului si numarul punctului de control, apoi va iesi din punctul de control. 
Fiecare thread va astepta pana cand toate thread-urile au fost create.
"""

def run_thread(thread_id, checkpoints_count, checkpoint_locks, start_barrier):
    print(f"Thread {thread_id} is waiting...")
    start_barrier.wait()

    for checkpoint_id in range(checkpoints_count):
        with checkpoint_locks[checkpoint_id]:
            print(f"Thread {thread_id} has entered checkpoint {checkpoint_id}")
            time.sleep(random.uniform(0.1, 0.2))
    
    print(f"Thread {thread_id} finished")

def main():
    if len(sys.argv) != 3:
        print("Please provide 2 arguments!")
    
    try:
        threads_count = int(sys.argv[1])
        checkpoints_count = int(sys.argv[2])
    
    except ValueError:
        print("Both arguments must be integers")
        return
    
    if threads_count <= 0 and checkpoints_count <= 0:
        print("N and M must be positive integers!")
    
    checkpoint_locks = [threading.Lock() for _ in range(checkpoints_count)]
    start_barrier = threading.Barrier(threads_count)

    threads = []
    for thread_id in range(threads_count):
        thread = threading.Thread(target = run_thread, args = (thread_id, checkpoints_count, checkpoint_locks, start_barrier))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()   