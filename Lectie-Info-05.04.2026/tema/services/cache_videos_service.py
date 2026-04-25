import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from constants.constants import K, tcp_ports_cache, timeframes
from repositories.videos_repository import VideoRepository
import time
import threading
import socket
import json

#top k videos cache
cache = [{}, {}, {}]
timeframe = [1, 7, 30]
video_repo = VideoRepository()

def refresh_cache(option: int):
    global video_repo, cache, timeframe

    while True:
        videos = video_repo.get_top_k(K, timeframe[option]) #iau top k stiri dintr-o perioada
        print(f"Refresh cache pentru {timeframe[option]} zile")
        # actualizez cache
        cache[option] = videos
        print(cache[option])
        time.sleep(30)
def handle_client(conn, addr, option):
    msg = conn.recv(1024) #primesc mesaje de la client
    decoded_msg = msg.decode('utf-8')

    if decoded_msg == 'req':
        videos_to_send = cache[option]
        #videos_to_send = list of tuples
        encoded_videos = json.dumps(videos_to_send).encode()
        print('Acum trimit mesajul')
        conn.sendall(encoded_videos)
        print('Am trimis mesajul!')
        time.sleep(3)

    else:
        conn.close()

def send_videos(option):
    server = socket.socket(socket. AF_INET, socket.SOCK_STREAM)
    HOST = '127.0.0.1'
    PORT = tcp_ports_cache[option] 
    server.bind((HOST, PORT))
    server.listen()
    print(f'Am inceput sa ascultam pentru {timeframe[option]} zile')
    while True:
        conn, addr = server.accept()
        print('Un client s-a conectat!')
        thread = threading.Thread(target = handle_client, args = (conn, addr, option))
        thread.start()

if __name__ == "__main__":
    threads = []

    for i in range(3):
        th = threading.Thread(target = refresh_cache, args = (i,))
        threads.append(th)
        th.start()
    
    for i in range(3):
        th = threading.Thread(target = send_videos, args = (i,))
        threads.append(th)
        th.start()

    for th in threads:
        th.join()