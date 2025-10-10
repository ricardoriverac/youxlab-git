lista = []
while True:
    lista.append(int(input('Digite um número: ')))
    resposta = str(input('Você quer continuar? [S/N] '))
    if resposta in 'Nn':
        break
print(f'Números digitados: {lista} ')
lista.sort(reverse=True)
print(f'Números em ordem decrescente: {lista} ')
if (5) in lista:
    print('O 5 está na lista !')
else: 
    print('O 5 não está na lista !')