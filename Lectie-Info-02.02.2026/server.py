import socket
import threading
import random

HOST = '127.0.0.1'
PORT = 9090

# 127.0.0.1:9090
random_number = str(random.randint(1, 1000)).encode('utf-8')
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

server.listen() # socketul serverului asculta requesturile
client = []

# thread care se ocupa de conexiunea cu clientii -> asculta mesajele de la conexiune, iar in cazul in care primim un mesaj, il transmite la toti clientii

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    global random_number
    connected = True
    while connected:
        msg = conn.recv(1024) #primesc mesaje de la client
        
        if msg.decode('utf-8') == random_number.decode('utf-8'):
            congrats_msg = "Congratulations! You guessed the number!".encode('utf-8')
            conn.send(congrats_msg)

        if msg:
            print(f"[{addr}] {msg.decode('utf-8')}")

            
        broadcast_message(msg, conn)
        

def broadcast_message(msg, sender_client):
    for c in client:
        if c != sender_client:
            c.send(msg)

def send_random_number():
    while True:
        global random_number
        random_number = str(random.randint(1, 1000)).encode('utf-8')
        broadcast_message(random_number, None)
        threading.Event().wait(10)  # astept 10 secunde 
        
        
# la fiecare 10 secunde, serverul transmite un numar random pe chat
# cine scrie cuvantul cat timp este inca valabil va primi un mesaj de congratulations -> (doar el va primi acel mesaj de la server)

#accept conexiunile de la clienti
if __name__ == "__main__":
    print("Server is listening...")
    threading.Thread(target=send_random_number, daemon=True).start()
    
    while True:
        conn, addr = server.accept() 
        client.append(conn)
        
        # deschid thread care se ocupa de clienti
        
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
    

        
        
        