from database import SessionLocal, engine, Base
from models import Author, Post, Comment
from crud import *
from datetime import datetime


def main():
    # Создаём таблицы, если их нет
    Base.metadata.create_all(bind=engine)

    # Создаём сессию для работы с БД
    session = SessionLocal()

    try:
        print("=" * 60)
        print("НАЧИНАЕМ ТЕСТИРОВАНИЕ БЛОГА")
        print("=" * 60)

        # 1. Создаём тестовых авторов
        print("\n1. Создаём авторов...")
        author1 = create_author(session, "Анна Петрова", "anna@example.com")
        author2 = create_author(session, "Иван Сидоров", "ivan@example.com")
        print(f"   Создан: {author1.name} (id={author1.id})")
        print(f"   Создан: {author2.name} (id={author2.id})")

        # 2. Создаём посты
        print("\n2. Создаём посты...")
        post1 = create_post(session, "Первый пост", "Это содержание первого поста.",
                            author1.id, published=True)
        post2 = create_post(session, "Черновик", "Этот пост пока не опубликован.",
                            author1.id, published=False)
        post3 = create_post(session, "Пост Ивана", "Текст от Ивана.",
                            author2.id, published=True)
        print(f"   '{post1.title}' (опубликован)")
        print(f"   '{post2.title}' (черновик)")
        print(f"   '{post3.title}' (опубликован)")

        # 3. Добавляем комментарии
        print("\n3. Добавляем комментарии...")
        add_comment(session, post1.id, "Читатель1", "Отличная статья!")
        add_comment(session, post1.id, "Читатель2", "Спасибо за материал!")
        add_comment(session, post1.id, "Аноним", "Коротко.")
        print("   Добавлено 3 комментария к первому посту")

        # 4. Публикуем черновик
        print("\n4. Публикуем черновик...")
        success = update_post_status(session, post2.id, published=True)
        if success:
            print(f"   '{post2.title}' теперь опубликован")

        # 5. Выводим все опубликованные посты
        print("\n5. Все опубликованные посты:")
        published_posts = get_published_posts(session)
        for post in published_posts:
            print(f"   '{post.title}' - автор: {post.author.name}")

        # 6. Топ авторов по количеству постов
        print("\n6. Топ авторов по количеству постов:")
        top_authors = get_top_authors_by_posts(session, limit=3)
        for rank, (name, count) in enumerate(top_authors, 1):
            print(f"   {rank}. {name}: {count} пост(ов)")

        # 7. Поиск автора по email
        print("\n7. Поиск автора по email...")
        found = get_author_by_email(session, "anna@example.com")
        if found:
            print(f"   Найдено: {found.name}")

        # ========== ТЕСТИРОВАНИЕ НОВЫХ ФУНКЦИЙ ==========
        print("\n" + "=" * 60)
        print("ТЕСТИРОВАНИЕ НОВЫХ ФУНКЦИЙ")
        print("=" * 60)

        # 8. Поиск автора по имени (№1)
        print("\n8. Поиск автора по имени:")
        found_by_name = get_author_by_name(session, "Иван Сидоров")
        if found_by_name:
            print(f"   Найден автор: {found_by_name.name}, email: {found_by_name.email}")

        # 9. Посты за определенную дату (№2)
        print("\n9. Посты за сегодняшнюю дату:")
        today_posts = get_posts_by_date(session, datetime.utcnow(), published_only=True)
        if today_posts:
            for post in today_posts:
                print(f"   '{post.title}'")
        else:
            print("   Нет опубликованных постов за эту дату")

        # 10. Добавление нескольких авторов (№3)
        print("\n10. Добавление нескольких авторов одновременно:")
        new_authors_data = [
            {"name": "Петр Иванов", "email": "petr@example.com"},
            {"name": "Мария Смирнова", "email": "maria@example.com"}
        ]
        new_authors = create_multiple_authors(session, new_authors_data)
        for author in new_authors:
            print(f"   Создан автор: {author.name} (id={author.id})")

        # 11. Получение поста с комментариями (№4)
        print(f"\n11. Получение поста с комментариями (id={post1.id}):")
        post_with_comments = get_post_with_comments(session, post1.id)
        if post_with_comments:
            post_obj = post_with_comments['post']
            comments = post_with_comments['comments']
            print(f"   Пост: '{post_obj.title}'")
            print(f"   Комментарии ({len(comments)} шт.):")
            for comment in comments:
                print(f"      - {comment.author_name}: {comment.text}")

        print("\n" + "=" * 60)
        print("ВСЕ ТЕСТЫ УСПЕШНО ЗАВЕРШЕНЫ")
        print("=" * 60)

    except Exception as e:
        print(f"\nОшибка: {e}")
        session.rollback()
    finally:
        session.close()
        print("\nСессия закрыта.")


if __name__ == "__main__":
    main()