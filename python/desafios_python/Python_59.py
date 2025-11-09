primeiroNumero = int(input('Digite um número: '))
segundoNumero = int(input('Digite outro número: '))

while True:
    print('''
[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos números
[ 5 ] Sair do programa''')
    opcao = int(input('Escolha uma opção: '))

    if opcao == 1:
        print('Soma: {}'.format(primeiroNumero + segundoNumero))
    elif opcao == 2:
        print('Multiplicação: {}'.format(primeiroNumero * segundoNumero))
    elif opcao == 3:
        print(f'Maior: {max(primeiroNumero,segundoNumero)}')
    elif opcao == 4:
        a = int(input('Novo primeiro número: '))
        b = int(input('Novo segundo número: '))
    elif opcao == 5:
        print('Saindo...')
        print('Volte sempre :)')
        break
    else:
        print('Opção inválida!')
    print('=-=' * 10)
