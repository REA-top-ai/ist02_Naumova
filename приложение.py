from flask import Flask, redirect, request, session, jsonify
import requests

app = Flask(__name__)
app.secret_key = 'секретный_ключ_12345'

# ========== ВСТАВЬ СВОИ ДАННЫЕ ИЗ КОНСОЛИ GOOGLE ==========
GOOGLE_CLIENT_ID = '114946699795-mpn4aoi29264bfkkb2qhunh76ngj1sap.apps.googleusercontent.com'
GOOGLE_CLIENT_SECRET = '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'
# ===========================================================

# URL для перенаправления после авторизации
REDIRECT_URI = 'http://localhost:5000/callback'


@app.route('/')
def index():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Вход через Google</title>
        <meta charset="utf-8">
        <style>
            body {
                font-family: Arial, sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            }
            .container {
                background: white;
                padding: 40px;
                border-radius: 20px;
                box-shadow: 0 10px 40px rgba(0,0,0,0.2);
                text-align: center;
                max-width: 500px;
            }
            .login-btn {
                background-color: #4285F4;
                color: white;
                border: none;
                padding: 12px 30px;
                font-size: 16px;
                border-radius: 5px;
                cursor: pointer;
            }
            .logout-btn {
                background-color: #dc3545;
                color: white;
                border: none;
                padding: 10px 25px;
                font-size: 14px;
                border-radius: 5px;
                cursor: pointer;
                margin-top: 20px;
            }
            .user-avatar {
                border-radius: 50%;
                width: 80px;
                height: 80px;
            }
        </style>
    </head>
    <body>
        <div class="container" id="app">
            <div id="content">Загрузка...</div>
        </div>
        <script>
            fetch('/check_auth')
                .then(response => response.json())
                .then(data => {
                    const contentDiv = document.getElementById('content');
                    if (data.authenticated) {
                        contentDiv.innerHTML = `
                            <div>
                                <img class="user-avatar" src="${data.user.picture}">
                                <h2>✅ Вы успешно авторизованы!</h2>
                                <p><strong>Имя:</strong> ${data.user.name}</p>
                                <p><strong>Email:</strong> ${data.user.email}</p>
                                <button class="logout-btn" onclick="logout()">Выйти</button>
                            </div>
                        `;
                    } else {
                        contentDiv.innerHTML = `
                            <div>
                                <h1>📱 Добро пожаловать!</h1>
                                <button class="login-btn" onclick="login()">🚀 Войти через Google</button>
                            </div>
                        `;
                    }
                });

            function login() { window.location.href = '/login'; }
            function logout() { window.location.href = '/logout'; }
        </script>
    </body>
    </html>
    '''


@app.route('/check_auth')
def check_auth():
    if 'user_info' in session:
        return jsonify({'authenticated': True, 'user': session['user_info']})
    return jsonify({'authenticated': False})


@app.route('/login')
def login():
    url = f'https://accounts.google.com/o/oauth2/v2/auth?client_id={GOOGLE_CLIENT_ID}&redirect_uri={REDIRECT_URI}&response_type=code&scope=email%20profile&access_type=online'
    return redirect(url)


@app.route('/callback')
def callback():
    code = request.args.get('code')
    if not code:
        return 'Ошибка: код не получен', 400

    token_data = {
        'code': code,
        'client_id': GOOGLE_CLIENT_ID,
        'client_secret': GOOGLE_CLIENT_SECRET,
        'redirect_uri': REDIRECT_URI,
        'grant_type': 'authorization_code'
    }
    response = requests.post('https://oauth2.googleapis.com/token', data=token_data)
    token_info = response.json()

    if 'access_token' not in token_info:
        return f'Ошибка: {token_info}', 400

    headers = {'Authorization': f'Bearer {token_info["access_token"]}'}
    user_response = requests.get('https://www.googleapis.com/oauth2/v2/userinfo', headers=headers)
    user_info = user_response.json()

    session['user_info'] = {
        'id': user_info['id'],
        'email': user_info['email'],
        'name': user_info.get('name', 'Без имени'),
        'picture': user_info.get('picture', '')
    }
    return redirect('/')


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')


if __name__ == '__main__':
    print('🚀 Сервер запущен: http://localhost:5000')
    app.run(host='localhost', port=5000, debug=True)