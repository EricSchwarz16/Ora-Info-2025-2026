"""
Hot Potato: Scrieti un program C care primeste ca argument un numar N la linia de comanda.
Procesul principal genereaza un numar aleator intre 1000 si 10000 (numim aceasta variabila POTATO)
si creeaza N thread-uri si le asigneaza fiecaruia un identificator unic pornind de la 1. Cele N thread-uri
executa o bucla infinita in care incearca sa scada o valoare aleatoare intre 10 si 100 din POTATO si apoi
asteapta un timp aleator intre 100 si 200 de milisecunde. Primul thread care face ca valoarea POTATO sa fie
negativa va afisa un mesaj prin care anunta aceasta (mesajul va include si identificatorul primit de la procesul principal),
apoi iese din bucla si isi incheie executia. Orice thread care detecteaza ca valoarea POTATO este negativa va iesi din bucla
si isi va incheia executia, dar fara sa afiseze niciun mesaj.
"""

import threading
import random
import time

N = random.randint(1, 100)
lock = threading.Lock()
POTATO = 0
winner_announced = False

def run_thread(id):
    global POTATO, winner_announced

    while True:
        with lock:
            if POTATO < 0:
                print(f"Threadul {id} este un fraier!")
                return

            val = random.randint(10, 100)
            POTATO -= val

            if POTATO < 0:
                if not winner_announced:
                    winner_announced = True
                    print(f"Threadul {id} este castigator!")
                return

        time.sleep(random.uniform(0.1, 0.2))

# primul thread care reuseste sa faca potato mai mic decat zero sunt castigator, restul sunt pierzator!
            
if __name__ == "__main__":
    POTATO = random.randint(1000, 10000)

    threads = []

    for i in range(1, N + 1):
        thread = threading.Thread(target = run_thread, args = (i,))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()
    


