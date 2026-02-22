
# simulare monte carlo
# asteptam 2 conexiuni
# 60 secunde rulam simularea cu clientii conectati
# dam broadcast prin udp la rezultat -> cand clientii primesc -> opresc simularea


import socket
import threading
import math
import time
HOST = '127.0.0.1'
PORT = 9090
MAX_CLIENTS = 2
clients = []

inside_points = 0
outside_points = 0

def handle_client(conn, addr):
    global inside_points, outside_points
    print(f"Started to handle client {conn, addr}")
    connected = True
    while connected:
        try:
            msg = conn.recv(1024)
            if not msg:
                break
            
            points = msg.decode('utf-8').split(' ')
            x = float(points[0])
            y = float(points[1])
            
            print(f"received {x, y}")
            
            #daca distanta de la origine <= 1 -> interior
            
            d = math.sqrt(x*x + y*y)
            
            # we could have race conditions here
            if d <= 1:
                inside_points += 1
            else:
                outside_points += 1
                    
        except Exception as e:
            print(f"[ERROR] {addr}: {e}")
            break
    
    print("connection stopped")

if __name__ == "__main__":
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    print("Running server")
    
    while True:
        conn, addr = server.accept()
        clients.append(conn)     
        print(f"Client {conn, addr} connected")
        
        # Start thread pentru fiecare client
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.daemon = True
        thread.start()
        
        if len(clients) == MAX_CLIENTS:
            #run monte carlo simulation 60 sec
            #dam broadcast ca am inceput -> clientii primesc semnalul si incep sa genereze numere
            time.sleep(2.5)
            msg = "START"
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
            sock.sendto(msg.encode(), ("<broadcast>", PORT))
            
            print("Started game!")
            
            time.sleep(20)
            #asteptam 60 secunde
            
            total_points = inside_points + outside_points
            estimation = 4 * inside_points / total_points
            
            #calculam rezultatul si dam broadcast la el, clientii se pot opri
            
            msg = str(estimation)
            print("Game ended!")
            print(f"My estimation {estimation}")
            sock.sendto(msg.encode(), ("<broadcast>", PORT))
            clients.clear()
            