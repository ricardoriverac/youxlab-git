saldo = []
nome = str(input("Titular da conta: "))
saldo.append(float(input("saldo: ")))
limite = float(input("Limite de saque: "))

def menu():
    print(" MENU BANCÁRIO ")
    print('''
1 - Consultar saldo
2 - Depositar
3 - Sacar 
4 - Sair
5 - Extrato
''')

extratoFinal = []
def consultar():
    print(f"Saldo da conta: {saldo}")

def depositar():
    deposito = float(input("depositar: "))
    if deposito <= 0:
        print("Valor inválido!")
    else:
        saldo[0] += deposito
        extratoFinal.append(f"Tipo: Deposito: {deposito}, Saldo: R${saldo}")


def sacar():
    saque = float(input("Quanto deseja sacar?: "))
    if saque <= limite:
        saldo[0] -= saque
        extratoFinal.append(f"Tipo: Saque: {saque}, Saldo: R${saldo}")
    else:
        print("Valor a sacar, Maior que limite de saque")


def extrato():
    print("——- EXTRATO ——-")
    if not extratoFinal:
        print("Nenhuma trasação feita!")
    else:
        print(extratoFinal)
        print(f"Saldo final: {saldo}")


while True:
    menu()
    escolha = int(input("escolha uma das opçoes: "))
    if escolha == 1:
        consultar()
    elif escolha == 2:
        depositar()
    elif escolha == 3:
        sacar()
    elif escolha == 4:
        print("Saindo do programa…")
        break
    elif escolha == 5:
        extrato()
    else:
        print("Número inválido!")