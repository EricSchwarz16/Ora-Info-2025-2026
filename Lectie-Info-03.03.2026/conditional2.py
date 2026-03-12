import threading
import random
import time

is_writing = False
reader_count = 0
condition = threading.Condition()

def reader(id):
    global is_writing, reader_count

    with condition:
        while is_writing:
            condition.wait()
        reader_count += 1
        print(f"Reader {id} citeste resursa (reader_count={reader_count})")

    time.sleep(random.uniform(0.5, 2))

    with condition:
        reader_count -= 1
        print(f"Reader {id} a terminat de citit (reader_count={reader_count})")

        if reader_count == 0:
            condition.notify_all()

def writer(id):
    global is_writing, reader_count

    with condition:
        while is_writing or reader_count > 0:
            condition.wait()
        is_writing = True

    print(f"Cititorul {id} modifica resursa")
    time.sleep(random.uniform(0.2, 1))

    with condition:
        is_writing = False
        print(f"Scriitorul {id} a terminat modificarea")
        condition.notify_all()

def main():
    C = random.randint(1, 50)
    S = random.randint(1, 20)

    threads = []

    print(f"Pornesc simularea cu {C} cititori si {S} scriitori")

    for index in range(1, C + 1):
        threads.append(threading.Thread(target=reader, args=(index,)))

    for index in range(1, S + 1):
        threads.append(threading.Thread(target=writer, args=(index,)))

    random.shuffle(threads)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print("Simularea s-a incheiat")

if __name__ == "__main__":
    main()