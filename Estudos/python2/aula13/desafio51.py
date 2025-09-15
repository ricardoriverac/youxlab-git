#10 TERMOS DE UMA PROGRESSÃO ARITMÉTICA
primeiroTermo= int(input('Qual o valor do primeiro termo? '))
razão = int(input('Qual o valor da razão? '))
for c in range (primeiroTermo, 11, razão):
    print(f'{c}', end= '>') 