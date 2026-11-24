from sources.articles.articles_getter import ArticlesGetter


def main() -> None:
    articles: ArticlesGetter = ArticlesGetter(4)
    for article in articles.get_articles():
        print(f"[{article.get_source()}] {article.get_description()}\n  {article.get_link()}")


if __name__ == "__main__":
    main()
