valorInicial = int(input('Digite o primeiro número do termo: '))
razao = int(input('Digite a razão do termo: '))
decimo = valorInicial + (10 - 1) * razao
count = 0
while valorInicial <= decimo:
    valorInicial += razao
    count += razao
    print(valorInicial, '-> ', end='')