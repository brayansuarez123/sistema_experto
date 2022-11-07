import os
from typing import Dict
import mysql.connector

PATH = os.path.dirname(__file__)

JUEGOS_PATH = f"{PATH}/../juegos.txt"

GET_DESCRIPCIONES_PATH = lambda juego: f"{PATH}/../descripciones de juegos/{juego}.txt"

GET_GENEROS_PATH = lambda juego: f"{PATH}/../decisiones/{juego}.txt"

pregunta_base = "¿ Te gusta el genero: {genero} ?"


def count(n=0):
    x = 1
    while x <= n:
        yield x
        x += 1


def juegos() -> Dict:
    todos_los_juegos = []
    with open(JUEGOS_PATH) as juegos_f:
        todos_los_juegos = juegos_f.read().split("\n")
    juegos_resp = []
    for juego in todos_los_juegos:
        j_dict = {"title": juego}
        with open(GET_DESCRIPCIONES_PATH(juego)) as des_f:
            j_dict["description"] = des_f.read()
        # TODO: Agregar la carpeta image url en caso de querer colocar imagenes a los juegos
        j_dict["image_url"] = ""
        juegos_resp.append(j_dict)
    c = count(len(juegos_resp))
    return tuple(map(lambda j: {**j, "id": next(c)}, juegos_resp))


def generos(lista_de_juegos: tuple):
    todos_los_generos = set()
    for juego in lista_de_juegos:
        with open(GET_GENEROS_PATH(juego)) as juego_f:
            for row in juego_f.read().split("\n"):
                todos_los_generos.add(row.split("=")[0])
    c = count(len(todos_los_generos))
    return tuple(map(lambda g: {"name": g, "id": next(c)}, todos_los_generos))


def preguntas_generos(generos: tuple[Dict]):
    c = count(len(generos))
    return tuple(map(lambda g: {"question": pregunta_base.format(genero=g.get("name")), "genre_id": g.get('id'), "id": next(c)}, generos))


def juego_generos(juegos: tuple[dict], generos: tuple[dict]):
    lista_juego_generos = []
    for juego in juegos:
        with open(GET_GENEROS_PATH(juego.get("title"))) as juego_f:
            for row in juego_f.read().split("\n"):
                genero_value = row.split("=")
                gen_result = next(filter(lambda g: g.get(
                    "name") == genero_value[0], generos))
                lista_juego_generos.append({"value": genero_value[1], "id_game": juego.get(
                    "id"), "id_genre": gen_result.get("id")})
    c = count(len(lista_juego_generos))
    return tuple(map(lambda item: {**item, "id": next(c)}, lista_juego_generos))


# IMPORTANTE: cambiar de acuerdo a la configuración de la base de datos
db = mysql.connector.connect(
    host="localhost",
    user="expert",
    password="expert",
    database="movie_expert"
)

if __name__ == "__main__":
    _juegos = juegos()
    _generos = generos(tuple(map(lambda j: j.get("title"), _juegos)))
    _preguntas_genero = preguntas_generos(_generos)
    _juego_generos = juego_generos(_juegos, _generos)
    cursor = db.cursor()
    sql = "INSERT INTO genre (name, id) VALUES (%s, %s)"
    cursor.executemany(sql, tuple(map(lambda g: tuple(g.values()), _generos)))
    sql = "INSERT INTO genre_question (question, genre_id, id) VALUES (%s, %s, %s)"
    cursor.executemany(sql, tuple(
        map(lambda j: tuple(j.values()), _preguntas_genero)))
    sql = "INSERT INTO game (title, description, image_url, id) VALUES (%s, %s, %s, %s)"
    cursor.executemany(sql, tuple(map(lambda j: tuple(j.values()), _juegos)))
    sql = "INSERT INTO game_genre (value, id_game, id_genre, id) VALUES (%s, %s, %s, %s)"
    cursor.executemany(sql, tuple(
        map(lambda j: tuple(j.values()), _juego_generos)))
    db.commit()
    print(cursor.rowcount, " was inserted.")
