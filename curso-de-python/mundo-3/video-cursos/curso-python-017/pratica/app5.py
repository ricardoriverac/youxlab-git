# Para criar listas pode-se usar list() ou []
valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for valor in valores: # Para cada elementos da lista ele irá printar o valor com "..." na frente.
    print(f'{valor}...', end=' ')