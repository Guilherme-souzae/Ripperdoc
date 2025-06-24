from database.connection import get_connection

class Consulta:

    @staticmethod
    def create(idPaciente, idMedicanico, idConsulta, preco):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Consulta (idConsulta, Paciente_idPaciente, Medicanico_idMedicanico, preco) VALUES (?, ?, ?, ?)",(idConsulta, idPaciente, idMedicanico, preco))  # Corrigida a ordem dos parâmetros
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def read_medicanico(iMedicanico):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT idConsulta, Paciente_idPaciente, preco FROM Consulta WHERE Medicanico_idMedicanico = ?", (iMedicanico,))
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        return result