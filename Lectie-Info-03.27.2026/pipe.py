from multiprocessing import Process, Pipe
import threading

#Process -> deschidem un proces nou
#Pipe -> comunicam intre procese

sum = 0
mutex = threading.Lock()

def thread_child():
    global sum
    mutex.acquire()
    sum += 1
    mutex.release()
    

def child_process(conn):
    print(sum)
    print("Am deschis un proces")
    conn.send(["Salut", "sunt", "jmecher"])
    print("Inchid conexiunea")
    conn.close()
    
    nrThreads = 10
    threads = []
    
    for _ in range(nrThreads):
        th = threading.Thread(target = thread_child, args = ())
        th.start()
        threads.append(th)
        
    for t in threads:
        t.join()
        
    print(f"Suma este {sum}")

if __name__ == "__main__":
    parent_conn, child_conn = Pipe() #capetele pipe-ului
    
    sum += 1
    p = Process(target = child_process, args = (child_conn, ))
    p.start()
    
    mesaj = parent_conn.recv()
    print(f"Am primit mesajul: {mesaj}")
    
    p.join()