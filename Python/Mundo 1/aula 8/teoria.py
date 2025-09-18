# Curso Python #08 - Utilizando Módulos
# import - inclui algo
# EXEMPLO
# bebida = suco , refrigerante , água , milkshake , café
# import bebida
# (chama todas as bebidas generalizada)
# doces = pudim , bolo , torta , brigadeiro , bala , pirulito
# from doce import
# (chama um doce em especifico)

# biblioteca matematica
# math
# ceil (arredonda pra cima)
# floor (arredonda pra baixo)
# trunc (elimina da virgula pra frente)
# pow (potencia)
# sqrt (calcula a raiz quadrada)
# factorial (é uma operação matemática que consiste em multiplicar um número natural por todos os seus antecessores inteiros positivos até 1. Por exemplo, o fatorial de 5, escrito como 5!, é igual a 5 × 4 × 3 × 2 × 1, que resulta em 120.) 

# JUNÇÃO
# import math
# from math import sqrt

# TESTE
# from math import sqrt, floor
# num = int(input('Digite um número: '))
# raiz = sqrt (num)
# print('A raiz de {} é igual a {:.2f}'.format(num, floor(raiz)))

# CHUTA VALORES
import random
num = random.randint(1, 16)
print(num)
