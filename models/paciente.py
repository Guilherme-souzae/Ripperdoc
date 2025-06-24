from database.connection import get_connection

class Paciente:

    @staticmethod
    def create(idPaciente, nome, origem, tolerancia):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Paciente (idPaciente, nome, origem, psicose, tolerancia, dinheiro, Medicanico_idMedicanico) VALUES (?, ?, ?, ?, ?, ?, ?)", (idPaciente, nome, origem, 0, tolerancia, 0, None))
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def read(cpf):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Paciente WHERE idPaciente = ?", (cpf,))
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def read_dinheiro(cpf):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT dinheiro FROM Paciente WHERE idPaciente = ?", (cpf,))
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def deposit(cpf, edinhos):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE Paciente SET dinheiro = dinheiro + ? WHERE idPaciente = ?", (edinhos, cpf))
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def model_input():
        id_exists = None
        while id_exists is None:
            id = input("Digite seu CPF:")
            id_exists = Paciente.read(id)

        return id