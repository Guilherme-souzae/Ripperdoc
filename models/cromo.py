from database.connection import get_connection

class Cromo:

    @staticmethod
    def create(nome, fabricante, preco, psicose, parte):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Cromo (nome, fabricante, preco, psicose, parte) VALUES (?, ?, ?, ?, ?)", (nome, fabricante, preco, psicose, parte))
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def read(id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Cromo WHERE idCromo = ?", (id,))
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def read_all_id():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Cromo ORDER BY idCromo DESC")
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        return [dict(row) for row in result]

    @staticmethod
    def read_all_preco():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Cromo ORDER BY preco DESC")
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        return [dict(row) for row in result]

    @staticmethod
    def read_all_fabricante(fabricante):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Cromo WHERE fabricante = ?", (fabricante,))
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        return [dict(row) for row in result]

    @staticmethod
    def read_preco(idCromo):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT preco FROM Cromo WHERE idCromo = ?", (idCromo,))
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def model_input():
        id_exists = None
        while id_exists is None:
            id = input("Digite o ID:")
            id_exists = Cromo.read(id)

        return id