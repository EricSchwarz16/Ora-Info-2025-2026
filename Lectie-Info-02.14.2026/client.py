#se conecteaza la server
#asteapta mesajul de broadcast -> dupa ce apare genereaza numere
#dupa mesajul de final se opreste
import socket
import threading
import random
import time

HOST = '127.0.0.1'
PORT = 9090
isRunning = True

def run_simulation(client):
    global isRunning
    #astept mesajul de broadcast si dupa generez
    print("Started simulation")
    while isRunning:
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        msg = str(x) + " " + str(y)
        
        client.send(msg.encode('utf-8'))
        time.sleep(2)
        print(f"Sent numbers {x, y}")

def listenToEstimation(udp_socket):
    global isRunning
    msg = udp_socket.recvfrom(1024)
    print(msg[0].decode('utf-8'))
    isRunning = False

if __name__ == "__main__":
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    #putem folosi mai multi clienti
    udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    udp_socket.bind(('', PORT))
    
    try:
        # Conectare la server
        client.connect((HOST, PORT))
        print(f"[CONNECTED] Connected to quiz server at {HOST}:{PORT}")
        
        msg = udp_socket.recvfrom(1024)
        print(msg[0].decode('utf-8'))
        
        # Start thread pentru primirea mesajelor
        receive_thread = threading.Thread(target=run_simulation, args=(client,))
        receive_thread.daemon = True
        receive_thread.start()
        
        
        # Listen for stop
        stop_thread = threading.Thread(target=listenToEstimation, args=(udp_socket,))
        stop_thread.daemon = True
        stop_thread.start()
        
        receive_thread.join()
        stop_thread.join()
        
    except Exception as e:
        print(f"[ERROR] Could not connect to server: {e}")
    finally:
        client.close()
        print("\n[DISCONNECTED] Disconnected from server.")
