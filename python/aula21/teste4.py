'''Função com o comando 'global', permite alterar o valor da variável global dentro de uma função
def funcao():
    global n1
    n1 = 4
    print(f'Valor de n1 dentro: {n1}')
n1 = 2
funcao()
print(f'Valor de n1 fora: {n1}')'''
def funcao():
    n1 = 4
    print(f'Valor de n1 dentro: {n1}')
n1 = 2
funcao()
print(f'Valor de n1 fora: {n1}')