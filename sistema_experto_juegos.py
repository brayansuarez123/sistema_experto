from experta import *

lista_juegos = []
decisiones = []
mapa_juegos = {}
mapeo_descripciones = {}
mapeo_definiciones = {}

def preprocess():
	global lista_juegos,decisiones,mapa_juegos,mapeo_descripciones,mapeo_definiciones
	juegos = open("juegos.txt")
	juegos_genero = juegos.read()
	lista_juegos = juegos_genero.split("\n")
	juegos.close()
	for juego in lista_juegos:
		archivo_juegos = open("decisiones/" + juego + ".txt")
		datos_juegos = archivo_juegos.read()
		lista_decisiones = datos_juegos.split("\n")
		decisiones.append(lista_decisiones)
		mapa_juegos[str(lista_decisiones)] = juego
		archivo_juegos.close()
		archivo_juegos = open("descripciones de juegos/" + juego + ".txt","r", encoding='UTF-8')
		datos_juegos = archivo_juegos.read()
		mapeo_descripciones[juego] = datos_juegos
		archivo_juegos.close()
		archivo_juegos = open("generos/" + juego + ".txt", "r", encoding='UTF-8')
		datos_juegos = archivo_juegos.read()
		mapeo_definiciones[juego] = datos_juegos
		archivo_juegos.close()
	

def identificar_juego(*arguments):
	lista_decisiones = []
	for juego in arguments:
		lista_decisiones.append(juego)
	# Handle key error
	return mapa_juegos[str(lista_decisiones)]

def get_detalles(juego):
	return mapeo_descripciones[juego]

def get_decisiones(juego):
	return mapeo_definiciones[juego]

def if_not_matched(juego):
		print("")
		id_juego = juego
		detalles_juego = get_detalles(id_juego)
		decisiones = get_decisiones(id_juego)
		print("")
		print("El titulo que mas se acomoda a tus gustos es: %s\n" %id_juego)
		print("una breve descripcion del mismo es :\n")
		print(detalles_juego+"\n")
		print("Los generos que contiene y su duracion aproximada es: \n")
		print(decisiones+"\n")

