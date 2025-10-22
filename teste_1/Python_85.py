lista = [[], []]
for c in range(1,8):
    valor = int(input(f'Digite o {c}° valor:'))

    if valor % 2 == 0:
       lista[0].append(valor)
    else:
       lista[1].append(valor)
print('-=' * 30)
print(f'Todos os valores digitados:{sorted(lista[0] + lista[1])}')
print(f'Os números pares digitados foram: {sorted(lista[0])}')
print(f'Entre os números digitados esses são ímpares: {sorted(lista[1])}')
        

