PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS Medicanico (
  idMedicanico INTEGER PRIMARY KEY,
  nome TEXT NOT NULL,
  preco INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS Paciente (
  idPaciente INTEGER PRIMARY KEY,
  nome TEXT NOT NULL,
  origem TEXT NOT NULL,
  tolerancia INTEGER NOT NULL,
  dinheiro INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS Consulta (
  idConsulta INTEGER NOT NULL,
  Paciente_idPaciente INTEGER NOT NULL,
  Medicanico_idMedicanico INTEGER NOT NULL,
  preco INTEGER NOT NULL,
  PRIMARY KEY (Paciente_idPaciente, Medicanico_idMedicanico, idConsulta),
  FOREIGN KEY (Paciente_idPaciente)
    REFERENCES Paciente(idPaciente)
    ON DELETE CASCADE,
  FOREIGN KEY (Medicanico_idMedicanico)
    REFERENCES Medicanico(idMedicanico)
    ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS Cromo (
  idCromo INTEGER PRIMARY KEY AUTOINCREMENT,
  nome TEXT NOT NULL,
  fabricante TEXT NOT NULL,
  preco INTEGER NOT NULL,
  psicose INTEGER NOT NULL,
  parte TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS Instalacao (
  Cromo_idCromo INTEGER,
  Paciente_idPaciente INTEGER,
  Consulta_Paciente_idPaciente INTEGER NOT NULL,
  Consulta_Medicanico_idMedicanico INTEGER NOT NULL,
  Consulta_idConsulta INTEGER NOT NULL,
  PRIMARY KEY (Cromo_idCromo, Paciente_idPaciente),
  FOREIGN KEY (Paciente_idPaciente)
    REFERENCES Paciente(idPaciente)
    ON DELETE CASCADE,
  FOREIGN KEY (Cromo_idCromo)
    REFERENCES Cromo(idCromo)
    ON DELETE CASCADE,
  FOREIGN KEY (Consulta_Paciente_idPaciente, Consulta_Medicanico_idMedicanico, Consulta_idConsulta)
    REFERENCES Consulta(Paciente_idPaciente, Medicanico_idMedicanico, idConsulta)
    ON DELETE CASCADE
);