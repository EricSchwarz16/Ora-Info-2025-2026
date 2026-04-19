import socket
import threading
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from constants.constants import tcp_ports_cache, tcp_ports_news, timeframes

def news_server(option: int):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    HOST = '127.0.0.1'
    PORT_NEWS = tcp_ports_news[option]
    server.bind((HOST, PORT_NEWS))
    server.listen()
    print(f"Am inceput sa ascultam pentru {timeframes[option]} zile")
    
    while True:
        conn, addr = server.accept() #conn -> socketul pentru userul care cere informatiile
        print("Un client s-a conectat")
        #trebuie sa ne conectam la cache serviceul correct
        
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #socketul care face conexiunea -> cache - news service
        PORT_CACHE = tcp_ports_cache[option]
        #ne conectam la server
        client.connect((HOST, PORT_CACHE))
        print("M am conectat la cache")
        
        #trimitem requestul
        msg = "req"
        client.send(msg.encode('utf-8'))
        print("Am trimis requestul")
        msg = client.recv(1024) #primesc mesaj de la cache
        
        #aratama ce am primit
        print(f"{msg.decode('utf-8')}")
        
        conn.sendall(msg)
        conn.close()
        
        
if __name__ == "__main__":
    threads = []
    
    for option in range(3):
        th = threading.Thread(target=news_server, args=((option),))   
        threads.append(th)
        th.start()
        
    for th in threads:
        th.join()    
     


