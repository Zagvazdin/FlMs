import os
from flask import Flask
from routes import main as routes

app = Flask(__name__)
app.secret_key = '3422'  # Необходимо для использования flash-сообщений и сессий

# Создаем директорию для сохранения файлов, если она не существует
os.makedirs('Сектора', exist_ok=True)

app.register_blueprint(routes)

if __name__ == '__main__':
    app.run(debug=True)
