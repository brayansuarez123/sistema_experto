from typing import Dict, Tuple
from utils import get_respuesta, Response, Juego

lista_juegos = []
decisiones = []
mapa_juegos = {}
mapeo_descripciones = {}
mapeo_definiciones = {}

generos = "accion, aventura, mundo_abierto, infantil, disparos, mitologia, prota_femenina, historia, medievales, vista_panoramica, militares, construccion,pixel_art, comedia, lucha, primera_persona, mundo_post_apocaliptico, frenetico, gestion, sangrientos, interestelar, plataformas, asaltos, lineales, mazmorras"
generos = generos.split(", ")

generos_iniciales = ["accion", "aventura", "mundo_abierto", "lucha"]

pregunta_base = "¿ Te gusta el genero: {} ?"


def preprocess():
    global lista_juegos, decisiones, mapa_juegos, mapeo_descripciones, mapeo_definiciones
    juegos = open("juegos.txt")
    juegos_genero = juegos.read()
    lista_juegos = juegos_genero.split("\n")
    juegos.close()
    for juego in lista_juegos:
        archivo_juegos = open("decisiones/" + juego + ".txt")
        datos_juegos = archivo_juegos.read()
        lista_decisiones = datos_juegos.split("\n")
        decisiones.append(lista_decisiones)
        dict_decisiones = {k: v for (k, v) in zip(generos, lista_decisiones)}
        mapa_juegos[juego] = dict_decisiones
        archivo_juegos.close()
        archivo_juegos = open("descripciones de juegos/" +
                              juego + ".txt", "r", encoding='UTF-8')
        datos_juegos = archivo_juegos.read()
        mapeo_descripciones[juego] = datos_juegos
        archivo_juegos.close()
        archivo_juegos = open("generos/" + juego +
                              ".txt", "r", encoding='UTF-8')
        datos_juegos = archivo_juegos.read()
        mapeo_definiciones[juego] = datos_juegos
        archivo_juegos.close()


preprocess()


def identificar_juego(*arguments):
    lista_decisiones = []
    for juego in arguments:
        lista_decisiones.append(juego)
    # Handle key error
    return mapa_juegos[str(lista_decisiones)]


def get_detalles(juego):
    print('JUEGO GANADOR', juego)
    return mapeo_descripciones[juego]


def get_decisiones(juego):
    return mapeo_definiciones[juego]


def if_not_matched(juego):
    print("")
    id_juego = juego
    detalles_juego = get_detalles(id_juego)
    decisiones = get_decisiones(id_juego)
    print("")
    print("El titulo que mas se acomoda a tus gustos es: %s\n" % id_juego)
    print("una breve descripcion del mismo es :\n")
    print(detalles_juego+"\n")
    print("Los generos que contiene y su duracion aproximada es: \n")
    print(decisiones+"\n")


def get_datos_del_juego(juego: str) -> Juego:
    return {"titulo": juego, "descripcion": "Descipcion del juego", "generos": "lista de generos"}


class SistemaExperto():
    def __init__(self) -> None:
        print("INICIANDO SISTEMA EXPERTO")
        self.__juego_recomendado = None
        self.__generos = {}
        self.__pregunta = None

    def get_pregunta(self):
        return self.__pregunta

    def get_generos(self):
        return self.__generos

    def siguiente_pregunta(self) -> Dict:
        if not (self.__juego_recomendado == None):
            return get_respuesta(juego=self.__juego_recomendado)
        resp = self.__preguntar_root()

        # si hay error o se devolvio una pregunta
        if resp.get("err") == True or "pregunta" in resp:
            return resp

        return self.__preguntar()

    def __preguntar_root(self) -> Response:
        if not ha_tomado_alguna_rama(self):
            genero, err = tomar_genero_raiz(self)
            if err:
                return get_respuesta(err=True)
            return get_respuesta(genero=genero)
        return get_respuesta()

    def __preguntar(self):
        games = self.__obtener_juegos_por_generos(**self.get_generos())
        if len(games.keys()) > 1:
            firstK = next(iter(games))
            nuevo_genero = next(iter((games[firstK].keys() -
                                      self.get_generos().keys())))
            return get_respuesta(genero=nuevo_genero)
        juego_recomendado = list(games.keys())[0]
        self.__juego_recomendado = get_datos_del_juego(juego_recomendado)
        return get_respuesta(juego=self.__juego_recomendado)

    def set_generos(self, **formDict):
        self.__generos = {**self.__generos, **formDict}

    def get_juego_recomendado(self):
        return self.__juego_recomendado

    def __obtener_juegos_por_generos(self, **generos):
        return {key: values for (key, values) in mapa_juegos.items() if generos.items() <= values.items()}


def ha_tomado_alguna_rama(obj: SistemaExperto):
    generos_actuales = obj.get_generos()
    # Generos temporales para investigar si algun genero incial tiene el valor de "si"
    generos_temp: Dict = {}
    for genero in generos_iniciales:
        generos_temp[genero] = generos_actuales.get(genero, "no")
    for value in generos_temp.values():
        if value == "si":
            return True
    return False


def tomar_genero_raiz(obj: SistemaExperto) -> Tuple[str, bool]:
    """
        retorna la pregunta raiz (si hubo un error el segundo valor sera True)
    """
    generos_temp = obj.get_generos()
    for genero in generos_iniciales:
        if generos_temp.get(genero, False) == False:
            return (genero, False)
    return ("", True)


__all__ = ['SistemaExperto']


if __name__ == "__main__":
    engine = SistemaExperto()
    engine.set_generos(
        accion="si", aventura="si", mundo_abierto="si", infantil="no")
    print(engine.siguiente_pregunta())
    # engine.run()  # Run it!
