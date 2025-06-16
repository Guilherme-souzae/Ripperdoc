import random

from models import medicanico
from models.cromo import Cromo
from models.medicanico import Medicanico
from models.paciente import Paciente
from frescura.img_to_text import show_logo
from database.connection import init_db

# cadastros
def cadastrar_medicanico():
    nome = input("Digite seu nome: ")
    senha = input("Digite sua senha: ")
    ssn = input("Digite seu CPF: ")
    reputacao = 0
    preco = input("Digite seu preço fixo: ")

    Medicanico.create(ssn, nome, senha, reputacao, preco)

def cadastrar_paciente():
    nome = input("Digite seu nome:")
    senha = input("Digite sua senha:")
    cpf = input("Digite seu CPF:")
    origem = input("Digite sua origem:")
    tolerancia = round(max(0, min(100, random.gauss(50, 15))))

    Paciente.create(cpf, nome, senha, origem, tolerancia)

# logins
def logar_medicanico():
    opt = input("Digite 0 para entrar com CPF, digite 1 para entrar com nome")
    if opt == "0":
        cpf = input("Digite seu CPF: ")
    elif opt == "1":
        nome = input("Digite seu nome: ")
        if Medicanico.check_if_name_exists(nome):
            print("Seu nome já está cadastrado! Entre com seu CPF")
            cpf = input("Digite seu CPF: ")
        else:
            cpf = Medicanico.get_cpf_from_name(nome)
    else:
        print("Opção invalida")
        return

    senha = input("Digite sua senha: ")

    if Medicanico.autenticate(cpf, senha):
        print("Medicânico autenticado com sucesso!")
        menu_medicanico(cpf)
    else:
        print("Senha incorreta!")

def logar_paciente():
    opt = input("Digite 0 para entrar com CPF, digite 1 para entrar com nome")
    if opt == "0":
        cpf = input("Digite seu CPF: ")
    elif opt == "1":
        nome = input("Digite seu nome: ")
        if Medicanico.check_if_name_exists(nome):
            print("Seu nome já está cadastrado! Entre com seu CPF")
            cpf = input("Digite seu CPF: ")
        else:
            cpf = Paciente.get_cpf_from_name(nome)
    else:
        print("Opção invalida")
        return

    senha = input("Digite sua senha: ")

    if Medicanico.autenticate(cpf, senha):
        print("Paciente autenticado com sucesso!")
        menu_paciente(cpf)
    else:
        print("Senha incorreta!")

# menus
def menu_medicanico(cpf):
    pass

def menu_paciente(cpf):
    print("\nMenu de paciente:")
    print("0 - Acessar Loja")

    opcao = input("Escolha uma opção: ")

    if opcao == '0':
        acessar_loja()

# ações
def acessar_loja():
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
        show_logo(fabricante)
        dados = Cromo.read_all_fabricante(fabricante)
        for cromo in dados:
            print(cromo)
    else:
        print("Opcao invalida")

# etc
def lancar_cromo():
    nome = input("Digite o nome do cromo: ")
    fabricante = input("Digite o fabricante: ")
    preco = input("Digite o preço: ")
    psicose = input("Digite o nível de psicose: ")
    parte = input("Digite a parte do corpo: ")

    Cromo.create(nome, fabricante, preco, psicose, parte)

# main driver
def main():
    init_db()

    while True:
        print("\nMenu:")
        print("1 - Cadastrar medicânico")
        print("2 - Cadastrar paciente")
        print("3 - Logar como medicânico")
        print("4 - Logar como paciente")
        print("5 - Lançar novo cromo no mercado")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_medicanico()
        elif opcao == '2':
            cadastrar_paciente()
        elif opcao == '3':
            logar_medicanico()
        elif opcao == '4':
            logar_paciente()
        elif opcao == '5':
            lancar_cromo()
        elif opcao == '0':
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()