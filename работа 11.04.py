import os
import requests
from datetime import datetime, timedelta
from mistralai.client import Mistral

# ==================== API КЛЮЧИ ====================
NEWSAPI_KEY = "69bb7e011b754dc4a2ca00c24e72a198"
MISTRAL_API_KEY = "W9JnQNBnrm4H5P8tXGg34troFVNB5h3G"


# ==================== ЧАСТЬ 1: ПОЛУЧЕНИЕ НОВОСТЕЙ ИЗ NEWSAPI ====================

def get_news_from_newsapi(topic, days_back=1):
    """
    Получает новости по заданной теме из NewsAPI за последние days_back дней

    Args:
        topic: тема для поиска (например, "technology", "business", "russia")
        days_back: количество дней назад (по умолчанию 1)

    Returns:
        list: список словарей с новостями
    """
    # Вычисляем дату
    from_date = (datetime.now() - timedelta(days=days_back)).strftime('%Y-%m-%d')

    # URL для запроса к NewsAPI
    url = f"https://newsapi.org/v2/everything"

    params = {
        'q': topic,
        'from': from_date,
        'sortBy': 'publishedAt',
        'language': 'ru',
        'apiKey': NEWSAPI_KEY,
        'pageSize': 20  # Максимум 20 статей для обработки
    }

    try:
        print(f"📡 Отправка запроса к NewsAPI по теме '{topic}'...")
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()

        if data['status'] == 'ok':
            articles = []
            for article in data['articles']:
                # Пропускаем новости без содержательного контента
                if article.get('title') == '[Removed]' or not article.get('title'):
                    continue

                articles.append({
                    'title': article.get('title', 'Без заголовка'),
                    'description': article.get('description', ''),
                    'content': article.get('content', ''),
                    'source': article.get('source', {}).get('name', 'Неизвестен'),
                    'published_at': article.get('publishedAt', ''),
                    'url': article.get('url', ''),
                    'author': article.get('author', 'Неизвестен')
                })

            print(f"✓ Найдено {len(articles)} новостей (всего в ответе: {data['totalResults']})")
            return articles
        else:
            print(f"❌ Ошибка NewsAPI: {data.get('message', 'Неизвестная ошибка')}")
            return []

    except requests.exceptions.RequestException as e:
        print(f"❌ Ошибка при запросе к NewsAPI: {e}")
        return []


# ==================== ЧАСТЬ 2: ГЕНЕРАЦИЯ АННОТАЦИИ ЧЕРЕЗ MISTRAL AI ====================

