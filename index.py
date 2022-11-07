from flask import Flask, render_template, request, redirect, url_for
from sistema_experto_juegos import SistemaExperto
index = Flask(__name__)

users_history = {}

current_user = None

answers = {}


def saveAnswers(**resp_data):
    resp_data.pop("submit")
    answers[current_user] = answers.get(current_user, list())
    answers[current_user].extend(resp_data.keys())


def obtener_generos_ordenados():
    return answers[current_user]


def clean_answers():
    if current_user == None:
        return
    answers[current_user] = []


def auth_middle():
    if current_user == None:
        return render_template("bienvenido.html")


@index.route("/", methods=["GET"])
def hello_world():
    global current_user
    current_user = None
    clean_answers()
    return render_template("bienvenido.html")


@index.route("/", methods=["POST"])
def redirectToExpert():
    global current_user
    user_info = request.form.to_dict(flat=True)
    if not "username" in user_info:
        return render_template("bienvenido.html", info="El campo de nombre de usuario es obligatorio")
    current_user = user_info.get("username")
    return redirect(url_for("preguntas"))


@index.route("/preguntas", methods=["GET"])
def start_preguntas():
    global users_history, current_user
    if auth_middle():
        return auth_middle()
    experto = SistemaExperto()
    respExp = experto.siguiente_pregunta()
    return render_template("pregunta.html", **respExp)


@index.route("/preguntas", methods=["POST"])
def preguntas():
    global users_history, current_user
    if auth_middle():
        return auth_middle()
    nuevos_generos = request.form.to_dict(flat=True)
    nuevos_generos.pop("submit")
    saveAnswers(**request.form.to_dict(flat=True))
    users_history[current_user] = {
        **users_history.get(current_user, {}), **nuevos_generos}
    experto = SistemaExperto(*obtener_generos_ordenados(),
                             **users_history[current_user])
    respExp = experto.siguiente_pregunta()
    if respExp.get("err"):
        clean_answers()
        users_history[current_user] = {}
        return render_template("juego_no_encontrado.html")
    if "juego" in respExp:
        clean_answers()
        users_history[current_user] = {}
        sugerencias = experto.recomendar_juegos(respExp["juego"])
        return render_template("resultado.html", juego_recomendado=respExp["juego"], sugerencias=sugerencias)
    return render_template("pregunta.html", **respExp)


if __name__ == "__main__":
    index.run()
