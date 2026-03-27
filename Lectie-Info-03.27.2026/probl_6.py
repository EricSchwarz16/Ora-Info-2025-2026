from multiprocessing import Process, Pipe

def child_process(conn):
    sir = conn.recv()
    print(f"Sirul primit este : {sir}")
    sum = 0

    for nr in sir:
        sum += nr
    
    sum = sum / len(sir)

    print("Media aritmetica este: ")
    conn.send(sum)
    conn.close()

if __name__ == "__main__":
    nr = []

    while True:
        x = int(input("Introdu un numar de la tastatura:"))
        if x != 0:
            nr.append(x)
        
        else:
            break
    

    parent_conn, child_conn = Pipe()
    p = Process(target = child_process, args = (child_conn,))

    parent_conn.send(nr)
    medie = parent_conn.recv()
    parent_conn.close()

    print(f"Media aritmetica a sirului este {medie}")
