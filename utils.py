from typing import TypedDict


class Juego(TypedDict):
    titulo: str
    descripcion: str
    generos: str


class Response(TypedDict):

    # El mensaje tiene algun tipo de error
    err: bool

    # La pregunta del sistema experto, solo se devuelve si el genero es suministrado
    pregunta: str

    # Genero del juego
    genero: str

    # Contenido del Juego
    juego: Juego


class InputsToResponse(TypedDict):

    # El mensaje tiene algun tipo de error
    err: bool

    # Genero del juego
    genero: str

    # Contenido del Juego
    juego: Juego


pregunta_base = "¿ Te gusta el genero: {} ?"


def get_respuesta(**kwargs: InputsToResponse) -> Response:
    if "genero" in kwargs:
        kwargs["pregunta"] = pregunta_base.format(kwargs.get("genero"))
    return {"err": False, **kwargs}


__all__ = ['Response', 'get_respuesta', 'InputsToResponse', 'Juego']
