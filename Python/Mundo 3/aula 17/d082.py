print('-'*35)
lista = []
listaPar= []
listaImpar = []
continuar = 'S'
while continuar == 'S':
    valores = int(input('Digite um número: '))
    lista.append(valores)
    print(lista)
    resposta = str(input('Deseja continuar? [S/N]: ')).upper()
    if resposta in 'N':
        break
for posicao, v in enumerate(lista):
    if v % 2 == 0:
        listaPar.append(v)
    elif v % 2 == 1:
        listaImpar.append(v)
print('-'*35)
print('           RESULTADO            ')
print('-'*35)
print('     LISTA NUMÉRICA      ')
print(f'Lista dos números escolhidos:\n{lista}.')
print('-'*35)
print('     LISTA NUMÉRICA (PAR)     ')
print(f'Lista do números PARES: {listaPar}.')
print('-'*35)
print('     LISTA NUMÉRICA (ÍMPAR)      ')
print(f'Lista dos números ÍMPARES: {listaImpar}')
print('-'*35)
print('     PROGRAMA ENCERRADO!     ')
print('-'*35)