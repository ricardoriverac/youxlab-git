#   Curso Python #17 - Listas (Parte 1)

#   TUPLAS () - são IMUTAVEIS
#   LISTAS [] - podem ser alteradas

# exemplo:
# lanche = ['hamburguer','suco','pizza','pudim']
# lanche[3] = 'picole' 
# lanche.append('batata frita') # comando para add novos elementos na lista
# lanche.append('pudim')
# lanche.insert(1,'cachorro-quente') # add um item entre os elementos da lista
# lanche.insert(1,'água')
# del lanche[5] # metodos de apagar 
# lanche.pop(4)
# if 'pizza' in lanche:
#     lanche.remove('pizza') # Não deu muito certo
# print(lanche)


# valores = list(range(4,11))
# valores = [8, 2, 5, 4, 9, 3, 0]
# valores.sort()
# valores.sort(reverse = True)
# print(valores)

# valores = [8, 2, 5, 4, 9, 3, 0]
# print(len(valores))


# PRÁTICA
# listaNumeros = [2, 5, 9, 1] 
# listaNumeros[2] = 3 
# listaNumeros.append(7)
# listaNumeros.append(10)
# listaNumeros.sort(reverse = True)
# listaNumeros.insert(6, 0)
# listaNumeros.pop(4)
# print(listaNumeros)
# print(f'Essa lista tem {len(listaNumeros)} elementos.')
# if 4 in listaNumeros: 
#     listaNumeros.remove(4)
# else:
#     print('O elemento 4 não existe.' )

# valores = []
# valores.append(1)
# valores.append(3)
# valores.append(5)
# for v in valores: # c - posição/ v - foi encontrado o valor 
# for c, v in enumerate(valores):
#     print(f'Na posição {c} encontrei o valor {v}...!')# , end = '')
# print('Cheguei ao final da lista')

# valores = list()
# for cont in range(0, 5):
#     valores.append(int(input('Digite um valor inteiro: ')))
# for c, v in enumerate(valores):
#     print(f'Na posição {c} encontrei o valor {v}...!')# , end = '')
# print('Cheguei ao final da lista')

lista = [3, 5, 9, 8]
lista1 = lista [:] # interliguei as duas listas / [:] - copia uma lista na outra 
lista1 [2] = 10
print(f'Lista A: {lista}')
print(f'Lista B: {lista1}')


