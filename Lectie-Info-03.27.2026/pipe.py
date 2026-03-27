from multiprocessing import Process, Pipe

#Process -> deschidem un proces nou
#Pipe -> comunicam intre procese

sum = 3

def child_process(conn):
    global sum
    print(sum)
    print("Am deschis un proces")
    conn.send(["Salut", "sunt", "jmecher"])
    print("Inchid conexiunea")
    conn.close()

if __name__ == "__main__":
    parent_conn, child_conn = Pipe() #capetele pipe-ului
    
    sum += 1
    p = Process(target = child_process, args = (child_conn, ))
    p.start()
    
    mesaj = parent_conn.recv()
    print(f"Am primit mesajul: {mesaj}")
    
    p.join()