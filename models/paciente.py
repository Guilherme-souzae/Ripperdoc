from database.connection import get_connection

class Paciente:

    @staticmethod
    def create(idPaciente, nome, senha, origem, tolerancia, Medicanico_idMedicanico):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Paciente (idPaciente, nome, senha, origem, tolerancia, Medicanico_idMedicanico) VALUES (?, ?, ?, ?, ?, ?)", (idPaciente, nome, senha, origem, tolerancia, Medicanico_idMedicanico))
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def check_if_name_exists(nome):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Paciente WHERE nome = ?", (nome,))
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
        cursor.execute("SELECT * FROM Paciente WHERE cpf = ? AND senha = ?", (cpf, senha))
        result = cursor.fetchone()
        if result == None:
            return False
        else:
            return True

    @staticmethod
    def get_cpf_from_name(name):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Paciente WHERE nome = ?", (name,))
        result = cursor.fetchone()
        conn.close()
        if result == None:
            return None
        else:
            return result[0]