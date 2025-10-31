'''
Faça um programa que tenha uma lista chamada números e duas funções 
chamadas sorteia() e somaPar(). A primeira função vai sortear 7 números 
e vai colocá-los dentro da lista e a segunda função vai mostrar a soma 
entre todos os valores pares sorteados pela função anterior.
'''

#Resposta

import random
adição_par = []
lst = [6, 8, 1, 13, 3, 15, 10]

def sorteia(aaa):
    random.shuffle(aaa)
    print(f'Os 7 números sorteados: {aaa} ')


sorteia(lst)

def somaPar():
    b = 0
    for c, v in enumerate(lst):
        if v % 2 == 0:
            b += v
    print(f'A soma de todos os números PARES e : {b}')
somaPar()