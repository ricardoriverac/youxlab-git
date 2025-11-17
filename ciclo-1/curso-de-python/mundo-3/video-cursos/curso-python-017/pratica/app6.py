# Para criar listas pode-se usar list() ou []
valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for chaves, valor in enumerate(valores): # o 'chaves' e 'enumerate' printa qual a posição do elemento
    print(f'Na posição {chaves} encontrei o valor {valor}')
print('Cheguei ao final da lista.')