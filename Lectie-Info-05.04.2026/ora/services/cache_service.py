import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from constants.constants import K, tcp_ports_cache, timeframes
from repositories.news_repository import NewsRepository
import time
import threading
import socket
import json
#top k news cache
#         1  7   30
cache = [{}, {}, {}]
news_repo = NewsRepository()

#timeframe 1, 7, 30
#un thread pentru fiecare timeframe
def refresh_cache(option: int):
    global news_repo, cache, timeframes
    while True:
        news = news_repo.get_top_k(K, timeframes[option]) #iau top k stiri dintr-o perioada
        print(f"Refresh cache pentru {timeframes[option]} zile")
        # actualizez cache
        cache[option] = news

        print(cache[option])
        time.sleep(30)

def handle_client(conn, addr, option):
    msg = conn.recv(1024) #primesc mesaje de la client
    
    #msg = req -> daca vrea sa primeasca newsurile, daca e altceva ignoram 
        
    decoded_msg = msg.decode('utf-8')
    if decoded_msg == 'req':
        news_to_send = cache[option]
        #news_to_send -> dict
        encoded_news = json.dumps(news_to_send).encode()
        print("Acum trimit mesajul")
        conn.sendall(encoded_news)
        print("Am trimis mesajul")
        time.sleep(3)
        #conn.shutdown(1)
    else:
        conn.close()

def send_news(option: int):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    HOST = '127.0.0.1'
    PORT = tcp_ports_cache[option]
    server.bind((HOST, PORT))
    server.listen()
    print(f"Am inceput sa ascultam pentru {timeframes[option]} zile")
    client = []
    
    while True:
        conn, addr = server.accept() 
        client.append(conn)
        
        # deschid thread care se ocupa de clienti
        
        thread = threading.Thread(target=handle_client, args=(conn, addr, option))
        thread.start()

if __name__ == "__main__":
    threads = []
    
    for option in range(3):
        th = threading.Thread(target=refresh_cache, args = ((option),))
        threads.append(th)    
        th.start()
        
    for option in range(3):
        th = threading.Thread(target=send_news, args = ((option),))
        threads.append(th)    
        th.start()
    
    for th in threads:
        th.join()