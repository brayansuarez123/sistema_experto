from typing import Dict, Tuple
from utils import get_respuesta, Response, Juego
from service import Service
from database import db

generos_iniciales = ["accion", "aventura", "lucha", "mundo_abierto"]

pregunta_base = "¿ Te gusta el genero: {} ?"

service = Service(db)


def get_datos_del_juego(juego: str) -> Juego:
    return service.consultar_juego_por_nombre(juego)


class SistemaExperto():
    # inicializar clase
    def __init__(self, **kwargs) -> None:
        print("INICIANDO SISTEMA EXPERTO")
        self.juegos_por_genero = service.consultar_generos_por_juego()
        self.__juego_recomendado = None
        self.__generos = kwargs
        self.__pregunta = None

    def get_pregunta(self):
        return self.__pregunta

    def get_generos(self):
        return self.__generos

    def siguiente_pregunta(self) -> Response:
        """
            El metodo siguiente_pregunta cuando es ejecutado
            devuelve un objeto Response el cual de manera dinamica
            puede trar los datos de la siguiente pregunta, informar que
            el sistema experto no encontro el juego buscado y traer la 
            información del juego encontrado.
        """
        # Si ya hay un juego registrado como encontrado entonces simplemente lo devuelve
        if not (self.__juego_recomendado == None):
            return get_respuesta(juego=self.__juego_recomendado)
        # Hace las cuatro primeras preguntas (una a la vez, el sistema va registrando cuales se han respondido)
        resp = self.__preguntar_root()

        # si hay error o se devolvio una pregunta
        if resp.get("err") == True or "pregunta" in resp:
            return resp

        # devuelve la siguiente pregunta o un juego en caso de encontrar
        return self.__preguntar()

    def __preguntar_root(self) -> Response:
        """
            Este metodo se limita hacer una de la cuatro preguntas
            base que se consideraron (accion, aventura, lucha, mundo_abierto)
        """
        if not ha_tomado_alguna_rama(self):
            genero, err = tomar_genero_raiz(self)
            if err:
                return get_respuesta(err=True)
            return get_respuesta(genero=genero)
        return get_respuesta()

    def __preguntar(self):
        """
            Este metodo contiene el nucleo logico del sistema experto
            para hallar un juego basado en sus generos.
        """
        games = self.__obtener_juegos_por_generos(**self.get_generos())
        if len(games.keys()) > 1:
            # El histograma es necesario para saber de todas las preguntas que se puden hacer
            # cual se deberia hacer primero
            histogram = {}
            for game in games.values():
                for gener in game.keys():
                    histogram[gener] = histogram.get(gener, 0) + 1
            histogram = {k: v for k,
                         v in histogram.items() if not (k in self.get_generos())}
            # Revisa la pregunta con mas puntuacion como candidata a ser preguntada
            nuevo_genero = max(histogram, key=histogram.get)
            return get_respuesta(genero=nuevo_genero)
        # No se encontro ningun juego
        if len(games.keys()) == 0:
            return get_respuesta(err=True)
        # Se encontro un juego que cumple los requisitos
        juego_recomendado = list(games.keys())[0]
        self.__juego_recomendado = get_datos_del_juego(juego_recomendado)
        return get_respuesta(juego=self.__juego_recomendado)

    def set_generos(self, **formDict):
        self.__generos = {**self.__generos, **formDict}

    def get_juego_recomendado(self):
        return self.__juego_recomendado

    def __obtener_juegos_por_generos(self, **generos):
        return {key: values for (key, values) in self.juegos_por_genero.items() if generos.items() <= values.items()}


def ha_tomado_alguna_rama(obj: SistemaExperto):
    generos_actuales = obj.get_generos()
    # Generos temporales para investigar si algun genero incial tiene el valor de "si"
    generos_temp: dict = {}
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


# SOLO PARA HACER PRUEBAS DEL SISTEMA EXPERTO
if __name__ == "__main__":
    engine = SistemaExperto(accion="no", aventura="si",
                            mitologia="no", gestion="si")
    engine.set_generos()
    print(engine.siguiente_pregunta())
    # engine.run()  # Run it!
