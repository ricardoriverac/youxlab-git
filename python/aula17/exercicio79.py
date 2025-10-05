lista = []
count = 0
while True:
    valor = int(input('Digite um valor: '))
    count += 1
    answer = ' '
    if valor not in lista:
        lista.append(valor)
    else:
        print('O valor já está presente. Não iremos adicioná-lo.')
    while answer not in 'SN':
        answer = str(input('Você quer continuar? [S/N] ')).strip().upper()[0]
    if answer in 'N':
        break


lista.sort()
print(lista)