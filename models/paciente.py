from database.connection import get_connection

class Paciente:

    @staticmethod
    def create(idPaciente, nome, origem, tolerancia):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Paciente (idPaciente, nome, origem, tolerancia, dinheiro) VALUES (?, ?, ?, ?, ?)", (idPaciente, nome, origem, tolerancia, 0))
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def remove(cpf):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Paciente WHERE idPaciente = ?", (cpf,))
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
    def read_all():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Paciente WHERE idPaciente")
        result = cursor.fetchall()
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
    def somar_psicose_instalada(cpf):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT SUM(Cromo.psicose) FROM Instalacao JOIN Cromo ON Instalacao.Cromo_idCromo = Cromo.idCromo WHERE Instalacao.Paciente_idPaciente = ?",(cpf,))
        result = cursor.fetchone()
        cursor.close()
        conn.close()

        return result["SUM(Cromo.psicose)"] if result and result["SUM(Cromo.psicose)"] is not None else 0

    @staticmethod
    def model_input():
        id_exists = None
        while id_exists is None:
            id = input("Digite o cpf do paciente:")
            id_exists = Paciente.read(id)

        return id