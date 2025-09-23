primeiroTermo = int(input('Digite o primeiro termo: '))
razao = int(input('De quanto em quanto está indo: '))
termoAtual = primeiroTermo
contar = 1
while contar <= 10:
    print(f'{termoAtual} -> ', end='')
    termoAtual += razao
    contar += 1
print('FIM')