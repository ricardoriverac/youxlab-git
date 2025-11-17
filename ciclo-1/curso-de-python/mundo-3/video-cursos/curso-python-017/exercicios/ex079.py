numeros = []
continuar = ''

while True:
    numeroLista = int(input('Digite um número: '))

    if numeroLista not in numeros:
        print('\033[32mNúmero adicionado!\033[m')
        numeros.append(numeroLista)

    else:
        print('\033[31mEsse número já foi adicionado a lista!\033[m')


    continuar = str(input('Deseja continuar? [S/N] ')).upper()
    if continuar == 'N':
        print('-' * 30)
        print('Programa Finalizado.')
        break

    if continuar != 'S':
        print('Resposta Inválida.')
        break

print('-' * 30)
numeros.sort()
print(f'Os números que você digitou são: \033[33m{numeros}\033[m.')