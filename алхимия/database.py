import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Загружаем переменные из файла .env
load_dotenv()

# Читаем переменные окружения (с значениями по умолчанию)
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "postgres")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "blog_db")

# Формируем строку подключения для SQLAlchemy
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Создаем движок подключения к БД
engine = create_engine(DATABASE_URL, echo=False)

# Создаем фабрику сессий
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

# Создаем базовый класс для моделей
Base = declarative_base()
