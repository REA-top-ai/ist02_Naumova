import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from Клиент.newsAPI_mistral import fetch_and_filter_news, save_news_to_file


def main():
    print("=" * 50)
    print("News API Analyzer")
    print("=" * 50)

    query = input("Enter search query (default: technology): ").strip()
    if not query:
        query = 'technology'

    print(f"\nSearching for: {query}")
    print("Note: Free API has 24h delay. Trying with last 2 days...")

    articles = fetch_and_filter_news(query=query, days_back=2)

    print(f"\nTotal articles found: {len(articles)}")

    if articles:
        save_news_to_file('text.txt', query)

        print("\nFirst 5 articles:")
        for i, article in enumerate(articles[:5], 1):
            print(f"\n{i}. Title: {article['title']}")
            print(f"   Source: {article['source']}")
            print(f"   Date: {article['publishedat']}")
            print(f"   Author: {article['author']}")
    else:
        print("\nNo articles found. Possible reasons:")
        print("1. Free API has 24h delay - try again tomorrow")
        print("2. Try different query (e.g., 'apple', 'microsoft')")
        print("3. Check your API key at https://newsapi.org/account")

    return articles


if __name__ == "__main__":
    result = main()