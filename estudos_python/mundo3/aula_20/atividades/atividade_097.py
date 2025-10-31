'''
Faça um programa que tenha uma função chamada escreva(), que receba um 
texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.

Ex: 
escreva('Olá, Mundo!')
Saída:
~~~~~~~~~
 Olá, Mundo!
~~~~~~~~~
'''

#Responda

def msg(msg):
    tem = len(msg)
    print('-'*tem)
    print(msg)
    print('-'*tem)

msg(str(input('Digite uma palavra: ')))