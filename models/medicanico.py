from database.connection import get_connection

class Medicanico:

    @staticmethod
    def create(idMedicanico, nome, preco):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Medicanico (idMedicanico, nome, preco) VALUES (?, ?, ?)", (idMedicanico, nome, preco))
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def remove(cpf):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Medicanico WHERE idMedicanico = ?", (cpf,))
        conn.commit()
        cursor.close()
        conn.close()

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
            id = input("Digíte o cpf do medicânico:")
            id_exists = Medicanico.read(id)

        return id