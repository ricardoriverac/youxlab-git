leituraPessoa = []
cadastroPessoa = []
quantidadePessoa = 0
maisPesada = maisLeve = 0
continuar = 'S'

while continuar == 'S':
    leituraPessoa.append(str(input('Digite seu nome: ')))
    leituraPessoa.append(float(input('Digite seu peso: ')))

    if len(cadastroPessoa) == 0:
        maisPesada = leituraPessoa[1]
        maisLeve = leituraPessoa[1]
    else:
        if leituraPessoa[1] > maisPesada:
            maisPesada = leituraPessoa[1]
        if leituraPessoa[1] < maisLeve:
            maisLeve = leituraPessoa [1]

    cadastroPessoa.append(leituraPessoa[:])
    leituraPessoa.clear()
    quantidadePessoa += 1

    continuar = str(input('Deseja continuar? [S/N] ')).upper()
    if continuar == 'N':
        break

print('-' * 25)
print(f'Foram cadastrados no total \033[33m{quantidadePessoa}\033[m pessoas.')

print(f'O maior peso registrado foi o peso \033[33m{maisPesada:.0f}\033[m. As pessoas com esse peso são: ',end='')
for p in cadastroPessoa:
    if p[1] == maisPesada:
        print('\033[33m', p[0], '\033[m', end='')

print()

print(f'O menor peso registrado foi o peso \033[33m{maisLeve:.0f}\033[m. As pessoas com esse peso são: ',end='')
for p in cadastroPessoa:
    if p[1] == maisLeve:
        print('\033[33m', p[0], '\033[m', end='')
print()