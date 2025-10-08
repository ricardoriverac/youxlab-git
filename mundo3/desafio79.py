lista = []
opção = ''

while True:
    num = int(input('Digite um valor: '))
    if num not in lista:
        lista.append(num)
        print('Valor adicionado com sucesso...')
    elif num in lista:
        print('Valor duplicado! Não vou adicionar...')
    else:
        print('Invalido. Tente novamente, ', end='')

    while True:
        opção = str(input('Quer continuar? [S/N] ').strip().upper())
        if opção == 'S' or opção == 'N':
            break
        else:
            print('Digite S ou N', end='. ')
    if opção == 'N':
         break
print(f'Você digitou os valores {lista.sort()}')

