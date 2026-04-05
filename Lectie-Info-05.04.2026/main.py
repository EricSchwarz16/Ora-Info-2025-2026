from news_repository import NewsRepository
import datetime
 
repo = NewsRepository()

repo.increment_views(2, date=datetime.datetime.now())
repo.increment_views(2, date=datetime.datetime.now())
repo.increment_views(2, date=datetime.datetime.now())
print(repo.get_top_k(2, 1))