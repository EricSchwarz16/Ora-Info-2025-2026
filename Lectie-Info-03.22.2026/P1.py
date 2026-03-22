import time
cnt = 1

def sayHello():
    print("Hello!")

if __name__ == "__main__":
    while True:
       print(f"cnt: {cnt}")
       time.sleep(2)
       cnt += 1 