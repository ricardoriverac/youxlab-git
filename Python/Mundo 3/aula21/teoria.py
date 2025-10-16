# Curso Python #21 - Funções (Parte 2)
# Nessa aula, vamos continuar nossos estudos de funções em Python, aprendendo mais sobre Interactive Help em Python,
# o uso de docstrings para documentar nossas funções, argumentos opcionais para dar mais dinamismo em funções Python,
#  escopo de variáveis e retorno de resultados. 

#  Interact help(Explica como funciona cada variavel)
# help(print) # - função + variavel do programa

#  Docstrings -> string de documentação
# print(input.__doc__) #

# def contador(i, f, p): # inicio, fim e passo 
#     """
#     -> Faz uma contagem e mostra na tela
#     :param i: inicio   
#     :param f: fim 
#     :param p: passo
#     :return: sem retorno
#     """
#     c=i
#     while c <= f:
#         print(f'{c}',end='..')
#         c+=p
#     print('FIM!')

# help(contador)
# contador(2, 100, 10)

#  Argumentos opcionais
# def somar(a=0, b=0, c=0):
#     """
#      -> Faz uma contagem e mostra na tela
#      :param i: inicio   
#      :param f: fim 
#      :param p: passo
#      :return: sem retorno
#      """
#     s=a+b+c
#     print(f'A soma vale {s}')
# somar(3, 2, 5)
# somar(8, 4)
# somar()

#  Escopo de variaveis
# def teste():
#     x =8
#     print(f'No programa principal, n vale {n}')
#     print(f'No programa principal, x vale {x}')
# Programa principal
# n =2
# print(f'No programa principal, n vale {n}')
# teste()
#
# def teste(b):
#     a=8
#     b+=4 # soma com o de fora
#     c=2
#     print(f'A dentro vale {a}')    
#     print(f'B dentro vale {b}')
#     print(f'C dentro vale {c}')
# a=5
# teste(a)
# print(f'A fora vale {a}')
#
# def funcao():
#     n1=4
#     print(f'N1 dentro vale {n1}')
# n1=2
# funcao()
# print(f'N1 global vale {n1}')
#
# def teste(b):
#     global a # global - por favor não use crie uma variavel 'A' use o a global  
#     a=8
#     b+=4 # soma com o de fora
#     c=2
#     print(f'A dentro vale {a}')
#     print(f'B dentro vale {b}')
#     print(f'C dentro vale {c}')
# # Programa principal
# a=5
# teste(a)
# print(f'A dentro vale {a}')

#  Retorno de resultados
# def somar(a=0, b=0, c=0):
#     s=a+b+c
#     return s
#     # print(f'A soma vale {s}')
# r1=somar(3, 2, 5)
# r2=somar(8, 4)
# r3=somar(1)
# print(f'Meus cálculos deram {r1}, {r2} e {r3}.')
#
# def fatorial(num=1):
#     f = 1
#     for c in range(num, 0, -1):
#         f *= c
#     return f
#
# n = int(input('Digite um número: '))
# print(f'O fatorial de {n} é igual{fatorial(n)}')
#
# f1 = fatorial(5)
# f2 = fatorial(4)
# f3 = fatorial()
# print(f'Os resultados são {f1}, {f2} e {f3}')
def par(n=0):
    if n%2==0:
        return True
    else:
        return False
    
num = int(input('Digite um número: '))
if par(num):
    print('É par!')
else:
    print('Não é par!')

