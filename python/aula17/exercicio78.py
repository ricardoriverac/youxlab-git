lista = []
major = minor = 0
for c in range(0, 5):
    lista.append(int(input(f'Digite o valor que você deseja colocar na posição {c}: ')))
    if c == 0:
        major = minor = lista[c]
    #vai ler o primeiro valor como o menor e o maior simultaneamente
    else:
        if lista[c] > major:
            major = lista[c]
        if lista[c] < minor:
            minor = lista[c]
print(lista)
for i, v in enumerate(lista):
    if v == major:
        print(f'Maior: {i} e {major}')
for i, v in enumerate(lista):
    if v == minor:
        print(f'menor: {i} e {v}')