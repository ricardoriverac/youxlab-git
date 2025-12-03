def cadastro():
    print(" → Cadastro ←")
    nome = input("Nome do titular da conta: ")
    saldo_inicial = float(input("Qual o saldo inicial: R$ "))
    limite_saque = float(input("Qual o limite máximo permitido por saque: R$ "))
    
    usuario = {
        "nome": nome,
        "saldo": saldo_inicial,
        "limite": limite_saque,
        "extrato": []
    }
    print(f"Conta criada para {nome}!")
    return usuario


def consultar_saldo(usuario):
    print(f"Saldo atual: R$ {usuario['saldo']:.2f}")


def depositar(usuario):
    valor = float(input("Valor para depósito: R$ "))
    if valor > 0:
        usuario["saldo"] += valor
        usuario["extrato"].append(("Depósito", valor, usuario["saldo"]))
        print(f"Depósito de R$ {valor:.2f} realizado!")
    else:
        print("Valor inválido para depósito")


def sacar(usuario):
    valor = float(input("Valor para saque: R$ "))
    if valor <= 0:
        print("Valor inválido.")
    elif valor > usuario["limite"]:
        print(f"Saque acima do limite permitido de R$ {usuario['limite']:.2f}")
    elif valor > usuario["saldo"]:
        print("Saldo insuficiente")
    else:
        usuario["saldo"] -= valor
        usuario["extrato"].append(("Saque", valor, usuario["saldo"]))
        print(f"Saque de R$ {valor:.2f} realizado!")


def exibir_extrato(usuario):
    print("→ Extrato ←")
    if not usuario["extrato"]:
        print("Nenhuma movimentação feita.")
    else:
        for operacao, valor, saldo in usuario["extrato"]:
            print(f"{operacao}: R$ {valor:.2f} | Saldo após: R$ {saldo:.2f}")
        print("Saldo final: R$ {:.2f}".format(usuario["saldo"]))


def menu():
    usuario = cadastro()
    
    while True:
        print("→ Menu ←")
        print("1 - Consultar saldo")
        print("2 - Depositar valor")
        print("3 - Sacar valor")
        print("4 - Sair")
        print("5 - Extrato")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            consultar_saldo(usuario)
        elif opcao == "2":
            depositar(usuario)
        elif opcao == "3":
            sacar(usuario)
        elif opcao == "4":
            print("Encerrado!")
            break
        elif opcao == "5":
            exibir_extrato(usuario)
        else:
            print("Opção inválida! Tente novamente!")

menu()
