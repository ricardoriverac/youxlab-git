# Curso Python #16 - Tuplas

# TUPLA - Variavel que guarda mais de um valor

# LISTA - 0.Hamburguer, 1.pudim, 2.água e 3.salada
# print(lanche[2])
# print(lanche[0:2]) --> escolhe o lanche 0 e o lanche 1
# print(lanche[1:]) --> escolhe o elemento enumerado e vai até o final
# print(lanche[-1]) --> conta o ultimo elemento como o pudim 
# len --> comprimento
# len(lanche) "ou seja 4 elementos no meu exemplo"--> diz quantos elementos tem no lanche
# c --> para cada comida em lanche
#   print(comida)
# TUPLAS SÃO IMUTAVEIS
 
# PRÁTICA
# pode começar uma variavel de três formas 
# lanche = () [] {}
# (TUPLA)
# [LISTA]
# {DICIONÁRIO}
# lanche = ('Hamburguer', 'pudim', 'água', 'salada')
# print(lanche)

# lanche = ('Hamburguer', 'pudim', 'água', 'salada')
# print(lanche[1])

# lanche = ('Hamburguer', 'pudim', 'água', 'salada')
# print(lanche[3])

# lanche = ('Hamburguer', 'pudim', 'água', 'salada')
# print(lanche[1:3])

# lanche = ('Hamburguer', 'pudim', 'água', 'salada')
# print(lanche[:3])

# lanche = ('Hamburguer', 'pudim', 'água', 'salada')
# print(lanche[1:])

# lanche = ('Hamburguer', 'pudim', 'água', 'salada')
# print(lanche[-1])

# lanche = ('Hamburguer', 'pudim', 'água', 'salada')
# print(lanche[-2])

# lanche = ('Hamburguer', 'pudim', 'água', 'salada')
# print(lanche[-2:])

# lanche = ('Hamburguer', 'pudim', 'água', 'salada')
# for comida in lanche:
#     print(f'Eu vou comer {comida}')
# print('Comi pra caramba!!!')

# for cont in range(0, len(lanche)):
#     print(f'Eu vou comer {lanche[cont]} na posição {cont}')
# print('Comi pra caramba!!')

# lanche = ('Hamburguer', 'pudim', 'água', 'salada')
# print(len(comida))
# print('Comi pra caramba!!!')

# for pos,cont in enumerate(lanche):
#     print(f'Eu vou comer {comida} na posição {pos}')
# print('Comi pra caramba!!')

# for pos,cont in enumerate(lanche):
#     print(f'Eu vou comer {comida} na posição {pos}')
# print('Comi pra caramba!!')

# lanche = ('Hamburguer', 'pudim', 'água', 'salada')
# print(sorted(lanche)) # sorted = colocar em ordem exemplo (ordem alfabetica)
# print(lanche)

a = (2, 5, 4)
b = (5, 8, 1, 2)
# c = a + b
# print(a)
# print(b)
# print(c) # junta os numeros
# invertendo
c = b + a
print(c)
print(len(c)) # lê o comprimento
# print(c.count(5)) # conta quantas vezes cada elemento aparece
print(c.index(2, 4)) # em que posição está o elemento

