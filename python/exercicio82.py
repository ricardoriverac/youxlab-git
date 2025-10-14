listaValores = []
listaImpar = []
listaPar = []
resposta = 'S'
while resposta == 'S':
    valor = int(input(f'digite um valor: '))
    resposta = str(input(f'deseja continuar? [S/N]: ')).upper()
    listaValores.append(valor)
print(f'a lista completa e {listaValores}')
print(f'a lista de pares e {listaImpar}')
print(f'a lista de impares e {listaPar}')

    
