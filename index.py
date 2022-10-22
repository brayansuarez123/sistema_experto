from typing import Dict
from flask import Flask, render_template, request
from sistema_experto_juegos import SistemaExperto
index = Flask(__name__)

user_resp: Dict[str, str] = {

}


@index.route("/")
def hello_world():
    return render_template("plantilla.html")


@index.route("/sistema", methods=["POST"])
def devolver():
    experto = SistemaExperto()
    experto.reset()
    experto.set_generos(request.form.to_dict(flat=True))
    experto.run()
    return render_template("resultado.html", juego_recomendado=experto.get_juego_recomendado())


def preguntas():
    return render_template("pregunta.html", pregunta={"title": "mi pregunta"})


if __name__ == "__main__":
    index.run()
