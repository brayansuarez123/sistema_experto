from flask import Flask, render_template, request
from sistema_experto_juegos import Greetings
index = Flask(__name__)


@index.route("/")
def hello_world():
    return render_template("plantilla.html")


@index.route("/sistema", methods=["POST"])
def devolver():
    experto = Greetings()
    experto.reset()
    experto.colocar_categorias(request.form.to_dict(flat=True))
    experto.run()
    return render_template("resultado.html", juego_recomendado=experto.get_juego_recomendado())


def recibir(**fromdata):
    print(fromdata)
    return


if __name__ == "__main__":
    index.run()
