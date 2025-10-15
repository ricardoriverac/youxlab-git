lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    answer = ' '
    while answer not in 'SN':
        answer = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if answer in 'N':
            break
lista.sort(reverse=True)
print(f'A lista possui {len(lista)} números.')
print(f'A lista, em ordem decrescente, é: {lista}')
if 5 in lista:
    print('O número 5 está presente')
else:
    print('O número cinco não está presente')