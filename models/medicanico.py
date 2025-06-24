from database.connection import get_connection

class Medicanico:

    @staticmethod
    def create(idMedicanico, nome, reputacao, preco):
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
    def read(cpf):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Medicanico WHERE idMedicanico = ?", (cpf,))
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def read_all():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Medicanico")
        result = cursor.fetchall()
        conn.close()
        return result

    @staticmethod
    def model_input():
        id_exists = None
        while id_exists is None:
            id = input("Digite seu CPF:")
            id_exists = Medicanico.read(id)

        return id