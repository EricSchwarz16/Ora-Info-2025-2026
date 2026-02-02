import socket
import threading

HOST = '127.0.0.1'
PORT = 9090

# 127.0.0.1:9090

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

server.listen() # socketul serverului asctula requesturile
client = []

# thread care se ocupa de conexiunea cu clientii -> asculta mesajele de la conexiune, iar in cazul in care primim un mesaj, il transmite la toti clientii

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    
    connected = True
    while connected:
        msg = conn.recv(1024) #primesc mesaje de la client
        
        if msg:
            print(f"[{addr}] {msg.decode('utf-8')}")
            
        broadcast_message(msg, conn)
        

def broadcast_message(msg, sender_client):
    for c in client:
        if c != sender_client:
            c.send(msg)
        
#accept conexiunile de la clienti
if __name__ == "__main__":
    print("Server is listening...")
    while True:
        conn, addr = server.accept() 
        client.append(conn)
        
        # deschid thread care se ocupa de clienti
        
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        
        
        