from flask import Flask, request, jsonify, session, redirect, url_for, render_template
import sqlite3
import requests
from datetime import date
from functools import wraps

app = Flask(__name__)
app.secret_key = 'secret-key-12345'

# ===== КЛЮЧИ =====
GOOGLE_CLIENT_ID = "225866641134-gtkghk8qingah1469bop246nftip4sm2.apps.googleusercontent.com"
GOOGLE_CLIENT_SECRET = "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"
CALORIE_NINJAS_KEY = "D5ZCalVxPn86EBhSzS1Zaw==pLBd250i0PxC4GiP"
MISTRAL_API_KEY = "W9JnQNBnrm4H5P8tXGg34troFVNB5h3G"

# ===== БАЗА ДАННЫХ =====
def get_db():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    with get_db() as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS users (
                email TEXT PRIMARY KEY,
                name TEXT,
                current_weight REAL,
                target_weight REAL,
                age INTEGER,
                height INTEGER
            )
        ''')
        conn.execute('''
            CREATE TABLE IF NOT EXISTS meals (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT,
                food_name TEXT,
                calories INTEGER,
                meal_type TEXT,
                date TEXT
            )
        ''')
        conn.commit()
    print("База данных создана")

init_db()

def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if 'email' not in session:
            return jsonify({'error': 'Unauthorized'}), 401
        return f(*args, **kwargs)
    return decorated

def search_food(query):
    url = "https://api.calorieninjas.com/v1/nutrition"
    headers = {'X-Api-Key': CALORIE_NINJAS_KEY}
    params = {'query': query}
    try:
        r = requests.get(url, headers=headers, params=params, timeout=10)
        if r.status_code == 200:
            items = r.json().get('items', [])
            return [{'name': i.get('name'), 'calories': round(i.get('calories', 0))} for i in items]
    except:
        pass
    return []

def calculate_bmr(weight, height, age):
    try:
        return round(10 * float(weight) + 6.25 * float(height) - 5 * float(age) + 5)
    except:
        return 2000

def get_mistral_advice(user_data, total_calories):
    if not user_data or not user_data.get('current_weight'):
        return f"За сегодня {total_calories} ккал. Заполните профиль (вес, рост, возраст) для советов."

    try:
        bmr = calculate_bmr(user_data['current_weight'], user_data['height'], user_data['age'])
        diff = bmr - total_calories

        prompt = f"""Короткий совет диетолога (600-1000 символов):

Вес: {user_data['current_weight']} кг, цель: {user_data['target_weight']} кг
Норма: {bmr} ккал, сегодня: {total_calories} ккал

Напиши кратко: оценку, сколько добавить/убавить, 2-3 продукта, совет по активности."""

        r = requests.post(
            "https://api.mistral.ai/v1/chat/completions",
            headers={"Authorization": f"Bearer {MISTRAL_API_KEY}", "Content-Type": "application/json"},
            json={
                "model": "mistral-small-latest",
                "messages": [{"role": "user", "content": prompt}],
                "max_tokens": 300,
                "temperature": 0.5
            },
            timeout=15
        )
        if r.status_code == 200:
            result = r.json()['choices'][0]['message']['content']
            return result.strip()
        else:
            return get_basic_advice(bmr, total_calories)
    except Exception as e:
        return get_basic_advice(bmr if 'bmr' in locals() else 2000, total_calories)

def get_basic_advice(bmr, total):
    diff = bmr - total
    if diff > 300:
        return f"{total} ккал сегодня. Добавьте {diff} ккал: орехи, банан, йогурт."
    elif diff < -300:
        return f"{total} ккал сегодня. Перебор {abs(diff)} ккал. Уменьшите порции."
    return f"{total} ккал сегодня. Хороший день!"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/me')
def api_me():
    if 'email' in session:
        try:
            with get_db() as conn:
                user = conn.execute('SELECT name, current_weight, target_weight, age, height FROM users WHERE email = ?',
                                    (session['email'],)).fetchone()
                if user:
                    return jsonify({
                        'authenticated': True,
                        'email': session['email'],
                        'name': user['name'] if user['name'] else session['email'],
                        'has_profile': True,
                        'current_weight': user['current_weight'] if user['current_weight'] else 0,
                        'target_weight': user['target_weight'] if user['target_weight'] else 0,
                        'age': user['age'] if user['age'] else 0,
                        'height': user['height'] if user['height'] else 0
                    })
                return jsonify({'authenticated': True, 'email': session['email'], 'has_profile': False})
        except Exception as e:
            print(f"Ошибка: {e}")
            return jsonify({'authenticated': True, 'email': session['email'], 'has_profile': False})
    return jsonify({'authenticated': False})

@app.route('/api/set_profile', methods=['POST'])
@login_required
def api_set_profile():
    data = request.json
    with get_db() as conn:
        conn.execute('''INSERT OR REPLACE INTO users (email, name, current_weight, target_weight, age, height) 
                        VALUES (?, ?, ?, ?, ?, ?)''',
                     (session['email'], data['name'], data['current_weight'],
                      data['target_weight'], data['age'], data['height']))
        conn.commit()
    session['name'] = data['name']
    return jsonify({'status': 'ok'})

@app.route('/api/search', methods=['POST'])
@login_required
def api_search():
    query = request.json.get('query')
    results = search_food(query)
    return jsonify({'results': results})

@app.route('/api/add_meal', methods=['POST'])
@login_required
def api_add_meal():
    data = request.json
    today = str(date.today())
    with get_db() as conn:
        conn.execute(
            'INSERT INTO meals (email, food_name, calories, meal_type, date) VALUES (?, ?, ?, ?, ?)',
            (session['email'], data['food_name'], data['calories'], data['meal_type'], today)
        )
        conn.commit()
    print(f"Добавлено: {data['food_name']} - {data['calories']} ккал")
    return jsonify({'status': 'ok'})

@app.route('/api/get_meals')
@login_required
def api_get_meals():
    today = str(date.today())
    with get_db() as conn:
        meals = conn.execute(
            'SELECT food_name, calories, meal_type FROM meals WHERE email = ? AND date = ?',
            (session['email'], today)
        ).fetchall()
    return jsonify({'meals': [dict(m) for m in meals]})

@app.route('/api/advice')
@login_required
def api_advice():
    today = str(date.today())
    with get_db() as conn:
        user = conn.execute('SELECT name, current_weight, target_weight, age, height FROM users WHERE email = ?',
                            (session['email'],)).fetchone()
        meals = conn.execute('SELECT calories FROM meals WHERE email = ? AND date = ?',
                            (session['email'], today)).fetchall()
    total_calories = sum(m['calories'] for m in meals)
    user_data = dict(user) if user else None
    advice = get_mistral_advice(user_data, total_calories)
    return jsonify({'advice': advice})

@app.route('/google/login')
def google_login():
    redirect_uri = url_for('google_callback', _external=True)
    return redirect(f"https://accounts.google.com/o/oauth2/v2/auth?client_id={GOOGLE_CLIENT_ID}&redirect_uri={redirect_uri}&response_type=code&scope=email%20profile")

@app.route('/google/callback')
def google_callback():
    code = request.args.get('code')
    if not code:
        return "Ошибка", 400
    redirect_uri = url_for('google_callback', _external=True)
    r = requests.post("https://oauth2.googleapis.com/token", data={
        'code': code,
        'client_id': GOOGLE_CLIENT_ID,
        'client_secret': GOOGLE_CLIENT_SECRET,
        'redirect_uri': redirect_uri,
        'grant_type': 'authorization_code'
    })
    if r.status_code != 200:
        return "Ошибка получения токена", 400
    access_token = r.json()['access_token']
    userinfo = requests.get('https://www.googleapis.com/oauth2/v2/userinfo',
                            headers={'Authorization': f'Bearer {access_token}'}).json()
    session['email'] = userinfo['email']
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True, port=5000)



