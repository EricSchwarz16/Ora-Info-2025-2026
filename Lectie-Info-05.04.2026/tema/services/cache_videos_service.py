import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from constants.constants import K
from repositories.videos_repository import VideoRepository
import time
import threading

#top k videos cache
cache = [{}, {}, {}]
timeframe = [1, 7, 30]
video_repo = VideoRepository()

def refresh_cache(option: int):
    global video_repo, cache, timeframe

    while True:
        videos = video_repo.get_top_k(K, timeframe[option]) #iau top k stiri dintr-o perioada
        print(f"Refresh cache pentru {timeframe[option]} zile")
        # actualizez cache
        cache[option] = videos
        print(cache[option])
        time.sleep(30)
    
if __name__ == "__main__":
    threads = []

    for i in range(3):
        th = threading.Thread(target = refresh_cache, args = (i,))
        threads.append(th)
        th.start()
    
    for th in threads:
        th.join()