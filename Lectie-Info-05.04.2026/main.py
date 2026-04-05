from news_repository import NewsRepository
import datetime

repo = NewsRepository()
print(repo.get_top_k(10, 30))
