#interact help
#help(int) # funcao
#docstrings
# print(input.__doc__)
#def contador(i,f,p):
#     """
#     """

#     c = i
#     while c <= f:
#         print(f'(c)',end='..')
#         c += p
#         print('fim')
  
# help(contador)
#parametros opcionais
# def somar(a=0, b=0, c=0):
#     s = a + b + c
#     print(f'a soma vale {s}')
# somar(3,2,5)
# somar(8,4)
# somar()
#escopo de variaveis
# def teste():
#     x = 8
#     print(f'na funçao teste, n vale {n}')
# n = 2
# print(f'no programa principal, n vale {n}')
# teste()
#retorno valores
# def somar(a=0, b=0, c=0):
#     s = a + b + c
#     return s
# r1 = somar(3, 2, 5)
# r2 = somar(2, 2)
# r3 = somar(6)

# print(f'os resultados foram [r1, r2, r3]')


#pratica
# def fotorial(num=1):
#     f = 1
#     for c in range(num, 0, -1):
#         f *= c
#     return f

# f1 = fotorial(5)
# f2 = fotorial(4)
# f3 = fotorial()
# print(f'os resultados sao {f1}, {f2} e {f3}')


#return serve pra varias coisas, numeros, fatorial logico, verdadeiro ou falso
# def par(n=0):
#     if n % 2 == 0:
#         return True
#     else: 
#         return False
    
# num = int(input('digite um numero: '))
# if par(num):
#     print('e par!')
# else:
#     print('nao e par!')


