import os
from constant import PATH
import time

if __name__ == "__main__":
    fifo_fd = os.open(PATH, os.O_RDONLY)
    
    received_bytes = os.read(fifo_fd, 1)

    lungime = int(received_bytes.decode('utf-8'))
    print(lungime)
    time.sleep(2)
    for _ in range(lungime):
        received_bytes = os.read(fifo_fd, 1)
        nr = received_bytes.decode('utf-8')
        print(nr)
        
    os.close(fifo_fd)
    print("p2 a terminat")