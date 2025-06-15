from database.connection import get_connection

class Paciente:
    def __init__(self, idPaciente, nome, senha, origem, tolerancia, Medicanico_idMedicanico=None):
        self.idPaciente = idPaciente
        self.nome = nome
        self.senha = senha
        self.origem = origem
        self.tolerancia = tolerancia
        self.Medicanico_idMedicanico = Medicanico_idMedicanico

    def create(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Paciente (idPaciente, nome, senha, origem, tolerancia, Medicanico_idMedicanico) VALUES (?, ?, ?, ?, ?, ?)", (self.idPaciente, self.nome, self.senha, self.origem, self.tolerancia, self.Medicanico_idMedicanico))
        conn.commit()
        cursor.close()
        conn.close()