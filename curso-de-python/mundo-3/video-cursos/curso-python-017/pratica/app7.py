valores = []
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: '))) # Está pedidon para o usúario adicionar valores 4 vezes, e será adicionado na lista.

for chaves, valor in enumerate(valores): # o 'chaves' e 'enumerate' printa qual a posição do elemento
    print(f'Na posição {chaves} encontrei o valor {valor}')
print('Cheguei ao final da lista.')