import os
# Модуль для работы с операционной системой. Нужен для чтения переменных окружения из файла .env

import psycopg2
# Библиотека для подключения к PostgreSQL. Позволяет Python'у отправлять запросы в базу данных

from psycopg2.extras import RealDictCursor
# Специальный тип курсора, который возвращает результат запроса в виде словаря (например: {'name': 'Альбина', 'age': 20})
# вместо кортежа (пример: ('Альбина', 20)). Так удобнее обращаться к данным по имени колонки

from flask import Flask, request, jsonify, session, redirect, url_for, render_template
# Flask - создаёт само веб-приложение
# request - получает данные от браузера (JSON, параметры запроса)
# jsonify - превращает Python-словарь в JSON-строку для отправки в браузер
# session - хранит данные пользователя между разными запросами (например, email после входа)
# redirect - перенаправляет пользователя на другой URL
# url_for - генерирует URL по имени функции (например, url_for('index') вернёт '/')
# render_template - загружает HTML-файл из папки templates и отправляет его в браузер

import requests
# Библиотека для отправки HTTP-запросов к внешним API (CalorieNinjas - поиск калорий, Mistral AI - советы)

from datetime import date
# Модуль для работы с датами. date.today() возвращает текущую дату (нужна для фильтрации блюд по дням)

from functools import wraps
# Вспомогательная функция для создания декораторов. Сохраняет имя и документацию оригинальной функции

from dotenv import load_dotenv

# Загружает переменные из файла .env в переменные окружения. Нужно для безопасности (чтобы ключи не хранить в коде)


# ============================================================================
# ЗАГРУЗКА ПЕРЕМЕННЫХ ИЗ .env
# ============================================================================

load_dotenv()
# Ищет файл .env в корне проекта и загружает все переменные оттуда


# ============================================================================
# СОЗДАНИЕ ПРИЛОЖЕНИЯ FLASK
# ============================================================================

app = Flask(__name__)
# Создаёт экземпляр Flask-приложения. __name__ - имя текущего модуля (нужно Flask'у для поиска файлов)

app.secret_key = os.getenv('SECRET_KEY')
# Устанавливает секретный ключ для подписи сессий (берётся из .env). Без него сессии не будут работать


# ============================================================================
# КЛЮЧИ API (ЗАГРУЖАЮТСЯ ИЗ .env)
# ============================================================================

GOOGLE_CLIENT_ID = os.getenv('GOOGLE_CLIENT_ID')
# Идентификатор приложения в Google. По нему Google понимает, какое приложение запрашивает доступ

GOOGLE_CLIENT_SECRET = os.getenv('GOOGLE_CLIENT_SECRET')
# Секретный ключ для подтверждения, что запрос действительно от нашего приложения

CALORIE_NINJAS_KEY = os.getenv('CALORIE_NINJAS_KEY')
# Ключ для доступа к CalorieNinjas API (сервис, который ищет калорийность продуктов по названию)

MISTRAL_API_KEY = os.getenv('MISTRAL_API_KEY')
# Ключ для доступа к Mistral AI (нейросеть, которая даёт персональные советы по питанию)

DB_CONFIG = {
    'host': os.getenv('DB_HOST', 'localhost'),
    # Адрес сервера базы данных. localhost - значит PostgreSQL установлен на этом же компьютере

    'database': os.getenv('DB_NAME', 'calorie_app_pg'),
    # Имя базы данных. Все данные пользователей и блюд хранятся в этой базе

    'user': os.getenv('DB_USER', 'postgres'),
    # Имя пользователя для подключения к PostgreSQL. postgres - стандартный администратор

    'password': os.getenv('DB_PASSWORD'),
    # Пароль для подключения. Обязательно хранится в .env, а не в коде!

    'port': os.getenv('DB_PORT', '5432')
    # Порт PostgreSQL. 5432 - стандартный порт для этой СУБД
}


def get_db():
    return psycopg2.connect(**DB_CONFIG)
    # Создаёт и возвращает соединение с базой данных.
    # **DB_CONFIG распаковывает словарь в параметры функции (как если бы их написали вручную)


