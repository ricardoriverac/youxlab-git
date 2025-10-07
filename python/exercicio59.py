def mostrar_menu():
    print("\n--- Menu de Opções ---")
    print("1. Opção 1: Exibir mensagem")
    print("2. Opção 2: Realizar cálculo")
    print("3. Sair")

def acao_opcao_1():
    print("Você escolheu a Opção 1!")

def acao_opcao_2():
    print("Você escolheu a Opção 2! Calculando...")
    resultado = 10 + 5
    print(f"O resultado é: {resultado}")

def main():
    while True: 
        mostrar_menu()
        escolha = input("Digite o número da opção desejada: ")

        if escolha == '1':
            acao_opcao_1()
        elif escolha == '2':
            acao_opcao_2()
        elif escolha == '3':
            print("Saindo do programa. Até logo!")
            break 
        else:
            print("Opção inválida. Por favor, tente novamente.")


