numeros = []
pares = []
impares = []
continuar = ''

while True:
    numero = int(input('Digite um número: '))
    numeros.append(numero)

    if numero % 2 == 0:
        pares.append(numero)

    if numero % 2 != 0:
        impares.append(numero)

    continuar = str(input('Deseja continuar? [S/N] ')).upper()
    if continuar == 'N':
        print('-' * 25)
        print('\033[31mPrograma Finalizado.\033[m')
        print('-' * 25)
        break

    if continuar != 'S':
        print('-' * 25)
        print('\033[31mResposta Inválida.\033[m')
        print('-' * 25)
        break

print(f'O números que \033[33mvocê\033[m digitou são: \033[33m{numeros}\033[m')
print(f'Os números \033[36mpares\033[m digitados são: \033[33m{pares}\033[m')
print(f'Os números \031[35mimpares\033[m digitados são: \033[33m{impares}\033[m')