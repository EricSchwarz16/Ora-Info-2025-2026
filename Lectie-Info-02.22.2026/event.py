import threading
import time
ev = threading.Event()

def inginer():
    print("Astept dupa document")
    ev.wait()
    
    print("Lucrez")
    
if __name__ == "__main__":
    NUM_INGINERI = 10
    
    for _ in range(NUM_INGINERI):
        threading.Thread(target = inginer).start()
        
    #vine bossu si le da drumu
    time.sleep(5)
    ev.set() #semnal