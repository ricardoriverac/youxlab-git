continuação= 'dsad'
lista= list()
listaPares= list()
listaImpares= list()
while continuação not in 'N':
    numero= int(input('Digite um valor: '))
    lista.append(numero)
    continuação= str(input('Deseja continuar? [S/N]').upper())
    if numero % 2 == 0:
        listaPares.append(numero)
    if numero % 2 == 1:
        listaImpares.append(numero)
print(f'A lista completa é {lista}')
print(f'Os números pares presentes na lista são: {listaPares}')
print(f'Os números ímpares são: {listaImpares}')
