from sqlalchemy.orm import Session
from sqlalchemy import func, desc
from models import Author, Post, Comment
from datetime import datetime


# ========== Функции для работы с авторами ==========

def create_author(session: Session, name: str, email: str):
    """Создает нового автора, возвращает объект"""
    new_author = Author(name=name, email=email)
    session.add(new_author)
    session.commit()
    session.refresh(new_author)
    return new_author


def get_author_by_email(session: Session, email: str):
    """Ищет автора по email"""
    return session.query(Author).filter(Author.email == email).first()


# Самостоятельная работа №1: Найти автора по имени
def get_author_by_name(session: Session, name: str):
    """Находит автора по имени"""
    return session.query(Author).filter(Author.name == name).first()


# Самостоятельная работа №3: Добавление сразу нескольких авторов
def create_multiple_authors(session: Session, authors_data):
    """Добавляет сразу нескольких авторов в БД"""
    authors = []
    for data in authors_data:
        author = Author(name=data['name'], email=data['email'])
        session.add(author)
        authors.append(author)
    session.commit()
    for author in authors:
        session.refresh(author)
    return authors


# ========== Функции для работы с постами ==========

def create_post(session: Session, title: str, content: str, author_id: int, published: bool = False):
    """Создает новый пост"""
    new_post = Post(
        title=title,
        content=content,
        author_id=author_id,
        published=published
    )
    session.add(new_post)
    session.commit()
    session.refresh(new_post)
    return new_post


def get_published_posts(session: Session, limit: int = 10):
    """Возвращает только опубликованные посты (published=True)"""
    return session.query(Post).filter(Post.published == True).limit(limit).all()


def get_posts_by_author(session: Session, author_id: int, limit: int = 10):
    """Возвращает все посты конкретного автора"""
    return session.query(Post).filter(Post.author_id == author_id).limit(limit).all()


# Самостоятельная работа №2: Посты за определенную дату
def get_posts_by_date(session: Session, date: datetime, published_only: bool = True):
    """Выводит опубликованные посты за определенную дату"""
    start_of_day = datetime(date.year, date.month, date.day, 0, 0, 0)
    end_of_day = datetime(date.year, date.month, date.day, 23, 59, 59)

    query = session.query(Post).filter(
        Post.created_at >= start_of_day,
        Post.created_at <= end_of_day
    )

    if published_only:
        query = query.filter(Post.published == True)

    return query.all()


def update_post_status(session: Session, post_id: int, published: bool):
    """Меняет статус публикации поста, возвращает True если успешно"""
    post = session.query(Post).filter(Post.id == post_id).first()
    if post is None:
        return False
    post.published = published
    session.commit()
    return True


# Самостоятельная работа №4: Пост с комментариями
def get_post_with_comments(session: Session, post_id: int):
    """Находит пост по id и выводит сам пост и комментарии к нему"""
    post = session.query(Post).filter(Post.id == post_id).first()
    if post is None:
        return None
    return {'post': post, 'comments': post.comments}


# ========== Функции для работы с комментариями ==========

def add_comment(session: Session, post_id: int, author_name: str, text: str):
    """Добавляет комментарий к посту"""
    new_comment = Comment(
        post_id=post_id,
        author_name=author_name,
        text=text
    )
    session.add(new_comment)
    session.commit()
    session.refresh(new_comment)
    return new_comment


# ========== Аналитические функции ==========

def get_top_authors_by_posts(session: Session, limit: int = 5):
    """Возвращает топ авторов по количеству созданных постов"""
    result = (
        session.query(
            Author.name,
            func.count(Post.id).label('post_count')
        )
        .join(Post)
        .group_by(Author.id)
        .order_by(desc('post_count'))
        .limit(limit)
        .all()
    )
    return result