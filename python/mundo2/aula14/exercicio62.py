primeiroTermo = int(input('digite o termo da PA: '))
razao = int(input('digite a razão da PA: '))
total = 0
termo = primeiroTermo
contador = 1
mais = 10
while mais != 0:
    total += mais
    while contador <= total:
        print(f'{termo} ', end = '')
        termo += razao
        contador += 1 
    mais = int(input('\nquantos termos a mais você quer ver? '))
print(f'PA terminada após {total} termos')