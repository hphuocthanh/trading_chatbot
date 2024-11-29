from gnews import GNews

google_news = GNews(max_results=20, period="3d")


def get_news(keyword: str):  # example: "bitcoin", "apple", "microsoft"
    return google_news.get_news(keyword)


def get_market_prices(keyword: str):

    return
