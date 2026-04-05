<<<<<<< HEAD
from news_repository import NewsRepository
import datetime
 
repo = NewsRepository()

repo.increment_views(2, date=datetime.datetime.now())
repo.increment_views(2, date=datetime.datetime.now())
repo.increment_views(2, date=datetime.datetime.now())
print(repo.get_top_k(2, 1))
=======
from repositories.news_repository import NewsRepository

repo = NewsRepository()
print(repo.get_top_k(10, 30))
>>>>>>> 68f0fc1995eef73b971b22979374f534683d3d95
