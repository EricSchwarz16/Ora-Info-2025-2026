import os
from constant import PATH
import time

if __name__ == "__main__":
    fifo_fd = os.open(PATH, os.O_RDONLY)

    with os.fdopen(fifo_fd, "r") as fifo:
        lungime = int(fifo.readline().strip())
        print(lungime)
        time.sleep(2)

        for _ in range(lungime):
            nr = int(fifo.readline().strip())
            print(nr)
        
    print("P2 a terminat")