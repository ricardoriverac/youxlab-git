'''
 Faça um programa que tenha uma função chamada escreva(),
que receba um texto qualquer como parâmetro e mostre uma mensagem 
com tamanho adaptável.

Ex: 
escreva('Olá, Mundo!')
Saída:
~~~~~~~~~
 Olá, Mundo!
~~~~~~~~~
'''

def escreva(msg):
    tamanho = len(msg)
    print('~' * (tamanho + 4))
    print(f'{msg}')
    print('~' * (tamanho + 4))


escreva('Ana Laura')
escreva('Python')