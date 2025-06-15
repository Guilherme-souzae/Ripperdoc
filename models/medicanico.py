from database.connection import get_connection

class Medicanico:
    def __init__(self, idMedicanico, nome, senha ,reputacao, preco):
        self.idMedicanico = idMedicanico
        self.nome = nome
        self.senha = senha
        self.reputacao = reputacao
        self.preco = preco

    def create(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Medicanico (idMedicanico, nome, senha, reputacao, preco) VALUES (?, ?, ?, ?, ?)", (self.idMedicanico, self.nome, self.senha, self.reputacao, self.preco))
        conn.commit()
        self.idMedicanico = cursor.lastrowid
        cursor.close()
        conn.close()

    def delete(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Medicanico WHERE idMedicanico = ?", (self.idMedicanico,))
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def check_if_name_exists(nome):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Medicanico WHERE nome = ?", (nome,))
        result = cursor.fetchone()
        conn.close()
        if result == None:
            return False
        else:
            return True

    @staticmethod
    def autenticate(cpf, senha):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Medicanico WHERE cpf = ? AND senha = ?", (cpf, senha))
        result = cursor.fetchone()
        if result == None:
            return False
        else:
            return True

    @staticmethod
    def get_cpf_from_name(name):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Medicanico WHERE nome = ?", (name,))
        result = cursor.fetchone()
        conn.close()
        if result == None:
            return None
        else:
            return result[0]