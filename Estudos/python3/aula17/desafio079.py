continuacao= 'dsadasd'
lista= list()
while continuacao not in 'N':
    numero= (int(input('Digite um valor: ')))
    if numero not in lista:
        print('Valor adicionado con sucesso...')
        lista.append(numero)
    elif numero in lista:
        print('Valor duplicado! Por favor digite um valor que não tenha sido inserido! ')
    continuacao= str(input('Você deseja continuar? [S/N]').upper())
listaOrdenada=sorted(lista)
print(f'Você digitou os valores {listaOrdenada}')