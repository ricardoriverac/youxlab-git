lista = []
dado = []
maior = menor = 0
while True:
    dado.append(str(input('Nome: ')).title().strip())
    dado.append(float(input('Peso: ')))
    if len(lista) == 0:
        menor = maior = dado[1]
    else:
        if dado[1] > maior:
            maior = dado[1]
        if dado[1] < menor:
            menor = dado[1]
    lista.append(dado[:])
    dado.clear()
    r = str(input('Deseja continuar? [S/N]')).upper()
    if r in 'N':
        break
print(f'Ao todo vc cadastrou {len(lista)} pessoas.')
print(f'Maior peso foi {maior} Kgs. Peso de ', end='')
for p in lista:
    if p[1] == maior:
        print(p[0], end=' ')
print()
print(f'Menor peso foi {menor} Kgs. Peso de ', end='')
for p in lista:
    if p[1] == menor:
        print(p[0], end=' ')
print('FIM!')