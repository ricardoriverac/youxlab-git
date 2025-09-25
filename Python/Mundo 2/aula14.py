# Curso Python #014 - Estrutura de repetição while
# @ = maçã do exemplo
# % = moeda do exemplo
# enquanto não @ >>>>>>>>>>>> while not @:
# se (objeto)    >>>>>>>>>>>> if ():
# senão se (objeto) >>>>>>>>> if ():
#  se % >>>>>>>>>>>>>>>>>>>>> if  %:

# PRÁTICA
# 1
# for c in range(1, 10):
#     print('c')
# print('FIM')

# 2
# c = 1
# while c < 10:
#     print(c)
#     c = c + 1
# print('FIM!')

# 3
# for c in range(1, 3):
#     n = int(input('Digite um valor: '))
# print('FIM')

# 4
# n = 1
# while n != 0: # enquanto n diferente de 0 
#     n = int(input('Digite um valor: '))
# print('FIM')

# 5
# r = 'S'
# while r == 'S':
#     n = int(input('Digite um valor: '))
#     r = str(input('Deseja continuar? [S/N] ')).upper()
# print('FIM!')

# 6 ---- PARES E IMPARES
n = 1
par = impar = 0
while n != 0: # enquanto o numero for diferente de 0 
    n = int(input('Digite um valor: ')) # acontece isso
    if n % 2 == 0:
        par += 1
    else:
        impar += 1 
print(f'Você digitou {par} números pares e {impar} números impares')
#
#
#
#
#
#