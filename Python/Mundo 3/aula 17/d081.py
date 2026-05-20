continuar = 'S'
lista = []
print('-'*30)
while continuar == 'S':
    numeros = int(input('Digite um valor: '))
    lista.append(numeros)
    print(lista)
    resposta = str(input('Deseja continuar [S/N]: ')).upper()
    if resposta in 'N':
        print('     PROGRAMA FINALIZADO!     ')
        break
print('-'*30)
print(f'Lista final: {lista}')
print(f'Tamanho da lista: {len(lista)}.')
lista.sort(reverse=True)
print(f'Lista da forma decrescente: {lista}')
if 5 in lista:
    print('O valor 5 está na lista.')
else:
    print('O número 5 não foi encontrado na lista.')
