nome = input('Qual o nome do titular da conta: ')
limite = float(input('Limite de saque: R$ '))
saldo = float(input('Saldo inicial: R$ '))
extrato = []

def depositar(saldo, extrato):
    valor = float(input('Valor do depósito: R$ '))
    if valor > 0:
        saldo += valor
        extrato.append(f'Depósito: R$ {valor:.2f}')
        print('Depósito realizado com sucesso!')
    else:
        print('Valor inválido!')
    return saldo, extrato

def sacar(saldo, extrato, limite):
    valor = float(input('Valor do saque: R$ '))
    if valor <= 0:
        print('Valor inválido!')
    elif valor > limite:
        print('Erro: acima do limite de saque.')
    elif valor > saldo:
        print('Erro: saldo insuficiente.')
    else:
        saldo -= valor
        extrato.append(f'- Saque: R$ {valor:.2f}')
        print('Saque realizado com sucesso!')
    return saldo, extrato

def mostrar_extrato(saldo, extrato):
    print('===== EXTRATO =====')
    if not extrato:
        print('Nenhuma movimentação.')
    else:
        for item in extrato:
            print(item)
    print(f'\nSaldo atual: R$ {saldo:.2f}')
    print('=' *20)

def ver_saldo(saldo):
    print(f'Saldo: R$ {saldo:.2f}\n')

menu = '''
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair
[5] Ver saldo
'''

while True:
    opcao = input(menu + 'Escolha uma opção: ')

    if opcao == '1':
        saldo, extrato = depositar(saldo, extrato)
    elif opcao == '2':
        saldo, extrato = sacar(saldo, extrato, limite)
    elif opcao == '3':
        mostrar_extrato(saldo, extrato)
    elif opcao == '4':
        print('Fim!')
        break
    elif opcao == '5':
        ver_saldo(saldo)
    else:
        print('Opção inválida!')