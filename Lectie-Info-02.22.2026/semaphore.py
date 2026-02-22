import threading
import random
import time

QUEUE_SIZE = 10
PRODUCER_NUMBER = 2
CONSUMER_NUMBER = 5
empty_slots = threading.Semaphore(QUEUE_SIZE)
filled_slots = threading.Semaphore(0)
mutex = threading.Lock()
products = []

def producer(id):
    global empty_slots, filled_slots, mutex, products
    
    while True:
        time.sleep(1)
        if(empty_slots._value == 0):
            print(f"Worker id-{id} waits for consumers to consume")
            
        empty_slots.acquire() # decrementez numarul de locuri libere, iar daca nu am niciun loc liber astept pana cand se gaseste unul
        #daca am empty slots, intru imi fac treaba
        random_number = random.randint(1, 100)
        print(f"Worker id-{id} started to work")
        # []
        # p1 -> 15
        # p2 -> 20
        mutex.acquire()
        products.append(random_number)
        print(f"Worker produced {random_number}, now we have {len(products)} products")
        mutex.release()
        
        filled_slots.release() #incrementez numarul de produse

def consumer(id):
    global empty_slots, filled_slots, mutex, products
    
    while True:
        time.sleep(1)
        if(filled_slots._value == 0):
            print(f"Consumer id-{id} waits for producers to produce")
        filled_slots.acquire()
        
        mutex.acquire()
        print(f"Consumed {products[-1]}, now we have {len(products) - 1} products")
        products.pop()
        mutex.release()
        
        empty_slots.release()

if __name__ == "__main__":
    threads = []
    id = 0
    for _ in range(PRODUCER_NUMBER):
        id += 1
        producer_thread = threading.Thread(target=producer, args=(id,))
        threads.append(producer_thread)
        producer_thread.start()
        
    id = 0
    for _ in range(CONSUMER_NUMBER): 
        id += 1
        consumer_thread = threading.Thread(target=consumer, args=(id,))
        threads.append(consumer_thread)
        consumer_thread.start()
    