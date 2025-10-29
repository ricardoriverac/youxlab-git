from time import sleep
print('===== MENU DE OPERAÇÕES =====')
num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))
opcao = 0
while opcao != 5:
    print('''
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa
    ''')
    opcao = int(input('Escolha uma opção: '))
    if opcao == 1:
        print(f'A soma de {num1} + {num2} é {num1 + num2}.')
    elif opcao == 2:
        print(f'O resultado de {num1} x {num2} é {num1 * num2}.')
    elif opcao == 3:
        if num1 > num2:
            print(f'O maior número é {num1}.')
        elif num2 > num1:
            print(f'O maior número é {num2}.')
        else:
            print('Os dois números são iguais.')
    elif opcao == 4:
        print('Informe os novos números:')
        num1 = int(input('Digite o primeiro valor: '))
        num2 = int(input('Digite o segundo valor: '))
    elif opcao == 5:
        print('Saindo do programa...')
    else:
        print('Opção inválida! Tente novamente.')
    print('-' * 30)
    sleep(1)
