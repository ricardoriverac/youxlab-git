valorInicial = int(input('Digite o valor inicial: '))
razao = int(input('Digite o valor da razão: '))
decimo = valorInicial + (10 - 1) * razao
quantidade = 0
count = 0

while valorInicial <= decimo:
    count += 1
    if count == 1:
        print(f'{valorInicial} -> ', end='')
    else:
        valorInicial += razao
        print(valorInicial, '-> ', end='')

quantidade = int(input('\nDigite quantos termos a mais você deseja ver? '))

for c in range(quantidade):

    valorInicial += razao
    print(valorInicial, '-> ', end='')

print('\033[31m\nPrograma encerrado.')