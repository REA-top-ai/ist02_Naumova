from .API_methods import get_news_articles, filter_articles
import json


def fetch_and_filter_news(query: str = 'technology', days_back: int = 2):
    articles = get_news_articles(query=query, days_back=days_back)

    if not articles:
        print("No articles found from API")
        return []

    filtered = filter_articles(articles)
    return filtered


def save_news_to_file(filename: str = 'text.txt', query: str = 'technology'):
    news = fetch_and_filter_news(query=query)

    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(news, f, ensure_ascii=False, indent=2)

    print(f"Saved {len(news)} articles to {filename}")
    return news