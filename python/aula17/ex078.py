lista = list()
for valores in range(0, 5):
    lista.append(int(input('Adicione um valor: ')))
print(f'Os valores informados foi: {lista}')
print(f'O maior valor foi {max(lista)} na posição ', end='')
for int, v in enumerate(lista):
    if max(lista) == v:
        print(f'{int}', end='ª ')
print()
print(f'O menor valor foi {min(lista)} na posição ', end='')
for int, v in enumerate(lista):
    if min(lista) == v:
        print(f'{int}', end='ª ')