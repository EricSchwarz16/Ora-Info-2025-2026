import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from constants.constants import K
from repositories.news_repository import NewsRepository
import time
import threading
#top k news cache
#         1  7   30
cache = [{}, {}, {}]
timeframes = [1, 7, 30]
news_repo = NewsRepository()

#timeframe 1, 7, 30
#un thread pentru fiecare timeframe
def refresh_cache(option: int):
    global news_repo, cache, timeframes
    while True:
        news = news_repo.get_top_k(K, timeframes[option]) #iau top k stiri dintr-o perioada
        print(f"Refresh cache pentru {timeframes[option]} zile")
        # actualizez cache
        cache[option] = news

        print(cache[option])
        time.sleep(30)

if __name__ == "__main__":
    threads = []
    
    for option in range(3):
        th = threading.Thread(target=refresh_cache, args = ((option),))
        threads.append(th)    
        th.start()
    
    for th in threads:
        th.join()