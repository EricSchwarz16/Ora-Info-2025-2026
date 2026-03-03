import threading
import time
import random

BARRIER_LIMIT = 3 

barrier = threading.Barrier(BARRIER_LIMIT)
cnt_perfume = 0
lock = threading.Lock()

def simulare_fabrica():
    global barrier, cnt_perfume, lock
    delay_time = random.uniform(0, 2)
    time.sleep(delay_time)

    barrier.wait()
    time.sleep(2)

    lock.acquire()
    cnt_perfume += 1
    id_cutie = cnt_perfume / 3
    if cnt_perfume % 3 == 0:
        print(f"Am expediat cutia cu numarul de serie {id_cutie}")

    lock.release()

if __name__ == "main":
    threads = []
    
    NUM_THREADS = random.randint(30, 50) * 3
    print(f"Avem {NUM_THREADS} Thread-uri")

    for id in range(NUM_THREADS):
        thread = threading.Thread(target = simulare_fabrica, args = (id,), daemon = True)
        threads.append(thread)
        thread.start()
    
    time.sleep(20)    