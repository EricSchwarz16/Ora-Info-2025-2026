import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from repositories.news_repository import NewsRepository
import socket
import datetime
UDP_PORT = 9091

if __name__ == "__main__":
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    udp_socket.bind(("", UDP_PORT))
    news_repo = NewsRepository()
    
    while True:
        message = udp_socket.recv(1024).decode()
        print(f"trebuie sa actualizez stirea cu id-{message}")
        print(news_repo.get_views_by_id(message))
        news_repo.increment_views(int(message), datetime.datetime.now())
        print(news_repo.get_views_by_id(message))