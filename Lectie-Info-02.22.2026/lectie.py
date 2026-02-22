import threading
import time
from threading import Lock

click = 0
RANGE = 100000
mtx = Lock() # lock = mutex

def incrementClick():
    global click
    
    for _ in range(5):
        mtx.acquire() # fix
        # ------------------------------------------
        test = click
        time.sleep(0.00000001)
        click = test + 1
        # --------------------------------------------------
        # sectiune critica - critical section
        mtx.release()
        #dead lock -> cand asteptam la infinit dupa un mecanism
        
if __name__ == "__main__":
    NUM_THREADS = 5
    threads = []
    
    #click number = NUM_THREADS * RANGE
    for _ in range(NUM_THREADS):
        th = threading.Thread(target=incrementClick)
        threads.append(th)
        th.start()
        
        
    for thread in threads:
        thread.join()
    
    print(click)