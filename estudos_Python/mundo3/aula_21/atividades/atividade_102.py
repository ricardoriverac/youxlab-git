'''
Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número 
a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela 
o processo de cálculo do fatorial.
'''

#Resposta


print('FATORIAL: ')
def fatorial(numero_calcular, show=False):
    '''
    Função: Ele serve para ver o fatorial de
    um serto número dentro dos patenteses

    Como usar: O primeiro eslot e para colocar 
    o número que quizer fatoriar

    show: Ele mostra se e para aparecer 
    o caminho do fatorial
    '''
    v = 1
    for c in range(numero_calcular, 0, -1): 
        v *= c
        if show == True:
            print(f' * {c}', end='')
    print(f' = {v}')

fatorial(8, True)
