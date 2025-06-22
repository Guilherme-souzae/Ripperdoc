from database.connection import get_connection

class Instalacao:

    @staticmethod
    def create(idCromo, idPaciente):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Instalacao (Cromo_idCromo, Paciente_idPaciente) VALUES (?, ?)", (idCromo, idPaciente))
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def read_cromos(idPaciente):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT Cromo.fabricante, Cromo.nome FROM Instalacao JOIN Cromo ON Instalacao.Cromo_idCromo = Cromo.idCromo WHERE Instalacao.Paciente_idPaciente = ?", (idPaciente,))
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        return result