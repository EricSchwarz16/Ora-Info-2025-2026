from repositories.news_repository import NewsRepository

repo = NewsRepository()
print(repo.get_top_k(10, 30))
