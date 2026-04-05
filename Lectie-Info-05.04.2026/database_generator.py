from repositories.news_repository import NewsRepository
import random
import datetime

NEWS_NUMBER = 97
timeframes = [1, 7, 30]
count = 4

"""
for _ in range(NEWS_NUMBER):
    title = f"Stire-{count}"
    descriere = f"descriere-{count}"
    content = f"content-{count}"
    photo = "https://test.com"
    
    print(f"Adaug stirea {title}")
    NewsRepository().add(title, descriere, content, photo)
    count += 1
"""

for timeframe in timeframes:
    for _ in range(1000):
        ids = NewsRepository().get_all_ids()
        
        chosen_id = random.choice(ids)
        date = datetime.datetime.now() - datetime.timedelta(days=timeframe - 1)
        NewsRepository().increment_views(chosen_id, date)
        print(f"Added views for news-{chosen_id} timeframe-{timeframe}")
        
