import threading
import time
import random

PHILOSOPHERS = random.randint(10, 25)
forks = [threading.Lock() for _ in range(PHILOSOPHERS)]

def flow(id: int):
    right = id
    left = 0 if id == PHILOSOPHERS - 1  else id - 1
    
    forks[left].acquire() #Potential deadlock in cazul in care fiecare filozof ia furculita din stanga
    forks[right].acquire() #FIX -> dupa un numar de secunde de astere eliminam furculita sa manance altcineva!!!!!
    
    print(f"M-am apucat sa mananc!!! id:{id}")
    time.sleep(2)
    print(f"Am terminat de mancat id: {id}")
    forks[left].release()
    forks[right].release()
    

if __name__ == "__main__":
    print(f"We have {PHILOSOPHERS} philosophers")
    threads = []
    
    for id in range(PHILOSOPHERS):
        #id incepe de la 0, nu de la 1 !!!!!!!!!
        thread = threading.Thread(target=flow, args = (id, ))
        threads.append(thread)
        thread.start()
        
    for th in threads:
        th.join()