from database.connection import get_connection

class Consulta:

    @staticmethod
    def create(idPaciente, idMedicanico, idConsulta, preco):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Consulta (idConsulta, idPaciente, idMedicanico, preco) VALUES (?, ?, ?, ?)", (idPaciente, idMedicanico, idConsulta, preco))
        conn.commit()
        cursor.close()
        conn.close()