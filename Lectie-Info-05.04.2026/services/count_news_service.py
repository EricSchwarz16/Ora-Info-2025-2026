import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from repositories.news_repository import NewsRepository
import random
import socket
import time

HOST = "127.0.0.1"
UDP_PORT = 9091

def broadcast(udp_socket, text):
    udp_socket.sendto(text.encode("utf-8"), ("<broadcast>", UDP_PORT))

if __name__ == "__main__":
    news_repo = NewsRepository()
    ids = news_repo.get_all_ids()
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    while True:
        chosen_id = random.choice(ids)
        time.sleep(random.randint(1,3))
        
        #dau broadcast la id-ul pe care il citesc
        broadcast(udp_socket, str(chosen_id))
        print(f"Am citit stirea cu id - {str(chosen_id)}")