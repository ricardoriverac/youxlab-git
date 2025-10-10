lista = []
for c in range(0, 5):
    numero = int(input('digite um número: '))
    if c ==0:
        lista.append(numero)
    elif numero > lista[-1]:
        lista.append (numero)
    else:
        quantidade = 0
        while quantidade < len(lista):
            if numero <= lista[quantidade]:
                lista.insert(quantidade, numero)
                break 
            quantidade = quantidade + 1
print(f'Lista ordenada: {lista}')