import sqlite3

# main driver
def main():
    while True:
        print("\nMenu:")
        print("1 - Opção 1")
        print("2 - Opção 2")
        print("3 - Opção 3")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            print("1")
        elif opcao == '2':
            print("2")
        elif opcao == '3':
            print("3")
        elif opcao == '0':
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()