from database.connection import get_connection

class Cromo:
    def __init__(self, idCromo, nome, fabricante, preco, psicose, parte):
        self.idCromo = idCromo
        self.nome = nome
        self.fabricante = fabricante
        self.preco = preco
        self.psicose = psicose
        self.parte = parte

    def create(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Cromo (idCromo, nome, fabricante, preco, psicose, parte) VALUES (?, ?, ?, ?, ?, ?)", (self.idCromo, self.nome, self.fabricante, self.preco, self.psicose, self.parte))
        conn.commit()
        cursor.close()
        conn.close()