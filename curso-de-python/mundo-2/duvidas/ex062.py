valorInicial = int(input('Digite o valor inicial: '))
razao = int(input('Digite o valor da razão: '))
decimo = valorInicial + (10 - 1) * razao
quatidade = 0
count = 0
while valorInicial <= decimo:
    count += 1
    if count == 1:
        print(f'{valorInicial} -> ', end='')
    else:
        valorInicial += razao
        print(valorInicial, '-> ', end='')

quatidade = int(input('\nDigite quantos termos deseja ver? '))

while quatidade != 0:
    while valorInicial <= quatidade: 
        count += 1
        if count == 1:
            print(valorInicial, '-> ', end='')
        else:
            valorInicial += razao
            print(valorInicial, '-> ', end='')
print('Programa encerrado.')