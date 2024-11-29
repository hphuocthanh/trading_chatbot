from api.models.news import News
from typing import List


def extract_news(news_data) -> List[News]:
    extracted_news: List[News] = []
    for news in news_data:
        extracted_news.append(
            {"title": news["title"], "description": news["description"]}
        )
    return extracted_news


def extract_market_prices(market_data):
    extracted_prices = []
    for price in market_data:
        extracted_prices.append({"symbol": price["symbol"], "price": price["price"]})
    return extracted_prices
