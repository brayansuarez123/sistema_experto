from mysql.connector.connection import MySQLConnection


class Service:
    def __init__(self, db: MySQLConnection):
        self.db = db

    def consultar_juegos(self):
        cursor = self.db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM game")
        result = cursor.fetchall()
        cursor.close()
        return result

    def consultar_generos_por_juego(self):
        cursor = self.db.cursor(dictionary=True)
        sql = """
        SELECT title, genre.name, gg.value from game
        JOIN game_genre as gg ON gg.id_game = game.id
        JOIN genre ON gg.id_genre = genre.id
        """
        cursor.execute(sql)
        result_raw: list[dict] = cursor.fetchall()
        cursor.close()
        result = {}
        for row in result_raw:
            juego_nombre = row.get("title")
            genres_dict = result.get(juego_nombre, {})
            genres_dict[row.get("name")] = row.get("value")
            result[juego_nombre] = genres_dict
        return result

    def consultar_juego_por_nombre(self, name: str):
        cursor = self.db.cursor(dictionary=True)
        sql = """
        SELECT g.id as id, g.title as titulo, g.description as descripcion, g.image_url, genre.name as genero
        from game as g JOIN game_genre as gg ON gg.id_game = g.id
        JOIN genre ON gg.id_genre = genre.id
        WHERE g.title = %s AND gg.value = 'si'
        """
        cursor.execute(sql, (name,))
        result_raw = cursor.fetchall()
        result = {}
        for row in result_raw:
            result["titulo"] = row["titulo"]
            result["descripcion"] = row["descripcion"]
            result["id"] = row["id"]
            result["image_url"] = row["image_url"]
            result["generos"] = (*result.get("generos", ()), row["genero"])
        cursor.close()
        return result

    def consultar_generos_por_un_juego(self, title):
        cursor = self.db.cursor(dictionary=True)
        sql = """
        SELECT genre.name, gg.value from game
        JOIN game_genre as gg ON gg.id_game = game.id
        JOIN genre ON gg.id_genre = genre.id
        WHERE game.title = %s
        """
        cursor.execute(sql, (title,))
        result_raw = cursor.fetchall()
        result = {}
        for row in result_raw:
            result[row["name"]] = row["value"]
        cursor.close()
        return result


if __name__ == "__main__":
    from database import db
    s = Service(db)
    print(s.consultar_generos_por_un_juego("Animal crossing")["aventura"])
