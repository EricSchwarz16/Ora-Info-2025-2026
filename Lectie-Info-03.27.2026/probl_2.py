from multiprocessing import Process

def process(id):
    if(id > 10):
        return
    
    print(f"Sunt procesul cu id = {id}")
    p = Process(target = process, args = (id + 1,))
    p.start()
    p.join()
    

if __name__ == "__main__":
    id = 1
    p = Process(target = process, args = (id,) )
    p.start()
    p.join()