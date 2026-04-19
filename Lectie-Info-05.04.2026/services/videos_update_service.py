import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from repositories.videos_repository import VideoRepository
import socket
import datetime
UDP_PORT = 9092

if __name__ == "__main__":
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    udp_socket.bind(("", UDP_PORT))
    video_repo = VideoRepository()

    while True:
        message = udp_socket.recv(1024).decode()
        print(f"Trebuie sa actualizez videoclipul cu id {message}")
        print(video_repo.get_views_by_id(message))
        video_repo.increment_views(int(message), datetime.datetime.now())
        print(video_repo.get_views_by_id(message))
