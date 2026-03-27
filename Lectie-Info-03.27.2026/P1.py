import os
from constant import PATH

if __name__ == "__main__":
    if os.path.exists(PATH):
        os.remove(PATH)
        
    # cream fisierul fifo
    os.mkfifo(PATH)
    print("Am creat fisierul FIFO")
    
    fifo_fd = os.open(PATH, os.O_WRONLY) #blocam pana cand cineva deschide fifoul
    print("Avem un cititor conectat!!!!")
    
    mesaj = [23, 42, 23, 32] # -> 23 | 42 | 23 | 32
    
    #{4}
    # {4|23|42|23|32}
    # 23 42 23 32 -> message.split('|')
    
    os.write(fifo_fd, str(len(mesaj)).encode())
    
    for nr in mesaj:
        os.write(fifo_fd, str(nr).encode())
        
    print("p1 a terminat")
    os.close(fifo_fd)
    os.remove(PATH)
    