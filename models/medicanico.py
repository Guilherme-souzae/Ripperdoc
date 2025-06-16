from database.connection import get_connection

class Medicanico:

    @staticmethod
    def create(idMedicanico, nome, senha, reputacao, preco):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Medicanico (idMedicanico, nome, senha, reputacao, preco) VALUES (?, ?, ?, ?, ?)", (idMedicanico, nome, senha, reputacao, preco))
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def check_if_name_exists(nome):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT idMedicanico FROM Medicanico WHERE nome = ?", (nome,))
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
        cursor.execute("SELECT idMedicanico FROM Medicanico WHERE idMedicanico = ? AND senha = ?", (cpf, senha))
        result = cursor.fetchone()
        if result == None:
            return False
        else:
            return True

    @staticmethod
    def get_cpf_from_name(name):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT idMedicanico FROM Medicanico WHERE nome = ?", (name,))
        result = cursor.fetchone()
        conn.close()
        if result == None:
            return None
        else:
            return result[0]