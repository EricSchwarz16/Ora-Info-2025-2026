import threading
import time
import random

PHILOSOPHERS = random.randint(10, 25)
forks = [threading.Lock() * PHILOSOPHERS]

def flow():
    
    forks[].acquire