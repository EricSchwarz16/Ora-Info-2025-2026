from multiprocessing import Process, Pipe
import random

def process_child(conn):
        nr = conn.recv()
        while nr < 5:
            nr /= 2
            print(f"Valoarea lui n este {nr}")
            conn.send(nr)
            nr = conn.recv()
    

if __name__ == "__main__":
    nr = random.randint(50, 200)
    
    parent_conn, child_conn = Pipe()
    p = Process(target = process_child, args = (child_conn,))
    p.start()
    while nr < 5:
        
        if nr % 2 == 0:
            parent_conn.send(nr)
    
        else:
            nr += 1
            print(f"Valoarea lui n este: {nr}")
            parent_conn.send(nr)

        nr = parent_conn.recv()
    
    parent_conn.close() 