def init_db():
    with get_db() as conn:
        # with гарантирует, что соединение автоматически закроется после выхода из блока
        # даже если произойдёт ошибка

        cur = conn.cursor()
        # Создаёт курсор - объект, через который выполняются SQL-запросы

        cur.execute(
            'CREATE TABLE IF NOT EXISTS users (email TEXT PRIMARY KEY, name TEXT, current_weight REAL, target_weight REAL, age INTEGER, height INTEGER)')
        # Создаёт таблицу пользователей, если её ещё нет.
        # email - почта (главный ключ, уникальный)
        # name - имя пользователя
        # current_weight - текущий вес (REAL - дробное число)
        # target_weight - целевой вес
        # age - возраст (INTEGER - целое число)
        # height - рост в сантиметрах

        cur.execute(
            'CREATE TABLE IF NOT EXISTS meals (id SERIAL PRIMARY KEY, email TEXT, food_name TEXT, calories INTEGER, meal_type TEXT, date TEXT)')
        # Создаёт таблицу приёмов пищи.
        # id - автоматически увеличивающийся номер (SERIAL)
        # email - кто добавил (связь с таблицей users)
        # food_name - название блюда
        # calories - количество калорий
        # meal_type - тип приёма (breakfast/lunch/dinner)
        # date - дата добавления (например, '2025-05-30')

        conn.commit()
        # Сохраняет все изменения в базе данных. Без commit() данные не запишутся!

    print("База готова")
    # Выводит сообщение в терминал при запуске, чтобы мы знали, что всё прошло успешно


init_db()


# Вызывает функцию инициализации при старте приложения (создаёт таблицы, если их нет)


def login_required(f):
    # Это декоратор - функция, которая оборачивает другую функцию.
    # Он проверяет, вошёл ли пользователь, и если нет - возвращает ошибку.

    @wraps(f)
    # Сохраняет имя и документацию оригинальной функции (без этого декоратор сломает отладку)

    def decorated(*args, **kwargs):
        # Внутренняя функция-обёртка

        if 'email' not in session:
            # Проверяем, есть ли в сессии email пользователя.
            # session - это словарь, который хранится на сервере и связан с конкретным браузером

            return jsonify({'error': 'Unauthorized'}), 401
            # Если нет - возвращаем ошибку 401 (Не авторизован)

        return f(*args, **kwargs)
        # Если есть - вызываем оригинальную функцию

    return decorated
    # Возвращаем обёрнутую функцию

def search_food(query):
    # Принимает название продукта, возвращает список с калориями

    try:
        # try/except - перехватываем ошибки (например, нет интернета)

        r = requests.get(f"https://api.calorieninjas.com/v1/nutrition?query={query}",
                         headers={'X-Api-Key': CALORIE_NINJAS_KEY}, timeout=10)
        # Отправляем GET-запрос к CalorieNinjas API.
        # f-string подставляет название продукта в URL.
        # headers - передаём API-ключ для авторизации.
        # timeout=10 - ждём ответ не больше 10 секунд

        if r.status_code == 200:
            # 200 - статус "Успешно" (сервер вернул данные)

            return [{'name': i.get('name'), 'calories': round(i.get('calories', 0))} for i in r.json().get('items', [])]
            # Извлекаем из ответа список продуктов.
            # i.get('name') - название продукта
            # i.get('calories') - калории
            # round() - округляем до целого числа
            # Возвращаем список словарей

    except:
        pass
        # При любой ошибке возвращаем пустой список

    return []


def calc_bmr(w, h, a):
    # w - вес в кг, h - рост в см, a - возраст в годах
    # Формула Миффлина-Сан-Жеора для мужчин

    return round(10 * w + 6.25 * h - 5 * a + 5)
    # Рассчитывает, сколько калорий нужно в день для поддержания веса
    # round() - округляет до целого числа


@app.route('/')
# Декоратор, который связывает URL '/' (корень сайта) с функцией ниже.
# Когда пользователь заходит на http://localhost:5000, вызывается эта функция

def index():
    return render_template('index.html')
    # Загружает файл index.html из папки templates и отправляет его в браузер


@app.route('/api/me')
# URL для получения информации о текущем пользователе

def api_me():
    if 'email' not in session:
        # Если пользователь не авторизован (нет email в сессии)

        return jsonify({'authenticated': False})
        # Возвращаем JSON с пометкой, что не авторизован

    with get_db() as conn:
        # Подключаемся к базе данных

        cur = conn.cursor(cursor_factory=RealDictCursor)
        # Создаём курсор, который возвращает результаты в виде словарей

        cur.execute('SELECT name, current_weight, target_weight, age, height FROM users WHERE email = %s',
                    (session['email'],))
        # Выполняем SQL-запрос: выбираем данные пользователя по его email.
        # %s - плейсхолдер, вместо него подставится email (защита от SQL-инъекций)

        u = cur.fetchone()
        # fetchone() - берёт первую (и единственную) запись из результата

        if u:
            # Если пользователь найден в базе данных

            return jsonify({
                'authenticated': True,  # Пользователь авторизован
                'email': session['email'],  # Email из сессии
                'name': u['name'],  # Имя из базы данных
                'has_profile': True,  # Профиль заполнен
                'current_weight': u['current_weight'] or 0,  # Вес (или 0 если пусто)
                'target_weight': u['target_weight'] or 0,  # Целевой вес
                'age': u['age'] or 0,  # Возраст
                'height': u['height'] or 0  # Рост
            })

        return jsonify({'authenticated': True, 'email': session['email'], 'has_profile': False})
        # Пользователь авторизован, но профиль не заполнен

