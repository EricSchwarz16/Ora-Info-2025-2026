import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from repositories.videos_repository import VideoRepository
import random
import socket
import time

HOST = "127.0.0.1"
UDP_PORT = 9092

def broadcast(udp_socket, text):
    udp_socket.sendto(text.encode("utf-8"), ("<broadcast>", UDP_PORT))

if __name__ == "__main__":
    video_repo = VideoRepository()
    ids = video_repo.get_all_ids()
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    
    while True:
        chosen_id = random.choice(ids)
        time.sleep(random.randint(1, 3))

        broadcast(udp_socket, str(chosen_id))
        print(f"M- am uitat la videoclipul cu id {str(chosen_id)}")


