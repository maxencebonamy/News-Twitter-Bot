from dataclasses import dataclass
from typing import List, Dict, ClassVar
import requests

from sources.articles.key import API_KEY
from sources.articles.article import Article


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
            data: Dict[str, ...] = requests.get(url).json()

            element: Dict[str, ...]
            for element in data["articles"]:
                article: Article = Article(element["description"], element["source"]["name"],
                                           element["urlToImage"], element["url"])

                if cond and article.is_complete() and article.is_valid():
                    self.__articles.append(article)
                    cond = len(self.__articles) < self.__count

            page_index += 1

        assert len(self.__articles) == self.__count

    def __getitem__(self, index: int):
        assert 0 <= index < self.__count
        return self.__articles[index]

    def get_articles(self) -> List[Article]:
        return self.__articles.copy()