@app.route('/api/set_profile', methods=['POST'])
# URL для сохранения профиля. methods=['POST'] - принимает только POST-запросы

@login_required
# Применяем декоратор - требует авторизации

def api_set_profile():
    data = request.json
    # Получаем JSON-данные из тела запроса (имя, вес, возраст и т.д.)

    with get_db() as conn:
        cur = conn.cursor()

        cur.execute(
            'INSERT INTO users (email, name, current_weight, target_weight, age, height) VALUES (%s,%s,%s,%s,%s,%s) ON CONFLICT (email) DO UPDATE SET name=EXCLUDED.name, current_weight=EXCLUDED.current_weight, target_weight=EXCLUDED.target_weight, age=EXCLUDED.age, height=EXCLUDED.height',
            (session['email'], data['name'], data['current_weight'], data['target_weight'], data['age'],
             data['height']))
        # Вставляем данные в таблицу users.
        # ON CONFLICT - если пользователь с таким email уже есть, не создаём новый,
        # а обновляем существующую запись (заменяем имя, вес и т.д.)

        conn.commit()
        # Сохраняем изменения

    session['name'] = data['name']
    # Обновляем имя в сессии

    return jsonify({'status': 'ok'})
    # Возвращаем успешный статус


@app.route('/api/search', methods=['POST'])
@login_required
def api_search():
    return jsonify({'results': search_food(request.json.get('query'))})
    # Получаем запрос (название продукта), вызываем search_food(), возвращаем результат

@app.route('/api/add_meal', methods=['POST'])
@login_required
def api_add_meal():
    data = request.json
    # Получаем данные о блюде (название, калории, тип приёма)

    with get_db() as conn:
        cur = conn.cursor()

        cur.execute('INSERT INTO meals (email, food_name, calories, meal_type, date) VALUES (%s,%s,%s,%s,%s)',
                    (session['email'], data['food_name'], data['calories'], data['meal_type'], str(date.today())))
        # Вставляем новую запись в таблицу meals.
        # email - берётся из сессии (кто добавил)
        # date - сегодняшняя дата (чтобы не показывать блюда из прошлых дней)

        conn.commit()

    return jsonify({'status': 'ok'})


@app.route('/api/delete_meal', methods=['POST'])
@login_required
def api_delete_meal():
    data = request.json

    with get_db() as conn:
        cur = conn.cursor()

        cur.execute('DELETE FROM meals WHERE id = %s AND email = %s', (data['meal_id'], session['email']))
        # Удаляем блюдо из таблицы.
        # Два условия: id блюда И email текущего пользователя.
        # Это защита - пользователь может удалить только своё блюдо, даже если узнает чужой id

        conn.commit()

    return jsonify({'status': 'ok'})


@app.route('/api/get_meals')
@login_required
def api_get_meals():
    with get_db() as conn:
        cur = conn.cursor(cursor_factory=RealDictCursor)

        cur.execute('SELECT id, food_name, calories, meal_type FROM meals WHERE email = %s AND date = %s',
                    (session['email'], str(date.today())))
        # Выбираем все блюда текущего пользователя за сегодня.
        # id нужен для удаления, food_name - название, calories - калории, meal_type - завтрак/обед/ужин

        return jsonify({'meals': cur.fetchall()})
        # fetchall() - получаем все записи и возвращаем в виде JSON