def generate_news_annotation(articles_data, topic):
    """
    Генерирует аналитическую аннотацию по новостям с помощью Mistral AI

    Args:
        articles_data: список словарей с новостями
        topic: тема новостей

    Returns:
        str: аннотация объёмом 250-300 слов на русском языке
    """

    if not articles_data:
        return "За последний день не найдено новостей по заданной теме."

    # Формируем текст из новостей с ограничением длины
    news_text = ""
    for i, article in enumerate(articles_data, 1):
        title = article.get('title', 'Без заголовка')
        description = article.get('description', '')
        content = article.get('content', '')

        # Ограничиваем длину контента
        if content and len(content) > 600:
            content = content[:600] + "..."

        # Добавляем дату публикации, если есть
        published_at = article.get('published_at', '')
        if published_at:
            try:
                pub_date = datetime.fromisoformat(published_at.replace('Z', '+00:00'))
                pub_date_str = pub_date.strftime('%d.%m.%Y %H:%M')
            except:
                pub_date_str = "Дата неизвестна"
        else:
            pub_date_str = "Дата неизвестна"

        news_text += f"\n{'=' * 60}\n"
        news_text += f"НОВОСТЬ {i}\n"
        news_text += f"📅 Время: {pub_date_str}\n"
        news_text += f"📰 Источник: {article.get('source', 'Неизвестен')}\n"
        news_text += f"✍️ Автор: {article.get('author', 'Не указан')}\n"
        news_text += f"📌 Заголовок: {title}\n"
        if description:
            news_text += f"📝 Описание: {description}\n"
        if content and content != "[Removed]":
            news_text += f"📄 Содержание: {content}\n"
        news_text += f"🔗 Ссылка: {article.get('url', 'Нет ссылки')}\n"

    # Промпт для Mistral AI
    prompt = f"""Ты — профессиональный аналитик новостей с 20-летним опытом. Твоя задача: проанализировать подборку новостей по теме "{topic}" за последние 24 часа и подготовить аналитическую аннотацию.

Вот новости для анализа:

{news_text}

ТРЕБОВАНИЯ К АННОТАЦИИ (строго соблюдай их):

1. ОБЪЁМ: 250-300 слов (ровно, не меньше и не больше)
2. ЯЗЫК: Только русский, литературный, деловой стиль
3. СТРУКТУРА:
   - Введение (2-3 предложения): общая характеристика информационной повестки
   - Основная часть (4-5 предложений): ключевые события и тренды
   - Анализ (3-4 предложения): что на самом деле произошло важного
   - Оценка (2-3 предложения): как события дня влияют на ситуацию
   - Прогноз (2-3 предложения): что ожидать в ближайшее время
4. Обязательно выдели 2-3 САМЫХ ВАЖНЫХ события с пояснением, почему они значимы
5. Добавь цифры, факты и конкретику из новостей
6. В конце сделай чёткий вывод по теме

Напиши аналитическую аннотацию на русском языке объёмом 250-300 слов.
Не используй клише и шаблонные фразы. Будь конкретным и фактологичным.
"""

    try:
        print("🤖 Отправка запроса к Mistral AI...")
        # Инициализация клиента Mistral AI
        client = Mistral(api_key=MISTRAL_API_KEY)

        # Отправка запроса
        chat_response = client.chat.complete(
            model="mistral-large-latest",
            messages=[
                {
                    "role": "system",
                    "content": "Ты — опытный аналитик новостей. Отвечай только на русском языке. Будь объективным, фактологичным, но при этом интересным. Избегай воды и общих фраз."
                },
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            temperature=0.3,
            max_tokens=1000
        )

        annotation = chat_response.choices[0].message.content
        print("✓ Аннотация успешно сгенерирована")
        return annotation

    except Exception as e:
        print(f"❌ Ошибка при обращении к Mistral AI: {e}")
        return f"Не удалось сгенерировать аннотацию из-за ошибки: {str(e)}"


# ==================== ЧАСТЬ 3: СОХРАНЕНИЕ В ФАЙЛ ====================

def save_annotation_to_file(annotation, filename="text.txt"):
    """
    Сохраняет аннотацию в текстовый файл
    """
    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(annotation)
        print(f"✓ Аннотация сохранена в файл: {filename}")
        return True
    except Exception as e:
        print(f"❌ Ошибка при сохранении файла: {e}")
        return False


# ==================== ОСНОВНАЯ ФУНКЦИЯ ====================

def main():
    """
    Основная функция: получает новости, генерирует аннотацию и сохраняет в файл
    """
    print("\n" + "=" * 70)
    print(" " * 20 + "📊 АНАЛИТИК НОВОСТЕЙ v1.0")
    print("=" * 70)

    # Ввод темы от пользователя
    print("\n💡 Примеры тем: 'Россия экономика', 'technology', 'бизнес', 'спорт', 'политика'")
    topic = input("\n🔍 Введите тему для анализа новостей: ").strip()

    if not topic:
        print("❌ Тема не может быть пустой! Использую тему по умолчанию: 'Россия'")
        topic = "Россия"

    print(f"\n📅 Анализируем новости за последние 24 часа по теме: '{topic}'")
    print("-" * 70)

    # Получаем новости
    articles = get_news_from_newsapi(topic, days_back=1)

    if not articles:
        print("\n❌ Новости не найдены. Возможные причины:")
        print("   - По теме '{topic}' нет новостей за последний день")
        print("   - Проблема с API-ключом NewsAPI")
        print("   - Превышен лимит запросов")
        return

    print(f"\n📊 Найдено {len(articles)} новостей для анализа")
    print("\n⏳ Генерация аналитической аннотации...")
    print("   (Это может занять 15-30 секунд)")
    print("-" * 70)

    # Генерируем аннотацию
    annotation = generate_news_annotation(articles, topic)

    # Выводим результат
    print("\n" + "=" * 70)
    print(" " * 20 + "📄 АНАЛИТИЧЕСКАЯ АННОТАЦИЯ")
    print("=" * 70)
    print(annotation)
    print("=" * 70)

    # Сохраняем в файл
    save_annotation_to_file(annotation, "text.txt")

    # Дополнительная статистика
    word_count = len(annotation.split())
    char_count = len(annotation)

    print(f"\n📈 СТАТИСТИКА:")
    print(f"   • Проанализировано новостей: {len(articles)}")
    print(f"   • Объём аннотации: {char_count} символов")
    print(f"   • Количество слов: {word_count}")

    if 250 <= word_count <= 300:
        print(f"   • Объём аннотации: ✅ ИДЕАЛЬНО (250-300 слов)")
    elif word_count < 250:
        print(f"   • Объём аннотации: ⚠️ МАЛОВАТО ({word_count} слов, нужно 250-300)")
    else:
        print(f"   • Объём аннотации: ⚠️ МНОГОВАТО ({word_count} слов, нужно 250-300)")

    print("\n" + "=" * 70)
    print("✅ ГОТОВО! Аннотация сохранена в файл 'text.txt'")
    print("=" * 70 + "\n")


# ==================== ТОЧКА ВХОДА ====================

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️ Программа прервана пользователем")
    except Exception as e:
        print(f"\n❌ Непредвиденная ошибка: {e}")
        print("Попробуйте перезапустить программу")