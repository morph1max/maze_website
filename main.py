# https://medium.com/nuances-of-programming/овладей-python-создавая-реальные-приложения-часть-4-60e016f18422
# https://pythonru.com/uroki/3-osnovy-flask

from flask import Flask, render_template


# Создание приложения.
app = Flask(__name__)


@app.route("/")
def home():
    """ Главная страница. """

    return render_template("home.html")


@app.route("/start_server")
def start_server():
    """ Страница для создания игровой сессии и старта сервера. """

    return render_template("start_server.html")


if __name__ == "__main__":
    app.run(debug=True)
