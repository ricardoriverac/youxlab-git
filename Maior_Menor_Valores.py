resp = 'S'
soma = quant = média = 0 
while resp in 'Ss':
    num = int(input('Digite um número:'))
    soma += num
    quant += 1
    resp = str(input('Quer contimuar? [S/N]')).upper(.strip()[0]