# @my_decorator is just a way of saying just_some_function = my_decorator(just_some_function)
#def identify_juego(accion, aventura, mundo_abierto, infantil, disparos, mitologia, prota_femenina, historia,medievales ,vista_panoramica,militares):
class Greetings(KnowledgeEngine):
	@DefFacts()
	def _initial_action(self):
		print("")
		print("Hola bienvenido a sugerencias gamers!.")
		yield Fact(action="encontrar_juego")
	

	
	@Rule(Fact(action='encontrar_juego'), NOT(Fact(accion=W())),salience = 1)
	def categoria_0(self):
		self.declare(Fact(accion=input("accion: ")))

	@Rule(Fact(action='encontrar_juego'), NOT(Fact(aventura=W())),salience = 1)
	def categoria_1(self):
		self.declare(Fact(aventura=input("aventura: ")))

	@Rule(Fact(action='encontrar_juego'), NOT(Fact(mundo_abierto=W())),salience = 1)
	def categoria_2(self):
		self.declare(Fact(mundo_abierto=input("mundo abierto: ")))

	@Rule(Fact(action='encontrar_juego'), NOT(Fact(infantil=W())),salience = 1)
	def categoria_3(self):
		self.declare(Fact(infantil=input("infantil: ")))

	@Rule(Fact(action='encontrar_juego'), NOT(Fact(disparos=W())),salience = 1)
	def categoria_4(self):
		self.declare(Fact(disparos=input("disparos: ")))

	@Rule(Fact(action='encontrar_juego'), NOT(Fact(prota_femenina=W())),salience = 1)
	def categoria_5(self):
		self.declare(Fact(prota_femenina=input("prota femenina: ")))
	 
	@Rule(Fact(action='encontrar_juego'), NOT(Fact(militares=W())),salience = 1)
	def categoria_6(self):
		self.declare(Fact(militares=input("militares: ")))
	
	@Rule(Fact(action='encontrar_juego'), NOT(Fact(medievales=W())),salience = 1)
	def categoria_7(self):
		self.declare(Fact(medievales=input("medievales: ")))
	
	@Rule(Fact(action='encontrar_juego'), NOT(Fact(historia=W())),salience = 1)
	def categoria_8(self):
		self.declare(Fact(historia=input("historia: ")))
	
	@Rule(Fact(action='encontrar_juego'), NOT(Fact(mitologia=W())),salience = 1)
	def categoria_9(self):
		self.declare(Fact(mitologia=input("mitologia: ")))
	
	@Rule(Fact(action='encontrar_juego'), NOT(Fact(vista_panoramica=W())),salience = 1)
	def categoria_10(self):
		self.declare(Fact(vista_panoramica=input("vista panoramica: ")))

	@Rule(Fact(action='encontrar_juego'), NOT(Fact(construccion=W())),salience = 1)
	def categoria_11(self):
		self.declare(Fact(construccion=input("construccion: ")))

	@Rule(Fact(action='encontrar_juego'), NOT(Fact(pixel_art=W())),salience = 1)
	def categoria_12(self):
		self.declare(Fact(pixel_art=input("pixel art: ")))

	@Rule(Fact(action='encontrar_juego'), NOT(Fact(comedia=W())),salience = 1)
	def categoria_13(self):
		self.declare(Fact(comedia=input("comedia: ")))

	@Rule(Fact(action='encontrar_juego'), NOT(Fact(lucha=W())),salience = 1)
	def categoria_14(self):
		self.declare(Fact(lucha=input("lucha: ")))

	@Rule(Fact(action='encontrar_juego'), NOT(Fact(primera_persona=W())),salience = 1)
	def categoria_15(self):
		self.declare(Fact(primera_persona=input("primera persona: ")))

	@Rule(Fact(action='encontrar_juego'), NOT(Fact(mundo_post_apocaliptico=W())),salience = 1)
	def categoria_16(self):
		self.declare(Fact(mundo_post_apocaliptico=input("mundo post apocaliptico: ")))

	@Rule(Fact(action='encontrar_juego'), NOT(Fact(frenetico=W())),salience = 1)
	def categoria_17(self):
		self.declare(Fact(frenetico=input("frenetico: ")))

	@Rule(Fact(action='encontrar_juego'), NOT(Fact(gestion=W())),salience = 1)
	def categoria_18(self):
		self.declare(Fact(gestion=input("gestion: ")))

	@Rule(Fact(action='encontrar_juego'), NOT(Fact(sangrientos=W())),salience = 1)
	def categoria_19(self):
		self.declare(Fact(sangrientos=input("sangrientos: ")))

	@Rule(Fact(action='encontrar_juego'), NOT(Fact(interestelar=W())),salience = 1)
	def categoria_20(self):
		self.declare(Fact(interestelar=input("interestelar: ")))

	@Rule(Fact(action='encontrar_juego'), NOT(Fact(plataformas=W())),salience = 1)
	def categoria_21(self):
		self.declare(Fact(plataformas=input("plataformas: ")))

	@Rule(Fact(action='encontrar_juego'), NOT(Fact(asaltos=W())),salience = 1)
	def categoria_22(self):
		self.declare(Fact(asaltos=input("asaltos: ")))

	@Rule(Fact(action='encontrar_juego'), NOT(Fact(lineales=W())),salience = 1)
	def categoria_23(self):
		self.declare(Fact(lineales=input("lineales: ")))

	@Rule(Fact(action='encontrar_juego'), NOT(Fact(mazmorras=W())),salience = 1)
	def categoria_24(self):
		self.declare(Fact(mazmorras=input("mazmorras: ")))	

	@Rule(Fact(action='encontrar_juego'),Fact(accion="si"),Fact(aventura="si"),Fact(mundo_abierto="no"),Fact(infantil="no"),Fact(disparos="si"),Fact(mitologia="no"),Fact(prota_femenina="si"),Fact(historia="no"),Fact(medievales="no"),Fact(vista_panoramica="no"),Fact(militares="no"),Fact(construccion="no"),Fact(pixel_art="no"),Fact(comedia="no"),Fact(lucha="no"),Fact(primera_persona="no"),Fact(mundo_post_apocaliptico="no"),Fact(frenetico="no"),Fact(gestion="no"),Fact(sangrientos="no"),Fact(interestelar="no"),Fact(plataformas="no"),Fact(asaltos="no"),Fact(lineales="no"),Fact(mazmorras="no"))
	def juego_0(self):
		self.declare(Fact(juego="Metroid"))

	@Rule(Fact(action='encontrar_juego'),Fact(accion="si"),Fact(aventura="no"),Fact(mundo_abierto="no"),Fact(infantil="no"),Fact(disparos="si"),Fact(mitologia="no"),Fact(prota_femenina="no"),Fact(historia="no"),Fact(medievales="no"),Fact(vista_panoramica="no"),Fact(militares="si"),Fact(construccion="no"),Fact(pixel_art="no"),Fact(comedia="no"),Fact(lucha="no"),Fact(primera_persona="no"),Fact(mundo_post_apocaliptico="no"),Fact(frenetico="no"),Fact(gestion="no"),Fact(sangrientos="no"),Fact(interestelar="no"),Fact(plataformas="no"),Fact(asaltos="no"),Fact(lineales="no"),Fact(mazmorras="no"))
	def juego_1(self):
		self.declare(Fact(juego="Cod"))

	@Rule(Fact(action='encontrar_juego'),Fact(accion="si"),Fact(aventura="no"),Fact(mundo_abierto="si"),Fact(infantil="no"),Fact(disparos="no"),Fact(mitologia="no"),Fact(prota_femenina="no"),Fact(historia="no"),Fact(medievales="si"),Fact(vista_panoramica="no"),Fact(militares="no"),Fact(construccion="no"),Fact(pixel_art="no"),Fact(comedia="no"),Fact(lucha="no"),Fact(primera_persona="no"),Fact(mundo_post_apocaliptico="no"),Fact(frenetico="no"),Fact(gestion="no"),Fact(sangrientos="no"),Fact(interestelar="no"),Fact(plataformas="no"),Fact(asaltos="no"),Fact(lineales="no"),Fact(mazmorras="no"))
	def juego_2(self):
		self.declare(Fact(juego="Skyrim"))

	@Rule(Fact(action='encontrar_juego'),Fact(accion="si"),Fact(aventura="no"),Fact(mundo_abierto="no"),Fact(infantil="no"),Fact(disparos="si"),Fact(mitologia="no"),Fact(prota_femenina="no"),Fact(historia="si"),Fact(medievales="no"),Fact(vista_panoramica="no"),Fact(militares="no"),Fact(construccion="no"),Fact(pixel_art="no"),Fact(comedia="no"),Fact(lucha="no"),Fact(primera_persona="no"),Fact(mundo_post_apocaliptico="no"),Fact(frenetico="no"),Fact(gestion="no"),Fact(sangrientos="no"),Fact(interestelar="no"),Fact(plataformas="no"),Fact(asaltos="no"),Fact(lineales="no"),Fact(mazmorras="no"))
	def juego_3(self):
		self.declare(Fact(juego="Gears of war"))

	@Rule(Fact(action='encontrar_juego'),Fact(accion="no"),Fact(aventura="si"),Fact(mundo_abierto="si"),Fact(infantil="no"),Fact(disparos="no"),Fact(mitologia="si"),Fact(prota_femenina="no"),Fact(historia="no"),Fact(medievales="no"),Fact(vista_panoramica="no"),Fact(militares="no"),Fact(construccion="no"),Fact(pixel_art="no"),Fact(comedia="no"),Fact(lucha="no"),Fact(primera_persona="no"),Fact(mundo_post_apocaliptico="no"),Fact(frenetico="no"),Fact(gestion="no"),Fact(sangrientos="no"),Fact(interestelar="no"),Fact(plataformas="no"),Fact(asaltos="no"),Fact(lineales="no"),Fact(mazmorras="no"))
	def juego_4(self):
		self.declare(Fact(juego="God of war"))

	@Rule(Fact(action='encontrar_juego'),Fact(accion="si"),Fact(aventura="si"),Fact(mundo_abierto="si"),Fact(infantil="si"),Fact(disparos="no"),Fact(mitologia="no"),Fact(prota_femenina="no"),Fact(historia="no"),Fact(medievales="no"),Fact(vista_panoramica="no"),Fact(militares="no"),Fact(construccion="no"),Fact(pixel_art="no"),Fact(comedia="no"),Fact(lucha="no"),Fact(primera_persona="no"),Fact(mundo_post_apocaliptico="no"),Fact(frenetico="no"),Fact(gestion="no"),Fact(sangrientos="no"),Fact(interestelar="no"),Fact(plataformas="no"),Fact(asaltos="no"),Fact(lineales="no"),Fact(mazmorras="no"))
	def juego_5(self):
		self.declare(Fact(juego="Kirby"))

	@Rule(Fact(action='encontrar_juego'),Fact(accion="no"),Fact(aventura="si"),Fact(mundo_abierto="si"),Fact(infantil="no"),Fact(disparos="no"),Fact(mitologia="no"),Fact(prota_femenina="no"),Fact(historia="no"),Fact(medievales="no"),Fact(vista_panoramica="si"),Fact(militares="no"),Fact(construccion="no"),Fact(pixel_art="no"),Fact(comedia="no"),Fact(lucha="no"),Fact(primera_persona="no"),Fact(mundo_post_apocaliptico="no"),Fact(frenetico="no"),Fact(gestion="no"),Fact(sangrientos="no"),Fact(interestelar="no"),Fact(plataformas="no"),Fact(asaltos="no"),Fact(lineales="no"),Fact(mazmorras="no"))
	def juego_6(self):
		self.declare(Fact(juego="Cult of the lamb"))

	@Rule(Fact(action='encontrar_juego'),Fact(accion="no"),Fact(aventura="no"),Fact(mundo_abierto="si"),Fact(infantil="no"),Fact(disparos="no"),Fact(mitologia="no"),Fact(prota_femenina="no"),Fact(historia="no"),Fact(medievales="no"),Fact(vista_panoramica="no"),Fact(militares="no"),Fact(construccion="si"),Fact(pixel_art="si"),Fact(comedia="no"),Fact(lucha="no"),Fact(primera_persona="no"),Fact(mundo_post_apocaliptico="no"),Fact(frenetico="no"),Fact(gestion="no"),Fact(sangrientos="no"),Fact(interestelar="no"),Fact(plataformas="no"),Fact(asaltos="no"),Fact(lineales="no"),Fact(mazmorras="no"))
	def juego_7(self):
		self.declare(Fact(juego="Terraria"))

	@Rule(Fact(action='encontrar_juego'),Fact(accion="si"),Fact(aventura="no"),Fact(mundo_abierto="no"),Fact(infantil="no"),Fact(disparos="si"),Fact(mitologia="no"),Fact(prota_femenina="no"),Fact(historia="no"),Fact(medievales="no"),Fact(vista_panoramica="no"),Fact(militares="no"),Fact(construccion="no"),Fact(pixel_art="no"),Fact(comedia="si"),Fact(lucha="no"),Fact(primera_persona="no"),Fact(mundo_post_apocaliptico="no"),Fact(frenetico="no"),Fact(gestion="no"),Fact(sangrientos="no"),Fact(interestelar="no"),Fact(plataformas="no"),Fact(asaltos="no"),Fact(lineales="no"),Fact(mazmorras="no"))
	def juego_8(self):
		self.declare(Fact(juego="Borderlands"))

	@Rule(Fact(action='encontrar_juego'),Fact(accion="si"),Fact(aventura="si"),Fact(mundo_abierto="no"),Fact(infantil="no"),Fact(disparos="no"),Fact(mitologia="no"),Fact(prota_femenina="no"),Fact(historia="no"),Fact(medievales="no"),Fact(vista_panoramica="no"),Fact(militares="no"),Fact(construccion="no"),Fact(pixel_art="no"),Fact(comedia="no"),Fact(lucha="si"),Fact(primera_persona="no"),Fact(mundo_post_apocaliptico="no"),Fact(frenetico="no"),Fact(gestion="no"),Fact(sangrientos="no"),Fact(interestelar="no"),Fact(plataformas="no"),Fact(asaltos="no"),Fact(lineales="no"),Fact(mazmorras="no"))
	def juego_9(self):
		self.declare(Fact(juego="Super smash bros"))

	@Rule(Fact(action='encontrar_juego'),Fact(accion="si"),Fact(aventura="no"),Fact(mundo_abierto="no"),Fact(infantil="no"),Fact(disparos="si"),Fact(mitologia="no"),Fact(prota_femenina="no"),Fact(historia="no"),Fact(medievales="no"),Fact(vista_panoramica="no"),Fact(militares="no"),Fact(construccion="no"),Fact(pixel_art="no"),Fact(comedia="no"),Fact(lucha="no"),Fact(primera_persona="si"),Fact(mundo_post_apocaliptico="no"),Fact(frenetico="no"),Fact(gestion="no"),Fact(sangrientos="no"),Fact(interestelar="no"),Fact(plataformas="no"),Fact(asaltos="no"),Fact(lineales="no"),Fact(mazmorras="no"))
	def juego_10(self):
		self.declare(Fact(juego="Kill zone"))

	@Rule(Fact(action='encontrar_juego'),Fact(accion="si"),Fact(aventura="si"),Fact(mundo_abierto="si"),Fact(infantil="no"),Fact(disparos="no"),Fact(mitologia="no"),Fact(prota_femenina="no"),Fact(historia="no"),Fact(medievales="no"),Fact(vista_panoramica="no"),Fact(militares="no"),Fact(construccion="no"),Fact(pixel_art="no"),Fact(comedia="no"),Fact(lucha="no"),Fact(primera_persona="no"),Fact(mundo_post_apocaliptico="si"),Fact(frenetico="no"),Fact(gestion="no"),Fact(sangrientos="no"),Fact(interestelar="no"),Fact(plataformas="no"),Fact(asaltos="no"),Fact(lineales="no"),Fact(mazmorras="no"))
	def juego_11(self):
		self.declare(Fact(juego="Fallout"))

	@Rule(Fact(action='encontrar_juego'),Fact(accion="si"),Fact(aventura="no"),Fact(mundo_abierto="no"),Fact(infantil="no"),Fact(disparos="si"),Fact(mitologia="no"),Fact(prota_femenina="no"),Fact(historia="no"),Fact(medievales="no"),Fact(vista_panoramica="no"),Fact(militares="no"),Fact(construccion="no"),Fact(pixel_art="no"),Fact(comedia="no"),Fact(lucha="no"),Fact(primera_persona="no"),Fact(mundo_post_apocaliptico="no"),Fact(frenetico="si"),Fact(gestion="no"),Fact(sangrientos="no"),Fact(interestelar="no"),Fact(plataformas="no"),Fact(asaltos="no"),Fact(lineales="no"),Fact(mazmorras="no"))
	def juego_12(self):
		self.declare(Fact(juego="Doom eternal"))

	@Rule(Fact(action='encontrar_juego'),Fact(accion="no"),Fact(aventura="si"),Fact(mundo_abierto="si"),Fact(infantil="no"),Fact(disparos="no"),Fact(mitologia="no"),Fact(prota_femenina="no"),Fact(historia="no"),Fact(medievales="no"),Fact(vista_panoramica="no"),Fact(militares="no"),Fact(construccion="no"),Fact(pixel_art="no"),Fact(comedia="no"),Fact(lucha="no"),Fact(primera_persona="no"),Fact(mundo_post_apocaliptico="no"),Fact(frenetico="no"),Fact(gestion="si"),Fact(sangrientos="no"),Fact(interestelar="no"),Fact(plataformas="no"),Fact(asaltos="no"),Fact(lineales="no"),Fact(mazmorras="no"))
	def juego_13(self):
		self.declare(Fact(juego="Animal crossing"))

	@Rule(Fact(action='encontrar_juego'),Fact(accion="no"),Fact(aventura="si"),Fact(mundo_abierto="si"),Fact(infantil="no"),Fact(disparos="no"),Fact(mitologia="no"),Fact(prota_femenina="no"),Fact(historia="no"),Fact(medievales="no"),Fact(vista_panoramica="no"),Fact(militares="no"),Fact(construccion="no"),Fact(pixel_art="si"),Fact(comedia="no"),Fact(lucha="no"),Fact(primera_persona="no"),Fact(mundo_post_apocaliptico="no"),Fact(frenetico="no"),Fact(gestion="si"),Fact(sangrientos="no"),Fact(interestelar="no"),Fact(plataformas="no"),Fact(asaltos="no"),Fact(lineales="no"),Fact(mazmorras="no"))
	def juego_14(self):
		self.declare(Fact(juego="Stardew valley"))

	@Rule(Fact(action='encontrar_juego'),Fact(accion="si"),Fact(aventura="no"),Fact(mundo_abierto="no"),Fact(infantil="no"),Fact(disparos="no"),Fact(mitologia="no"),Fact(prota_femenina="no"),Fact(historia="no"),Fact(medievales="no"),Fact(vista_panoramica="no"),Fact(militares="no"),Fact(construccion="no"),Fact(pixel_art="no"),Fact(comedia="no"),Fact(lucha="si"),Fact(primera_persona="no"),Fact(mundo_post_apocaliptico="no"),Fact(frenetico="no"),Fact(gestion="no"),Fact(sangrientos="si"),Fact(interestelar="no"),Fact(plataformas="no"),Fact(asaltos="no"),Fact(lineales="no"),Fact(mazmorras="no"))
	def juego_15(self):
		self.declare(Fact(juego="Mortal kombat"))

	@Rule(Fact(action='encontrar_juego'),Fact(accion="si"),Fact(aventura="si"),Fact(mundo_abierto="si"),Fact(infantil="no"),Fact(disparos="no"),Fact(mitologia="no"),Fact(prota_femenina="no"),Fact(historia="no"),Fact(medievales="no"),Fact(vista_panoramica="no"),Fact(militares="no"),Fact(construccion="no"),Fact(pixel_art="no"),Fact(comedia="no"),Fact(lucha="no"),Fact(primera_persona="no"),Fact(mundo_post_apocaliptico="no"),Fact(frenetico="no"),Fact(gestion="no"),Fact(sangrientos="no"),Fact(interestelar="no"),Fact(plataformas="no"),Fact(asaltos="no"),Fact(lineales="no"),Fact(mazmorras="no"))
	def juego_16(self):
		self.declare(Fact(juego="Zelda"))

	@Rule(Fact(action='encontrar_juego'),Fact(accion="si"),Fact(aventura="no"),Fact(mundo_abierto="si"),Fact(infantil="no"),Fact(disparos="no"),Fact(mitologia="no"),Fact(prota_femenina="no"),Fact(historia="no"),Fact(medievales="no"),Fact(vista_panoramica="no"),Fact(militares="no"),Fact(construccion="si"),Fact(pixel_art="no"),Fact(comedia="no"),Fact(lucha="no"),Fact(primera_persona="no"),Fact(mundo_post_apocaliptico="no"),Fact(frenetico="no"),Fact(gestion="no"),Fact(sangrientos="no"),Fact(interestelar="no"),Fact(plataformas="no"),Fact(asaltos="no"),Fact(lineales="no"),Fact(mazmorras="no"))
	def juego_17(self):
		self.declare(Fact(juego="Minecraft"))

	@Rule(Fact(action='encontrar_juego'),Fact(accion="no"),Fact(aventura="no"),Fact(mundo_abierto="si"),Fact(infantil="no"),Fact(disparos="si"),Fact(mitologia="no"),Fact(prota_femenina="no"),Fact(historia="no"),Fact(medievales="no"),Fact(vista_panoramica="no"),Fact(militares="no"),Fact(construccion="no"),Fact(pixel_art="no"),Fact(comedia="no"),Fact(lucha="no"),Fact(primera_persona="no"),Fact(mundo_post_apocaliptico="no"),Fact(frenetico="no"),Fact(gestion="no"),Fact(sangrientos="no"),Fact(interestelar="si"),Fact(plataformas="no"),Fact(asaltos="no"),Fact(lineales="no"),Fact(mazmorras="no"))
	def juego_18(self):
		self.declare(Fact(juego="Destiny"))

	@Rule(Fact(action='encontrar_juego'),Fact(accion="si"),Fact(aventura="si"),Fact(mundo_abierto="no"),Fact(infantil="no"),Fact(disparos="no"),Fact(mitologia="no"),Fact(prota_femenina="no"),Fact(historia="no"),Fact(medievales="no"),Fact(vista_panoramica="no"),Fact(militares="no"),Fact(construccion="no"),Fact(pixel_art="no"),Fact(comedia="no"),Fact(lucha="no"),Fact(primera_persona="no"),Fact(mundo_post_apocaliptico="no"),Fact(frenetico="no"),Fact(gestion="no"),Fact(sangrientos="no"),Fact(interestelar="no"),Fact(plataformas="si"),Fact(asaltos="no"),Fact(lineales="no"),Fact(mazmorras="no"))
	def juego_19(self):
		self.declare(Fact(juego="Mario"))

	@Rule(Fact(action='encontrar_juego'),Fact(accion="si"),Fact(aventura="no"),Fact(mundo_abierto="no"),Fact(infantil="no"),Fact(disparos="no"),Fact(mitologia="no"),Fact(prota_femenina="no"),Fact(historia="no"),Fact(medievales="no"),Fact(vista_panoramica="si"),Fact(militares="no"),Fact(construccion="no"),Fact(pixel_art="no"),Fact(comedia="no"),Fact(lucha="si"),Fact(primera_persona="no"),Fact(mundo_post_apocaliptico="no"),Fact(frenetico="no"),Fact(gestion="no"),Fact(sangrientos="no"),Fact(interestelar="no"),Fact(plataformas="no"),Fact(asaltos="no"),Fact(lineales="no"),Fact(mazmorras="no"))
	def juego_20(self):
		self.declare(Fact(juego="League of legends"))

	@Rule(Fact(action='encontrar_juego'),Fact(accion="si"),Fact(aventura="no"),Fact(mundo_abierto="no"),Fact(infantil="no"),Fact(disparos="si"),Fact(mitologia="no"),Fact(prota_femenina="no"),Fact(historia="no"),Fact(medievales="no"),Fact(vista_panoramica="no"),Fact(militares="no"),Fact(construccion="no"),Fact(pixel_art="no"),Fact(comedia="no"),Fact(lucha="no"),Fact(primera_persona="no"),Fact(mundo_post_apocaliptico="no"),Fact(frenetico="no"),Fact(gestion="no"),Fact(sangrientos="no"),Fact(interestelar="no"),Fact(plataformas="no"),Fact(asaltos="si"),Fact(lineales="no"),Fact(mazmorras="no"))
	def juego_21(self):
		self.declare(Fact(juego="GTA"))

	@Rule(Fact(action='encontrar_juego'),Fact(accion="no"),Fact(aventura="si"),Fact(mundo_abierto="no"),Fact(infantil="no"),Fact(disparos="no"),Fact(mitologia="no"),Fact(prota_femenina="no"),Fact(historia="no"),Fact(medievales="no"),Fact(vista_panoramica="no"),Fact(militares="no"),Fact(construccion="no"),Fact(pixel_art="no"),Fact(comedia="no"),Fact(lucha="no"),Fact(primera_persona="no"),Fact(mundo_post_apocaliptico="no"),Fact(frenetico="no"),Fact(gestion="no"),Fact(sangrientos="no"),Fact(interestelar="no"),Fact(plataformas="no"),Fact(asaltos="no"),Fact(lineales="si"),Fact(mazmorras="no"))
	def juego_22(self):
		self.declare(Fact(juego="Subway surfers"))

	@Rule(Fact(action='encontrar_juego'),Fact(accion="si"),Fact(aventura="no"),Fact(mundo_abierto="no"),Fact(infantil="no"),Fact(disparos="si"),Fact(mitologia="no"),Fact(prota_femenina="no"),Fact(historia="no"),Fact(medievales="no"),Fact(vista_panoramica="no"),Fact(militares="no"),Fact(construccion="no"),Fact(pixel_art="no"),Fact(comedia="no"),Fact(lucha="no"),Fact(primera_persona="no"),Fact(mundo_post_apocaliptico="no"),Fact(frenetico="no"),Fact(gestion="no"),Fact(sangrientos="no"),Fact(interestelar="no"),Fact(plataformas="no"),Fact(asaltos="no"),Fact(lineales="no"),Fact(mazmorras="si"))
	def juego_23(self):
		self.declare(Fact(juego="The binding of isaac"))

	@Rule(Fact(action='encontrar_juego'),Fact(accion="si"),Fact(aventura="si"),Fact(mundo_abierto="no"),Fact(infantil="no"),Fact(disparos="no"),Fact(mitologia="no"),Fact(prota_femenina="no"),Fact(historia="no"),Fact(medievales="no"),Fact(vista_panoramica="no"),Fact(militares="no"),Fact(construccion="no"),Fact(pixel_art="no"),Fact(comedia="si"),Fact(lucha="no"),Fact(primera_persona="no"),Fact(mundo_post_apocaliptico="no"),Fact(frenetico="no"),Fact(gestion="no"),Fact(sangrientos="no"),Fact(interestelar="no"),Fact(plataformas="no"),Fact(asaltos="no"),Fact(lineales="no"),Fact(mazmorras="no"))
	def juego_24(self):
		self.declare(Fact(juego="Castle crashers"))

	@Rule(Fact(action='encontrar_juego'),Fact(juego=MATCH.juego),salience = -998)
	def juego(self, juego):
		print("")
		id_juego = juego
		juego_details = get_detalles(id_juego)
		treatments = get_decisiones(id_juego)
		print("")
		print("El juego que mas se acomoda a sus gustos seria %s\n" %(id_juego))
		print("Una breve descripcion del mismo: \n")
		print(juego_details+"\n")
		print("su duracion aproximada y los generos a los que pertenece: \n")
		print(treatments+"\n")

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
		  Fact(pixel_art=MATCH.pixel_art),NOT(Fact(juego=MATCH.juego)),salience = -999)

	def not_matched(self,accion, aventura, mundo_abierto, infantil, disparos, mitologia, prota_femenina, historia,medievales ,vista_panoramica ,militares ,construccion ,pixel_art, comedia, lucha, primera_persona, mundo_post_apocaliptico, frenetico, gestion, sangrientos, interestelar, plataformas, asaltos, lineales, mazmorras):
		print("\nno se encontro un juego que cumpla con todos los generos, pero este seria un aproximado a sus gustos.")
		lis = [accion, aventura, mundo_abierto, infantil, disparos, mitologia, prota_femenina, historia,medievales ,vista_panoramica ,militares ,construccion ,pixel_art, comedia, lucha, primera_persona, mundo_post_apocaliptico, frenetico, gestion, sangrientos, interestelar, plataformas, asaltos, lineales, mazmorras]
		max_count = 0
		max_juego = ""
		for key,val in mapa_juegos.items():
			count = 0
			temp_list = eval(key)
			for j in range(0,len(lis)):
				if(temp_list[j] == lis[j] and lis[j] == "si"):
					count = count + 1
			if count > max_count:
				max_count = count
				max_juego = val
		if_not_matched(max_juego)


if __name__ == "__main__":
	preprocess()
	engine = Greetings()
	while(1):
		engine.reset()  # Prepare the engine for the execution.
		engine.run()  # Run it!
		print("le gustaria volver a probar el sistema experto?")
		if input() == "no":
			exit()
		#print(engine.facts)