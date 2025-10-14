numeros = []
count = 0
continuar = ''

while True:
    numeros.append(int(input('Digite um número: ')))
    count += 1

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

if count == 1:
    print('Foi digitado apenas \033[33m1\033[m número.')
if count > 1:
    print(f'Foram digitados \033[33m{count}\033[m números')

numeros.sort(reverse=True)
print(f'Os números da lista em forma decrescente são: \033[33m{numeros}\033[m')

if 5 in numeros:
    print(f'O número 5 \033[32mfoi\033[m digitado, e \033[32mestá\033[m na lista.')
else:
    print(f'O número 5 \033[31mnão\033[m foi digitado e \033[31mnão\033[m esta na lista')