@app.route('/api/advice')
@login_required
def api_advice():
    with get_db() as conn:
        cur = conn.cursor()

        cur.execute('SELECT calories, food_name, meal_type FROM meals WHERE email = %s AND date = %s',
                    (session['email'], str(date.today())))
        # Получаем все блюда пользователя за сегодня

        meals = cur.fetchall()
        # Сохраняем их в переменную

        cur.execute('SELECT name, current_weight, target_weight, age, height FROM users WHERE email = %s',
                    (session['email'],))
        # Получаем данные пользователя из таблицы users

        user = cur.fetchone()

    total = sum(m[0] for m in meals)
    # Считаем общее количество калорий за сегодня (суммируем все calories из meals)

    if not user or not user[1]:
        # Если профиль не заполнен (нет веса, роста, возраста)

        return jsonify({'advice': f"За сегодня {total} ккал. Заполните профиль!"})
        # Возвращаем простой совет с просьбой заполнить профиль

    bmr = calc_bmr(user[1], user[4], user[3])
    # Рассчитываем норму калорий на основе веса, роста и возраста

    meals_list = "\n".join([f"- {m[1]} ({m[2]}): {m[0]} ккал" for m in meals]) or "Пока ничего"
    # Формируем красивый список блюд для отправки в нейросеть

    prompt = f"""Диетолог. Дай развёрнутый совет (800-1500 символов).
Данные: {user[0]}, вес {user[1]}кг, цель {user[2]}кг, возраст {user[3]} лет, рост {user[4]}см. Норма {bmr} ккал.
Сегодня: {total} ккал ({'+' if total > bmr else ''}{total - bmr} от нормы).
Блюда:\n{meals_list}
Напиши: 1) анализ рациона 2) сколько добавить/убавить 3) примеры продуктов (5-7 шт) 4) совет по активности 5) мотивацию"""
    # Формируем запрос к нейросети. Нейросеть получит всю информацию о пользователе и его рационе

    try:
        r = requests.post("https://api.mistral.ai/v1/chat/completions",
                          headers={"Authorization": f"Bearer {MISTRAL_API_KEY}"},
                          json={"model": "mistral-small-latest", "messages": [{"role": "user", "content": prompt}],
                                "max_tokens": 1500}, timeout=30)
        # Отправляем POST-запрос к Mistral AI.
        # headers - передаём API-ключ
        # model - какая версия нейросети (mistral-small-latest - быстрая и качественная)
        # messages - список сообщений (role: user - от пользователя, content - текст запроса)
        # max_tokens - максимальная длина ответа (1500 токенов ~ 1000-1200 символов)
        # timeout=30 - ждём ответ не больше 30 секунд

        advice = r.json()['choices'][0]['message'][
            'content'] if r.status_code == 200 else f"За сегодня {total} ккал. Норма {bmr} ккал."
        # Если запрос успешен (status_code 200) - извлекаем ответ нейросети.
        # Если нет - возвращаем простой базовый совет

    except:
        advice = f"За сегодня {total} ккал. Норма {bmr} ккал."
        # Если произошла ошибка (нет интернета, проблема с API) - возвращаем простой совет

    return jsonify({'advice': advice})
    # Возвращаем совет в виде JSON

@app.route('/google/login')
# URL для начала процесса входа через Google

def google_login():
    return redirect(
        f"https://accounts.google.com/o/oauth2/v2/auth?client_id={GOOGLE_CLIENT_ID}&redirect_uri={url_for('google_callback', _external=True)}&response_type=code&scope=email%20profile")
    # Перенаправляет пользователя на страницу входа Google.
    # client_id - идентификатор нашего приложения
    # redirect_uri - куда Google вернёт пользователя после входа (на /google/callback)
    # response_type=code - запрашиваем код авторизации
    # scope=email profile - запрашиваем доступ к email и базовой информации профиля


@app.route('/google/callback')
# URL, куда Google перенаправляет после успешного входа

def google_callback():
    code = request.args.get('code')
    # Получаем код авторизации из параметров запроса

    if not code:
        return "Ошибка", 400
        # Если кода нет - возвращаем ошибку

    r = requests.post("https://oauth2.googleapis.com/token",
                      data={'code': code, 'client_id': GOOGLE_CLIENT_ID, 'client_secret': GOOGLE_CLIENT_SECRET,
                            'redirect_uri': url_for('google_callback', _external=True),
                            'grant_type': 'authorization_code'})
    # Обмениваем код авторизации на access_token.
    # POST-запрос к Google с нашими ключами и полученным кодом

    if r.status_code != 200:
        return "Ошибка токена", 400
        # Если не удалось получить токен - возвращаем ошибку

    userinfo = requests.get('https://www.googleapis.com/oauth2/v2/userinfo',
                            headers={'Authorization': f'Bearer {r.json()["access_token"]}'}).json()
    # Используем access_token, чтобы получить информацию о пользователе (email)

    session['email'] = userinfo['email']
    # Сохраняем email в сессию. ЭТО ГЛАВНАЯ СТРОЧКА - ОНА ОЗНАЧАЕТ, ЧТО ПОЛЬЗОВАТЕЛЬ ВОШЁЛ!

    return redirect('/')
    # Перенаправляем на главную страницу

if __name__ == '__main__':
    # Это условие означает: "если этот файл запущен напрямую, а не импортирован как библиотека"

    app.run(debug=True, port=5000)
    # Запускает Flask-сервер.
    # debug=True - режим отладки (при изменении кода сервер перезапустится автоматически)
    # port=5000 - порт, на котором будет доступно приложение (http://localhost:5000)