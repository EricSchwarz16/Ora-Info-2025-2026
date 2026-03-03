import threading
import time
import random

BARRIER_LIMIT = 3
NUM_THREADS = 11

barrier = threading.Barrier(BARRIER_LIMIT)

def simulare_pod(id):
    global barrier
    
    print(f"Am ajuns la bariera, astept sa se dechida! Thread id: {id}")
    arrive_time = random.randint(0, 5)
    time.sleep(arrive_time)
    
    barrier.wait() #nu asteapta pana cand celelalte threaduri termina treaba, cand sunt NUM_THREADS le lasa inauntru
    time.sleep(1)
    
    print("Am trecut podul")
    
if __name__ == "__main__":
    threads = []

    for id in range(NUM_THREADS):
        th = threading.Thread(target=simulare_pod, args=((id, )), daemon=True)
        threads.append(th)
        th.start()
    
    time.sleep(10)
    
    