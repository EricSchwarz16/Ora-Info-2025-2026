from repositories.videos_repository import VideoRepository
import random
import datetime
VIDEOS_NUMBER = 100
timeframes = [1, 7, 30]
count = 4

"""""
#for _ in range(VIDEOS_NUMBER):
title = f"Video {count}"
author = f"Author {count}"
date = f"{datetime.datetime.now().date()}"
content = f"Content {count}"
URL = f"https://test.com/video{count}"

print(f"Adaug video {title}")
VideoRepository().add(title, date, author, content, URL)

count += 1
"""

for timeframe in timeframes:
    for _ in range(1000):
        ids = VideoRepository().get_all_ids()

        chosen_id = random.choice(ids)
        date = datetime.datetime.now() - datetime.timedelta(days = timeframe - 1)
        VideoRepository().increment_views(chosen_id, date)
        print(f"Added views for video {chosen_id} timeframe {timeframe}")