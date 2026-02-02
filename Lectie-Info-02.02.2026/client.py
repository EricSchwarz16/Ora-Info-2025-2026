import socket
import threading

HOST = '127.0.0.1'
PORT = 9090

def handle_messages(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    
    connected = True
    while connected:
        msg = conn.recv(1024)
        
        #print la mesaje
        print(f"{msg.decode('utf-8')}")
        

if __name__ == "__main__":
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    #ne conectam la server
    client.connect((HOST, PORT))
    
    #trimitem mesaje
    
    thread = threading.Thread(target=handle_messages, args=(client, HOST))
    thread.start()
    
    while True:
        #citim mesajul
        
        msg = input()
        client.send(msg.encode('utf-8'))
        
        
    