from typing import Dict, Tuple
from experta import Fact, DefFacts, KnowledgeEngine, Rule, MATCH, NOT, AND, W, OR

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


def obtener_juegos_por_generos(**generos):
    return {key: values for (key,
                             values) in mapa_juegos.items() if generos.items() <= values.items()}

# @my_decorator is just a way of saying just_some_function = my_decorator(just_some_function)
# def identify_juego(accion, aventura, mundo_abierto, infantil, disparos, mitologia, prota_femenina, historia,medievales ,vista_panoramica,militares):


class Greetings(KnowledgeEngine):
    @DefFacts()
    def _initial_action(self):
        print("")
        print("Hola bienvenido a sugerencias gamers!.")
        self.__juego_recomendado = None
        self.__generos = {}
        self.__pregunta = None
        yield Fact(action="encontrar_juego")

    def get_pregunta(self):
        return self.__pregunta

    def get_generos(self):
        return self.__generos

    def siguiente_pregunta(self) -> Tuple[str, bool]:
        if not ha_tomado_alguna_rama(self):
            return tomar_genero_raiz(self)
        self.facts

    @Rule(AND(Fact(action='encontrar_juego'), NOT(Fact(juego=W()))), salience=10)
    def preguntar_root(self):
        if not ha_tomado_alguna_rama(self):
            genero, err = tomar_genero_raiz(self)
            self.__pregunta = {"pregunta": pregunta_base.format(
                genero), "genero": genero}
            if err:
                self.__pregunta = {
                    "pregunta": "No se ha encontrado un juego que se ajuste a sus criterios", "genero": "NOT_FOUND"}
            return

    def preguntar(self):
        if not (self.__juego_recomendado == None):
            return
        return obtener_juegos_por_generos(**self.__generos)

    def colocar_categorias(self, **formDict):
        self.__generos = {**self.__generos, **formDict}
        self.declare(Fact(**formDict))

    @Rule(Fact(action='encontrar_juego'), Fact(accion="si"), Fact(aventura="si"), Fact(mundo_abierto="no"), Fact(infantil="no"), Fact(disparos="si"), Fact(mitologia="no"), Fact(prota_femenina="si"), Fact(historia="no"), Fact(medievales="no"), Fact(vista_panoramica="no"), Fact(militares="no"), Fact(construccion="no"), Fact(pixel_art="no"), Fact(comedia="no"), Fact(lucha="no"), Fact(primera_persona="no"), Fact(mundo_post_apocaliptico="no"), Fact(frenetico="no"), Fact(gestion="no"), Fact(sangrientos="no"), Fact(interestelar="no"), Fact(plataformas="no"), Fact(asaltos="no"), Fact(lineales="no"), Fact(mazmorras="no"))
    def juego_0(self):
        self.declare(Fact(juego="Metroid"))

    @Rule(Fact(action='encontrar_juego'), Fact(accion="si"), Fact(aventura="no"), Fact(mundo_abierto="no"), Fact(infantil="no"), Fact(disparos="si"), Fact(mitologia="no"), Fact(prota_femenina="no"), Fact(historia="no"), Fact(medievales="no"), Fact(vista_panoramica="no"), Fact(militares="si"), Fact(construccion="no"), Fact(pixel_art="no"), Fact(comedia="no"), Fact(lucha="no"), Fact(primera_persona="no"), Fact(mundo_post_apocaliptico="no"), Fact(frenetico="no"), Fact(gestion="no"), Fact(sangrientos="no"), Fact(interestelar="no"), Fact(plataformas="no"), Fact(asaltos="no"), Fact(lineales="no"), Fact(mazmorras="no"))
    def juego_1(self):
        self.declare(Fact(juego="Cod"))

    @Rule(Fact(action='encontrar_juego'), Fact(accion="si"), Fact(aventura="no"), Fact(mundo_abierto="si"), Fact(infantil="no"), Fact(disparos="no"), Fact(mitologia="no"), Fact(prota_femenina="no"), Fact(historia="no"), Fact(medievales="si"), Fact(vista_panoramica="no"), Fact(militares="no"), Fact(construccion="no"), Fact(pixel_art="no"), Fact(comedia="no"), Fact(lucha="no"), Fact(primera_persona="no"), Fact(mundo_post_apocaliptico="no"), Fact(frenetico="no"), Fact(gestion="no"), Fact(sangrientos="no"), Fact(interestelar="no"), Fact(plataformas="no"), Fact(asaltos="no"), Fact(lineales="no"), Fact(mazmorras="no"))
    def juego_2(self):
        self.declare(Fact(juego="Skyrim"))

    @Rule(Fact(action='encontrar_juego'), Fact(accion="si"), Fact(aventura="no"), Fact(mundo_abierto="no"), Fact(infantil="no"), Fact(disparos="si"), Fact(mitologia="no"), Fact(prota_femenina="no"), Fact(historia="si"), Fact(medievales="no"), Fact(vista_panoramica="no"), Fact(militares="no"), Fact(construccion="no"), Fact(pixel_art="no"), Fact(comedia="no"), Fact(lucha="no"), Fact(primera_persona="no"), Fact(mundo_post_apocaliptico="no"), Fact(frenetico="no"), Fact(gestion="no"), Fact(sangrientos="no"), Fact(interestelar="no"), Fact(plataformas="no"), Fact(asaltos="no"), Fact(lineales="no"), Fact(mazmorras="no"))
    def juego_3(self):
        self.declare(Fact(juego="Gears of war"))

    @Rule(Fact(action='encontrar_juego'), Fact(accion="no"), Fact(aventura="si"), Fact(mundo_abierto="si"), Fact(infantil="no"), Fact(disparos="no"), Fact(mitologia="si"), Fact(prota_femenina="no"), Fact(historia="no"), Fact(medievales="no"), Fact(vista_panoramica="no"), Fact(militares="no"), Fact(construccion="no"), Fact(pixel_art="no"), Fact(comedia="no"), Fact(lucha="no"), Fact(primera_persona="no"), Fact(mundo_post_apocaliptico="no"), Fact(frenetico="no"), Fact(gestion="no"), Fact(sangrientos="no"), Fact(interestelar="no"), Fact(plataformas="no"), Fact(asaltos="no"), Fact(lineales="no"), Fact(mazmorras="no"))
    def juego_4(self):
        self.declare(Fact(juego="God of war"))

    @Rule(Fact(action='encontrar_juego'), Fact(accion="si"), Fact(aventura="si"), Fact(mundo_abierto="si"), Fact(infantil="si"), Fact(disparos="no"), Fact(mitologia="no"), Fact(prota_femenina="no"), Fact(historia="no"), Fact(medievales="no"), Fact(vista_panoramica="no"), Fact(militares="no"), Fact(construccion="no"), Fact(pixel_art="no"), Fact(comedia="no"), Fact(lucha="no"), Fact(primera_persona="no"), Fact(mundo_post_apocaliptico="no"), Fact(frenetico="no"), Fact(gestion="no"), Fact(sangrientos="no"), Fact(interestelar="no"), Fact(plataformas="no"), Fact(asaltos="no"), Fact(lineales="no"), Fact(mazmorras="no"))
    def juego_5(self):
        self.declare(Fact(juego="Kirby"))

    @Rule(Fact(action='encontrar_juego'), Fact(accion="no"), Fact(aventura="si"), Fact(mundo_abierto="si"), Fact(infantil="no"), Fact(disparos="no"), Fact(mitologia="no"), Fact(prota_femenina="no"), Fact(historia="no"), Fact(medievales="no"), Fact(vista_panoramica="si"), Fact(militares="no"), Fact(construccion="no"), Fact(pixel_art="no"), Fact(comedia="no"), Fact(lucha="no"), Fact(primera_persona="no"), Fact(mundo_post_apocaliptico="no"), Fact(frenetico="no"), Fact(gestion="no"), Fact(sangrientos="no"), Fact(interestelar="no"), Fact(plataformas="no"), Fact(asaltos="no"), Fact(lineales="no"), Fact(mazmorras="no"))
    def juego_6(self):
        self.declare(Fact(juego="Cult of the lamb"))

    @Rule(Fact(action='encontrar_juego'), Fact(accion="no"), Fact(aventura="no"), Fact(mundo_abierto="si"), Fact(infantil="no"), Fact(disparos="no"), Fact(mitologia="no"), Fact(prota_femenina="no"), Fact(historia="no"), Fact(medievales="no"), Fact(vista_panoramica="no"), Fact(militares="no"), Fact(construccion="si"), Fact(pixel_art="si"), Fact(comedia="no"), Fact(lucha="no"), Fact(primera_persona="no"), Fact(mundo_post_apocaliptico="no"), Fact(frenetico="no"), Fact(gestion="no"), Fact(sangrientos="no"), Fact(interestelar="no"), Fact(plataformas="no"), Fact(asaltos="no"), Fact(lineales="no"), Fact(mazmorras="no"))
    def juego_7(self):
        self.declare(Fact(juego="Terraria"))

    @Rule(Fact(action='encontrar_juego'), Fact(accion="si"), Fact(aventura="no"), Fact(mundo_abierto="no"), Fact(infantil="no"), Fact(disparos="si"), Fact(mitologia="no"), Fact(prota_femenina="no"), Fact(historia="no"), Fact(medievales="no"), Fact(vista_panoramica="no"), Fact(militares="no"), Fact(construccion="no"), Fact(pixel_art="no"), Fact(comedia="si"), Fact(lucha="no"), Fact(primera_persona="no"), Fact(mundo_post_apocaliptico="no"), Fact(frenetico="no"), Fact(gestion="no"), Fact(sangrientos="no"), Fact(interestelar="no"), Fact(plataformas="no"), Fact(asaltos="no"), Fact(lineales="no"), Fact(mazmorras="no"))
    def juego_8(self):
        self.declare(Fact(juego="Borderlands"))

    @Rule(Fact(action='encontrar_juego'), Fact(accion="si"), Fact(aventura="si"), Fact(mundo_abierto="no"), Fact(infantil="no"), Fact(disparos="no"), Fact(mitologia="no"), Fact(prota_femenina="no"), Fact(historia="no"), Fact(medievales="no"), Fact(vista_panoramica="no"), Fact(militares="no"), Fact(construccion="no"), Fact(pixel_art="no"), Fact(comedia="no"), Fact(lucha="si"), Fact(primera_persona="no"), Fact(mundo_post_apocaliptico="no"), Fact(frenetico="no"), Fact(gestion="no"), Fact(sangrientos="no"), Fact(interestelar="no"), Fact(plataformas="no"), Fact(asaltos="no"), Fact(lineales="no"), Fact(mazmorras="no"))
    def juego_9(self):
        self.declare(Fact(juego="Super smash bros"))

    @Rule(Fact(action='encontrar_juego'), Fact(accion="si"), Fact(aventura="no"), Fact(mundo_abierto="no"), Fact(infantil="no"), Fact(disparos="si"), Fact(mitologia="no"), Fact(prota_femenina="no"), Fact(historia="no"), Fact(medievales="no"), Fact(vista_panoramica="no"), Fact(militares="no"), Fact(construccion="no"), Fact(pixel_art="no"), Fact(comedia="no"), Fact(lucha="no"), Fact(primera_persona="si"), Fact(mundo_post_apocaliptico="no"), Fact(frenetico="no"), Fact(gestion="no"), Fact(sangrientos="no"), Fact(interestelar="no"), Fact(plataformas="no"), Fact(asaltos="no"), Fact(lineales="no"), Fact(mazmorras="no"))
    def juego_10(self):
        self.declare(Fact(juego="Kill zone"))

    @Rule(Fact(action='encontrar_juego'), Fact(accion="si"), Fact(aventura="si"), Fact(mundo_abierto="si"), Fact(infantil="no"), Fact(disparos="no"), Fact(mitologia="no"), Fact(prota_femenina="no"), Fact(historia="no"), Fact(medievales="no"), Fact(vista_panoramica="no"), Fact(militares="no"), Fact(construccion="no"), Fact(pixel_art="no"), Fact(comedia="no"), Fact(lucha="no"), Fact(primera_persona="no"), Fact(mundo_post_apocaliptico="si"), Fact(frenetico="no"), Fact(gestion="no"), Fact(sangrientos="no"), Fact(interestelar="no"), Fact(plataformas="no"), Fact(asaltos="no"), Fact(lineales="no"), Fact(mazmorras="no"))
    def juego_11(self):
        self.declare(Fact(juego="Fallout"))

    @Rule(Fact(action='encontrar_juego'), Fact(accion="si"), Fact(aventura="no"), Fact(mundo_abierto="no"), Fact(infantil="no"), Fact(disparos="si"), Fact(mitologia="no"), Fact(prota_femenina="no"), Fact(historia="no"), Fact(medievales="no"), Fact(vista_panoramica="no"), Fact(militares="no"), Fact(construccion="no"), Fact(pixel_art="no"), Fact(comedia="no"), Fact(lucha="no"), Fact(primera_persona="no"), Fact(mundo_post_apocaliptico="no"), Fact(frenetico="si"), Fact(gestion="no"), Fact(sangrientos="no"), Fact(interestelar="no"), Fact(plataformas="no"), Fact(asaltos="no"), Fact(lineales="no"), Fact(mazmorras="no"))
    def juego_12(self):
        self.declare(Fact(juego="Doom eternal"))

    @Rule(Fact(action='encontrar_juego'), Fact(accion="no"), Fact(aventura="si"), Fact(mundo_abierto="si"), Fact(infantil="no"), Fact(disparos="no"), Fact(mitologia="no"), Fact(prota_femenina="no"), Fact(historia="no"), Fact(medievales="no"), Fact(vista_panoramica="no"), Fact(militares="no"), Fact(construccion="no"), Fact(pixel_art="no"), Fact(comedia="no"), Fact(lucha="no"), Fact(primera_persona="no"), Fact(mundo_post_apocaliptico="no"), Fact(frenetico="no"), Fact(gestion="si"), Fact(sangrientos="no"), Fact(interestelar="no"), Fact(plataformas="no"), Fact(asaltos="no"), Fact(lineales="no"), Fact(mazmorras="no"))
    def juego_13(self):
        self.declare(Fact(juego="Animal crossing"))

    @Rule(Fact(action='encontrar_juego'), Fact(accion="no"), Fact(aventura="si"), Fact(mundo_abierto="si"), Fact(infantil="no"), Fact(disparos="no"), Fact(mitologia="no"), Fact(prota_femenina="no"), Fact(historia="no"), Fact(medievales="no"), Fact(vista_panoramica="no"), Fact(militares="no"), Fact(construccion="no"), Fact(pixel_art="si"), Fact(comedia="no"), Fact(lucha="no"), Fact(primera_persona="no"), Fact(mundo_post_apocaliptico="no"), Fact(frenetico="no"), Fact(gestion="si"), Fact(sangrientos="no"), Fact(interestelar="no"), Fact(plataformas="no"), Fact(asaltos="no"), Fact(lineales="no"), Fact(mazmorras="no"))
    def juego_14(self):
        self.declare(Fact(juego="Stardew valley"))

    @Rule(Fact(action='encontrar_juego'), Fact(accion="si"), Fact(aventura="no"), Fact(mundo_abierto="no"), Fact(infantil="no"), Fact(disparos="no"), Fact(mitologia="no"), Fact(prota_femenina="no"), Fact(historia="no"), Fact(medievales="no"), Fact(vista_panoramica="no"), Fact(militares="no"), Fact(construccion="no"), Fact(pixel_art="no"), Fact(comedia="no"), Fact(lucha="si"), Fact(primera_persona="no"), Fact(mundo_post_apocaliptico="no"), Fact(frenetico="no"), Fact(gestion="no"), Fact(sangrientos="si"), Fact(interestelar="no"), Fact(plataformas="no"), Fact(asaltos="no"), Fact(lineales="no"), Fact(mazmorras="no"))
    def juego_15(self):
        self.declare(Fact(juego="Mortal kombat"))

    @Rule(Fact(action='encontrar_juego'), Fact(accion="si"), Fact(aventura="si"), Fact(mundo_abierto="si"), Fact(infantil="no"), Fact(disparos="no"), Fact(mitologia="no"), Fact(prota_femenina="no"), Fact(historia="no"), Fact(medievales="no"), Fact(vista_panoramica="no"), Fact(militares="no"), Fact(construccion="no"), Fact(pixel_art="no"), Fact(comedia="no"), Fact(lucha="no"), Fact(primera_persona="no"), Fact(mundo_post_apocaliptico="no"), Fact(frenetico="no"), Fact(gestion="no"), Fact(sangrientos="no"), Fact(interestelar="no"), Fact(plataformas="no"), Fact(asaltos="no"), Fact(lineales="no"), Fact(mazmorras="no"))
    def juego_16(self):
        self.declare(Fact(juego="Zelda"))

    @Rule(Fact(action='encontrar_juego'), Fact(accion="si"), Fact(aventura="no"), Fact(mundo_abierto="si"), Fact(infantil="no"), Fact(disparos="no"), Fact(mitologia="no"), Fact(prota_femenina="no"), Fact(historia="no"), Fact(medievales="no"), Fact(vista_panoramica="no"), Fact(militares="no"), Fact(construccion="si"), Fact(pixel_art="no"), Fact(comedia="no"), Fact(lucha="no"), Fact(primera_persona="no"), Fact(mundo_post_apocaliptico="no"), Fact(frenetico="no"), Fact(gestion="no"), Fact(sangrientos="no"), Fact(interestelar="no"), Fact(plataformas="no"), Fact(asaltos="no"), Fact(lineales="no"), Fact(mazmorras="no"))
    def juego_17(self):
        self.declare(Fact(juego="Minecraft"))

    @Rule(Fact(action='encontrar_juego'), Fact(accion="no"), Fact(aventura="no"), Fact(mundo_abierto="si"), Fact(infantil="no"), Fact(disparos="si"), Fact(mitologia="no"), Fact(prota_femenina="no"), Fact(historia="no"), Fact(medievales="no"), Fact(vista_panoramica="no"), Fact(militares="no"), Fact(construccion="no"), Fact(pixel_art="no"), Fact(comedia="no"), Fact(lucha="no"), Fact(primera_persona="no"), Fact(mundo_post_apocaliptico="no"), Fact(frenetico="no"), Fact(gestion="no"), Fact(sangrientos="no"), Fact(interestelar="si"), Fact(plataformas="no"), Fact(asaltos="no"), Fact(lineales="no"), Fact(mazmorras="no"))
    def juego_18(self):
        self.declare(Fact(juego="Destiny"))

    @Rule(Fact(action='encontrar_juego'), Fact(accion="si"), Fact(aventura="si"), Fact(mundo_abierto="no"), Fact(infantil="no"), Fact(disparos="no"), Fact(mitologia="no"), Fact(prota_femenina="no"), Fact(historia="no"), Fact(medievales="no"), Fact(vista_panoramica="no"), Fact(militares="no"), Fact(construccion="no"), Fact(pixel_art="no"), Fact(comedia="no"), Fact(lucha="no"), Fact(primera_persona="no"), Fact(mundo_post_apocaliptico="no"), Fact(frenetico="no"), Fact(gestion="no"), Fact(sangrientos="no"), Fact(interestelar="no"), Fact(plataformas="si"), Fact(asaltos="no"), Fact(lineales="no"), Fact(mazmorras="no"))
    def juego_19(self):
        self.declare(Fact(juego="Mario"))

    @Rule(Fact(action='encontrar_juego'), Fact(accion="si"), Fact(aventura="no"), Fact(mundo_abierto="no"), Fact(infantil="no"), Fact(disparos="no"), Fact(mitologia="no"), Fact(prota_femenina="no"), Fact(historia="no"), Fact(medievales="no"), Fact(vista_panoramica="si"), Fact(militares="no"), Fact(construccion="no"), Fact(pixel_art="no"), Fact(comedia="no"), Fact(lucha="si"), Fact(primera_persona="no"), Fact(mundo_post_apocaliptico="no"), Fact(frenetico="no"), Fact(gestion="no"), Fact(sangrientos="no"), Fact(interestelar="no"), Fact(plataformas="no"), Fact(asaltos="no"), Fact(lineales="no"), Fact(mazmorras="no"))
    def juego_20(self):
        self.declare(Fact(juego="League of legends"))

    @Rule(Fact(action='encontrar_juego'), Fact(accion="si"), Fact(aventura="no"), Fact(mundo_abierto="no"), Fact(infantil="no"), Fact(disparos="si"), Fact(mitologia="no"), Fact(prota_femenina="no"), Fact(historia="no"), Fact(medievales="no"), Fact(vista_panoramica="no"), Fact(militares="no"), Fact(construccion="no"), Fact(pixel_art="no"), Fact(comedia="no"), Fact(lucha="no"), Fact(primera_persona="no"), Fact(mundo_post_apocaliptico="no"), Fact(frenetico="no"), Fact(gestion="no"), Fact(sangrientos="no"), Fact(interestelar="no"), Fact(plataformas="no"), Fact(asaltos="si"), Fact(lineales="no"), Fact(mazmorras="no"))
    def juego_21(self):
        self.declare(Fact(juego="GTA"))

    @Rule(Fact(action='encontrar_juego'), Fact(accion="no"), Fact(aventura="si"), Fact(mundo_abierto="no"), Fact(infantil="no"), Fact(disparos="no"), Fact(mitologia="no"), Fact(prota_femenina="no"), Fact(historia="no"), Fact(medievales="no"), Fact(vista_panoramica="no"), Fact(militares="no"), Fact(construccion="no"), Fact(pixel_art="no"), Fact(comedia="no"), Fact(lucha="no"), Fact(primera_persona="no"), Fact(mundo_post_apocaliptico="no"), Fact(frenetico="no"), Fact(gestion="no"), Fact(sangrientos="no"), Fact(interestelar="no"), Fact(plataformas="no"), Fact(asaltos="no"), Fact(lineales="si"), Fact(mazmorras="no"))
    def juego_22(self):
        self.declare(Fact(juego="Subway surfers"))

    @Rule(Fact(action='encontrar_juego'), Fact(accion="si"), Fact(aventura="no"), Fact(mundo_abierto="no"), Fact(infantil="no"), Fact(disparos="si"), Fact(mitologia="no"), Fact(prota_femenina="no"), Fact(historia="no"), Fact(medievales="no"), Fact(vista_panoramica="no"), Fact(militares="no"), Fact(construccion="no"), Fact(pixel_art="no"), Fact(comedia="no"), Fact(lucha="no"), Fact(primera_persona="no"), Fact(mundo_post_apocaliptico="no"), Fact(frenetico="no"), Fact(gestion="no"), Fact(sangrientos="no"), Fact(interestelar="no"), Fact(plataformas="no"), Fact(asaltos="no"), Fact(lineales="no"), Fact(mazmorras="si"))
    def juego_23(self):
        self.declare(Fact(juego="The binding of isaac"))

    @Rule(Fact(action='encontrar_juego'), Fact(accion="si"), Fact(aventura="si"), Fact(mundo_abierto="no"), Fact(infantil="no"), Fact(disparos="no"), Fact(mitologia="no"), Fact(prota_femenina="no"), Fact(historia="no"), Fact(medievales="no"), Fact(vista_panoramica="no"), Fact(militares="no"), Fact(construccion="no"), Fact(pixel_art="no"), Fact(comedia="si"), Fact(lucha="no"), Fact(primera_persona="no"), Fact(mundo_post_apocaliptico="no"), Fact(frenetico="no"), Fact(gestion="no"), Fact(sangrientos="no"), Fact(interestelar="no"), Fact(plataformas="no"), Fact(asaltos="no"), Fact(lineales="no"), Fact(mazmorras="no"))
    def juego_24(self):
        self.declare(Fact(juego="Castle crashers"))

    @Rule(Fact(action='encontrar_juego'), Fact(juego=MATCH.juego), salience=-998)
    def juego(self, juego):
        print("")
        id_juego = juego
        juego_details = get_detalles(id_juego)
        treatments = get_decisiones(id_juego)
        print("")
        print("El juego que mas se acomoda a sus gustos seria %s\n" % (id_juego))
        print("Una breve descripcion del mismo: \n")
        print(juego_details+"\n")
        print("su duracion aproximada y los generos a los que pertenece: \n")
        print(treatments+"\n")
        self.__juego_recomendado = {
            "name": juego, "detalle": juego_details, "generos": treatments}

    @Rule(Fact(action='encontrar_juego'),
          Fact(accion=MATCH.accion),
          Fact(aventura=MATCH.aventura),
          Fact(mundo_abierto=MATCH.mundo_abierto),
          Fact(infantil=MATCH.infantil),
          Fact(disparos=MATCH.disparos),
          Fact(mitologia=MATCH.mitologia),
          Fact(prota_femenina=MATCH.prota_femenina),
          Fact(medievales=MATCH.medievales),
          Fact(historia=MATCH.historia),
          Fact(vista_panoramica=MATCH.vista_panoramica),
          Fact(militares=MATCH.militares),
          Fact(construccion=MATCH.construccion),
          Fact(comedia=MATCH.comedia),
          Fact(lucha=MATCH.lucha),
          Fact(primera_persona=MATCH.primera_persona),
          Fact(mundo_post_apocaliptico=MATCH.mundo_post_apocaliptico),
          Fact(frenetico=MATCH.frenetico),
          Fact(gestion=MATCH.gestion),
          Fact(sangrientos=MATCH.sangrientos),
          Fact(interestelar=MATCH.interestelar),
          Fact(plataformas=MATCH.plataformas),
          Fact(asaltos=MATCH.asaltos),
          Fact(lineales=MATCH.lineales),
          Fact(mazmorras=MATCH.mazmorras),
          Fact(pixel_art=MATCH.pixel_art), NOT(Fact(juego=MATCH.juego)), salience=-999)
    def not_matched(self, accion, aventura, mundo_abierto, infantil, disparos, mitologia, prota_femenina, historia, medievales, vista_panoramica, militares, construccion, pixel_art, comedia, lucha, primera_persona, mundo_post_apocaliptico, frenetico, gestion, sangrientos, interestelar, plataformas, asaltos, lineales, mazmorras):
        print("\nno se encontro un juego que cumpla con todos los generos, pero este seria un aproximado a sus gustos.")
        lis = [accion, aventura, mundo_abierto, infantil, disparos, mitologia, prota_femenina, historia, medievales, vista_panoramica, militares, construccion,
               pixel_art, comedia, lucha, primera_persona, mundo_post_apocaliptico, frenetico, gestion, sangrientos, interestelar, plataformas, asaltos, lineales, mazmorras]
        print('LISTA DE JUEGOS', lis)
        max_count = 0
        max_juego = ""
        for key, val in mapa_juegos.items():
            count = 0
            temp_list = eval(key)
            for j in range(0, len(lis)):
                if (temp_list[j] == lis[j] and lis[j] == "si"):
                    count = count + 1
            if count > max_count:
                max_count = count
                max_juego = val

        self.__juego_recomendado = {"name": max_juego, "detalle": get_detalles(
            max_juego), "generos": get_decisiones(max_juego)}
        if_not_matched(max_juego)

    def get_juego_recomendado(self):
        return self.__juego_recomendado


def ha_tomado_alguna_rama(obj: Greetings):
    generos_actuales = obj.get_generos()
    # Generos temporales para investigar si algun genero incial tiene el valor de "si"
    generos_temp: Dict = {}
    for genero in generos_iniciales:
        generos_temp[genero] = generos_actuales.get(genero, "no")
    for value in generos_temp.values():
        if value == "si":
            return True
    return False


def tomar_genero_raiz(obj: Greetings) -> Tuple[str, bool]:
    """
        retorna la pregunta raiz y si hubo algun error (si hubo un error el segundo valor sera True)
    """
    generos_temp = obj.get_generos()
    for genero in generos_iniciales:
        if generos_temp.get(genero, False) == False:
            return (genero, False)
    return ("", True)


__all__ = ['Greetings']


if __name__ == "__main__":
    engine = Greetings()
    engine.reset()  # Prepare the engine for the execution.
    engine.colocar_categorias(
        accion="si", aventura="si", mundo_abierto="si", infantil="no")
    print(engine.preguntar())
    # engine.run()  # Run it!
    if engine.get_pregunta():
        print(engine.get_pregunta())
