nome = input("Nome do titular: ")
saldo = float(input("Seu saldo inicial:  "))
limite = float(input("Limite de saque:  "))
extrato = []

while True:
    print("""
    1 - Consultar saldo
    2 - Depositar
    3 - Sacar
    4 - Extrato
    5 - Sair
    """)

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print(f"Saldo atual: R$ {saldo:}")

    elif opcao == "2":
        valor = float(input("Valor do depósito: R$ "))
        if valor > 0:
            saldo += valor
            extrato.append(f"Depósito: +R$ {valor:} | Saldo: R$ {saldo:}")
            print("Depósito realizado!")
        else:
            print("Valor inválido.")

    elif opcao == "3":
        valor = float(input("Valor do saque: R$ "))
        if valor > saldo:
            print("Saldo insuficiente.")
        elif valor > limite:
            print("Valor acima do limite de saque.")
        elif valor <= 0:
            print("Valor inválido.")
        else:
            saldo -= valor
            extrato.append(f"Saque: -R$ {valor:} | Saldo: R$ {saldo:}")
            print("Saque realizado!")

    elif opcao == "4":
        
        if len(extrato) == 0:
            print("Nenhuma movimentação feita.")
        else:
            for movimentacao in extrato:
                print(movimentacao)
        print(f"Saldo atual: R$ {saldo:}")

    elif opcao == "5":
        print("Saindo... ")
        break

    else:
        print("Opção inválida.")