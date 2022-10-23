from flask import Flask, render_template, request, redirect, url_for
from sistema_experto_juegos import SistemaExperto
index = Flask(__name__)

users_history = {}

current_user = None


def auth_middle():
    if current_user == None:
        return render_template("bienvenido.html")


@index.route("/", methods=["GET"])
def hello_world():
    global current_user
    current_user = None
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
    nuevos_generos = {k: v for k, v in request.form.to_dict(
        flat=True).items() if k != "submit"}
    users_history[current_user] = {
        **users_history.get(current_user, {}), **nuevos_generos}
    print(users_history[current_user])
    experto = SistemaExperto(**users_history[current_user])
    respExp = experto.siguiente_pregunta()
    if respExp.get("err"):
        users_history[current_user] = {}
        return render_template("juego_no_encontrado.html")
    if "juego" in respExp:
        users_history[current_user] = {}
        return render_template("resultado.html", juego_recomendado=respExp.get("juego"))
    return render_template("pregunta.html", **respExp)


if __name__ == "__main__":
    index.run()
