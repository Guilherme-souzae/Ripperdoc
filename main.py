import random
import time

from models.Instalacao import Instalacao
from models.cromo import Cromo
from models.medicanico import Medicanico
from models.paciente import Paciente
from models.consulta import Consulta
from database.connection import init_db

# === CADASTROS ===

def cadastrar_medicanico():
    cpf = input("Digite seu CPF: ")
    nome = input("Digite seu nome: ")
    preco = input("Digite seu preço fixo: ")

    Medicanico.create(cpf, nome, preco)


def cadastrar_paciente():
    cpf = input("Digite seu CPF:")
    nome = input("Digite seu nome:")
    origem = input("Digite sua origem:")
    tolerancia = round(max(0, min(100, random.gauss(50, 15))))

    Paciente.create(cpf, nome, origem, tolerancia)


# === CADASTROS ===

def remover_medicanico():
    cpf = Medicanico.model_input()
    Medicanico.remove(cpf)

def remover_paciente():
    cpf = Paciente.model_input()
    Paciente.remove(cpf)

# === AÇÕES ===

def criar_consulta(dia_atual):
    cpf_paciente = Paciente.model_input()
    cpf_medicanico = Medicanico.model_input()

    num_instalacoes = int(input("Digite quantos cromos deseja instalar:"))
    preco_total = 0
    psicose_total = 0
    cromos_a_serem_instalados = []

    for i in range(num_instalacoes):
        idCromo = Cromo.model_input()
        cromos_a_serem_instalados.append(idCromo)
        preco_total += int(Cromo.read(idCromo)["preco"])
        psicose_total += int(Cromo.read(idCromo)["psicose"])

    if preco_total > Paciente.read(cpf_paciente)["dinheiro"]:
        print("Saldo insuficiente, cancelando consulta")
        return

    if psicose_total > Paciente.read(cpf_paciente)["tolerancia"] - Paciente.somar_psicose_instalada(cpf_paciente):
        print("A instalação vai te tornar um cyberpsicopata, cancelando consulta")
        return

    Paciente.deposit(cpf_paciente, -preco_total)
    Consulta.create(cpf_paciente, cpf_medicanico, dia_atual, preco_total)
    for i in range(num_instalacoes):
        Instalacao.create(int(cromos_a_serem_instalados[i]), cpf_paciente, cpf_medicanico, dia_atual)

    dia_atual += 1


def log_medicanico():
    cpf_medicanico = Medicanico.model_input()
    consultas = Consulta.read_medicanico(cpf_medicanico)

    if not consultas:
        print("\nNenhuma consulta encontrada para este medicânico.")
        return

    print(f"\nConsultas do medicânico {cpf_medicanico}:")

    total_valor = 0
    for consulta in consultas:
        print(f"ID da Consulta: {consulta['idConsulta']}")
        print(f"CPF do Paciente: {consulta['Paciente_idPaciente']}")
        print(f"Preço: {consulta['preco']}")
        print()  # espaço entre os blocos

        total_valor += consulta['preco']

    print(f"Total de consultas: {len(consultas)}")
    print(f"Valor total recebido: {total_valor}")


def lancar_cromo():
    nome = input("Digite o nome do cromo: ")
    fabricante = input("Digite o fabricante: ")
    preco = input("Digite o preço: ")
    psicose = input("Digite o nível de psicose: ")
    parte = input("Digite a parte do corpo: ")

    Cromo.create(nome, fabricante, preco, psicose, parte)


def executar_varredura():
    cpf = Paciente.model_input()
    dados = Paciente.read(cpf)
    instalacoes = Instalacao.read_cromos(cpf)

    print("CPF: ", dados["idPaciente"])
    print("Nome: ", dados["nome"])
    print("Origem: ", dados["origem"])
    print("Cyberpsicose: ", Paciente.somar_psicose_instalada(cpf), "/", dados["tolerancia"])
    print("Carteira: ", dados["dinheiro"])

    if not instalacoes:
        print("Nenhum cromo instalado.")
    else:
        for c in instalacoes:
            print(f"{c['fabricante']} - {c['nome']}")


def depositar():
    cpf = Paciente.model_input()
    deposito = input("\nQuanto deseja depositar?:")
    Paciente.deposit(cpf, deposito)


def acessar_catalogo():
    print("\nLoja:")
    print("0 - Exibir todos os cromos por lançamento")
    print("1 - Exibir todos os cromos por preço")
    print("2 - Escolher fabricante")
    opcao = input("Escolha uma opção: ")

    if opcao == "0":
        dados = Cromo.read_all_id()
        for cromo in dados:
            print(cromo)
    elif opcao == "1":
        dados = Cromo.read_all_preco()
        for cromo in dados:
            print(cromo)
    elif opcao == "2":
        fabricante = input("Digite o fabricante: ")
        dados = Cromo.read_all_fabricante(fabricante)
        for cromo in dados:
            print(cromo)
    else:
        print("Opcao invalida")


def exibir_ids():
    medicanicos = Medicanico.read_all()
    pacientes = Paciente.read_all()

    print("\nMedicânicos cadastrados:")
    if medicanicos:
        for m in medicanicos:
            print(f"- {m['idMedicanico']}")
    else:
        print("Nenhum medicânico cadastrado.")

    print("\nPacientes cadastrados:")
    if pacientes:
        for p in pacientes:
            print(f"- {p['idPaciente']}")
    else:
        print("Nenhum paciente cadastrado.")


# === MAIN DRIVER ===

def main():
    init_db()

    while True:
        timestamp = int(time.time())

        try:
            print("\nMenu:")
            print("1 - Cadastrar medicânico")
            print("2 - Cadastrar paciente")
            print("3 - Criar consulta")
            print("4 - Log do medicânico")
            print("5 - Lançar novo cromo no mercado")
            print("6 - Executar varredura no paciente")
            print("7 - Depositar dinheiro no paciente")
            print("8 - Consultar catálogo de cromos")
            print("9 - Exibir todos os IDs de medicânicos e pacientes")
            print("0 - Sair")
            opcao = input("Escolha uma opção: ")

            if opcao == '1':
                cadastrar_medicanico()
            elif opcao == '2':
                cadastrar_paciente()
            elif opcao == '3':
                criar_consulta(timestamp)
            elif opcao == '4':
                log_medicanico()
            elif opcao == '5':
                lancar_cromo()
            elif opcao == '6':
                executar_varredura()
            elif opcao == '7':
                depositar()
            elif opcao == '8':
                acessar_catalogo()
            elif opcao == '9':
                exibir_ids()
            elif opcao == '0':
                break
            else:
                print("Opção inválida.")
        except Exception as e:
            print(f"Ocorreu um erro: {e}")


if __name__ == "__main__":
    main()