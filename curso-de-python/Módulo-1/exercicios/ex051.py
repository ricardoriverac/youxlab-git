valorInicial = int(input('Digite o primeiro número do termo: '))
razao = int(input('Digite a razão do termo: '))
decimo = valorInicial + (10 -1) * razao
for pa in range(0, decimo, razao):
    print('{} '.format(pa), end='- ')