# https://medium.com/nuances-of-programming/овладей-python-создавая-реальные-приложения-часть-4-60e016f18422
# https://pythonru.com/uroki/3-osnovy-flask

from flask import Flask, render_template, request

import socket


# Создание приложения.
app = Flask(__name__)


@app.route("/", methods=['post', 'get'])
def home():
    """ Главная страница. """

    return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True)
