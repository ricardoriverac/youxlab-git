primeiroTermo = int(input('digite o termo da PA: '))
razao = int(input('digite a razão da PA: '))
termo = primeiroTermo
contador = 1
while contador <= 10:
    print(f'{termo} ', end = '')
    termo += razao
    contador += 1 
