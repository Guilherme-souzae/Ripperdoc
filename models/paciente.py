from database.connection import get_connection

class Paciente:

    @staticmethod
    def create(idPaciente, nome, senha, origem, tolerancia):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Paciente (idPaciente, nome, senha, origem, psicose, tolerancia, dinheiro, Medicanico_idMedicanico) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (idPaciente, nome, senha, origem, 0, tolerancia, 0, None))
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
    def deposit(cpf, edinhos):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE Paciente SET dinheiro = dinheiro + ? WHERE idPaciente = ?", (edinhos, cpf))
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
        cursor.execute("SELECT * FROM Paciente WHERE idPaciente = ? AND senha = ?", (cpf, senha))
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