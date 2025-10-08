lista = list()
for valores in range(0,5):
    lista.append(int(input('Adicione um valor numérico: ')))
print(f'Os valores numéricos foram: {lista}')
print(f'O maior valor numérico é o {max(lista)} na posição ', end='')
for int, v in enumerate(lista):
    if max(lista) == v:
        print(f'{int}', end='ª ')
print()
print(f'O menor valor numérico é o {min(lista)} na posição ', end='')
for int, v in enumerate(lista):
    if min(lista) == v:
        print(f'{int}', end='ª ')