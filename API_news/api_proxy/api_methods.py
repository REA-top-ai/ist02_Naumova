import json
import os
from datetime import datetime

CACHE_FILE = 'news_cache.json'


def proxy_request(api_func, *args, **kwargs):
    print(f"Proxy: Executing request to NewsAPI")
    result = api_func(*args, **kwargs)
    print(f"Proxy: Request completed, got {len(result)} articles")
    return result


def get_cached_news(query: str, use_cache: bool = True):
    if not use_cache:
        return None

    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, 'r', encoding='utf-8') as f:
            cache = json.load(f)

        cache_time = cache.get('timestamp', '')
        cache_query = cache.get('query', '')
        cache_data = cache.get('data', [])

        if cache_query == query and cache_data:
            print(f"Using cached data for query: {query}")
            return cache_data

    return None


def save_to_cache(query: str, data: list):
    cache = {
        'timestamp': datetime.now().isoformat(),
        'query': query,
        'data': data
    }

    with open(CACHE_FILE, 'w', encoding='utf-8') as f:
        json.dump(cache, f, ensure_ascii=False, indent=2)

    print(f"Saved to cache: {len(data)} articles")