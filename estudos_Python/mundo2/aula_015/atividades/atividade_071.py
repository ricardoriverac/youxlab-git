'''
Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao 
usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas 
cédulas de cada valor serão entregues.
OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
'''

#Resposta

quantidade = 0
valor = int(input('quanto você quer sacar? '))
while True: 
    if valor >= 50 :
        valor = valor - 50 
        quantidade = quantidade + 1
    if valor < 50:
        break
while True:
    if valor >= 20 :
        valor = valor - 20 
        quantidade = quantidade + 1
    if valor < 20:
        break
while True:
    if valor >= 10:
        valor = valor - 10 
        quantidade = quantidade + 1
    if valor < 10:
        break
while True:
    if valor >= 1:
        valor = valor - 1
        quantidade += 1
    if valor < 1:
        break
print ('você ter q sacar {} notas' .format (quantidade))
