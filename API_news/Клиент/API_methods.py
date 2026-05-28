import requests
from datetime import datetime, timedelta
from typing import List, Dict, Any

API_KEY = "69bb7e011b754dc4a2ca00c24e72a198"


def get_news_articles(query: str = 'technology', days_back: int = 2, page_size: int = 50) -> List[Dict]:
    base_url = "https://newsapi.org/v2/everything"

    from_date = (datetime.now() - timedelta(days=days_back)).strftime('%Y-%m-%d')

    params = {
        'q': query,
        'from': from_date,
        'sortBy': 'publishedAt',
        'pageSize': page_size,
        'language': 'en',
        'apiKey': API_KEY
    }

    try:
        response = requests.get(base_url, params=params)
        print(f"URL: {response.url}")
        data = response.json()

        print(f"Status: {data.get('status')}")
        if data.get('message'):
            print(f"Message: {data.get('message')}")
        print(f"Total results: {data.get('totalResults', 0)}")

        if data.get('status') != 'ok':
            return []

        return data.get('articles', [])
    except Exception as e:
        print(f"Error: {e}")
        return []


def filter_articles(articles: List[Dict]) -> List[Dict[str, Any]]:
    filtered = []

    for article in articles:
        title = article.get('title', '').strip()
        url = article.get('url')

        if not title or title == "[Removed]":
            continue
        if not url:
            continue

        filtered.append({
            "title": title,
            "source": article.get('source', {}).get('name', 'Unknown'),
            "publishedat": article.get('publishedAt', ''),
            "author": article.get('author', 'Unknown') or 'Unknown'
        })

        if len(filtered) >= 50:
            break

    print(f"Filtered: {len(filtered)} articles")
    return filtered