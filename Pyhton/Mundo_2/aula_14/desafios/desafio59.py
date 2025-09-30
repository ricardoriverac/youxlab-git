numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite outro número: '))
escolha = 0
while escolha != 5:
    print('''[ 1 ] Adição
    [ 2 ] Multiplicação
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] sair do programa)''')
    escolha = int(input('Escolha uma das opções: '))
    if escolha == 1:
        soma = numero1 + numero2
        print(f'{numero1} + {numero2} = {soma}')
    elif escolha == 2:
        multiplicando = numero1 * numero2
        print(f'{numero1} x {numero2} = {multiplicando}')
    if escolha == 3:
        maior = numero1 > numero2
        print(f'O primeiro número ( {numero1} ) é maior que o segundo número ( {numero2} )')
    elif escolha == 3:
           maior = numero2 > numero1
           print(f'O segundo número ( {numero2} ) é maior que o primeiro número ( {numero1} )')
    elif escolha == 4:
        print('Digite os novos números: ')
        novonum = int(input('Digite o primeiro número: '))
        novonum1 = int(input('Digite o segundo número:'))
    elif escolha == 5:
        print('... Acabou !...')
    else:
        print('Erro! Tente novamente!')
    print('Fim do programa.')