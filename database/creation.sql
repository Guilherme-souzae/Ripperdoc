-- todos os precos sao tratados como INTEGER (ou edinhos)
-- todas as datas sao tratadas como string (ex: '2077-06-02T14:00:00')

PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS Medicanico (
  idMedicanico INTEGER PRIMARY KEY,
  nome TEXT NOT NULL,
  senha TEXT NOT NULL,
  reputacao INTEGER NOT NULL,
  preco INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS Paciente (
  idPaciente INTEGER PRIMARY KEY,
  nome TEXT NOT NULL,
  senha TEXT NOT NULL,
  origem TEXT NOT NULL,
  psicose INTEGER NOT NULL,
  tolerancia INTEGER NOT NULL,
  dinheiro INTEGER NOT NULL,
  Medicanico_idMedicanico INTEGER, -- medicanico fixo do paciente, para onde o mesmo eh enviado em caso de emergencia, apesar de improvavel um paciente pode nao ter um medicanico fixo
  FOREIGN KEY (Medicanico_idMedicanico)
    REFERENCES Medicanico(idMedicanico)
    ON DELETE NO ACTION
);

CREATE TABLE IF NOT EXISTS Consulta (
  dataHora TEXT NOT NULL,
  preco INTEGER NOT NULL,
  Paciente_idPaciente INTEGER NOT NULL,
  Medicanico_idMedicanico INTEGER NOT NULL,
  PRIMARY KEY (Paciente_idPaciente, Medicanico_idMedicanico, dataHora), -- consultas sao tratadas como entidades fracas formadas pela PK do medicanico, paciente e sua data e hora
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
  PRIMARY KEY (Cromo_idCromo, Paciente_idPaciente),
  FOREIGN KEY (Paciente_idPaciente)
    REFERENCES Paciente(idPaciente)
    ON DELETE CASCADE,
  FOREIGN KEY (Cromo_idCromo)
    REFERENCES Cromo(idCromo)
    ON DELETE CASCADE
);