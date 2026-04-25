import socket
import threading
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from constants.constants import tcp_ports_cache, tcp_ports_videos, timeframes

def videos_server(option):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    HOST = '127.0.0.1'
    PORT_VIDEOS = tcp_ports_videos[option]
    server.bind((HOST, PORT_VIDEOS))
    server.listen()
    print(f'Am inceput sa ascultam pentru {timeframes[option]} zile')

    while True:
        conn, addr = server.accept()
        print('Un client s-a conectat!')
        
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        PORT_CACHE = tcp_ports_cache[option]
        client.connect((HOST, PORT_CACHE))
        print('M-am conectat la cache!')

        msg = 'req'
        client.send(msg.encode('utf-8'))
        print('Am trimis request-ul!')
        chunks = []
        while True:
            chunk = client.recv(4096)
            if not chunk:
                break
            chunks.append(chunk)
        msg = b''.join(chunks)
        print(f"{msg.decode('utf-8')}")
        conn.sendall(msg)
        conn.close()

if __name__ == '__main__':
    threads = []
    for option in range(3):
        th = threading.Thread(target = videos_server, args = (option, ))
        threads.append(th)
        th.start()
    
    for th in threads:
        th.join()