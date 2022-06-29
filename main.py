# https://medium.com/nuances-of-programming/овладей-python-создавая-реальные-приложения-часть-4-60e016f18422
# https://pythonru.com/uroki/3-osnovy-flask
# https://www.linode.com/

from flask import Flask, render_template, request

from server.server import server
import socket


# Создание приложения.
app = Flask(__name__)


@app.route("/", methods=['post', 'get'])
def home():
    """ Главная страница. """

    return render_template("home.html")


@app.route("/server", methods=['post', 'get'])
def start_server():
    """ Страница для создания игровой сессии и старта сервера. """

    if request.method == "POST":
        total_amount = abs(int(request.form.get("total_amount")))
        boss_amount = abs(int(request.form.get("boss_amount")))
        port = int(request.form.get("boss_amount"))
        server(total_amount, boss_amount, port)

        hostname = socket.gethostname()
        dns_resolved_addr = socket.gethostbyname(hostname)
        message = f"Сервер создан!\nip={dns_resolved_addr};\nport={port};"
    else:
        message = "Ждём создание сервера."


    return render_template("server.html", message=message)


if __name__ == "__main__":
    app.run(debug=True)
