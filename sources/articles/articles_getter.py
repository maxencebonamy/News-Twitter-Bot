from dataclasses import dataclass
from typing import List, Dict, ClassVar
import os
import requests
from sources.articles.article import Article


API_KEY: str = os.environ.get("NEWS_API_KEY", "")


@dataclass
class ArticlesGetter:

    __PAGE_LENGTH: ClassVar[int] = 10

    __count: int

    def __post_init__(self):
        self.__articles: List[Article] = []

        page_index: int = 1
        cond: bool = True

        while cond:
            url: str = f"https://newsapi.org/v2/top-headlines?country=fr" \
                       f"&pageSize={ArticlesGetter.__PAGE_LENGTH}" \
                       f"&page={page_index}&apiKey={API_KEY}"
            data: Dict[str, ...] = requests.get(url, timeout=10).json()

            if data.get("status") != "ok":
                raise RuntimeError(f"NewsAPI error: {data.get('message', data)}")
            if not data["articles"]:
                break

            element: Dict[str, ...]
            for element in data["articles"]:
                article: Article = Article(element["description"], element["source"]["name"],
                                           element["urlToImage"], element["url"])

                if cond and article.is_complete() and article.is_valid():
                    self.__articles.append(article)
                    cond = len(self.__articles) < self.__count

            page_index += 1

        if len(self.__articles) < self.__count:
            raise RuntimeError(f"Only {len(self.__articles)}/{self.__count} valid articles found")

    def __getitem__(self, index: int):
        assert 0 <= index < self.__count
        return self.__articles[index]

    def get_articles(self) -> List[Article]:
        return self.__articles.copy()