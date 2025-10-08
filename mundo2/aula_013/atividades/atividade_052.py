'''
Faça um programa que leia um número inteiro a diga se ela é OU NÃO um número primo.
'''

#Resposta

digite_o_numero = int(input('Digite um número inteiro: '))
valor = 0

for c in range(1, digite_o_numero +1):
    if digite_o_numero %  c == 0 :
        print('\033[33m', end='')
        valor += 1
    else:
        print('\033[31m', end='')
    print(f'{c}')
print(f'O número {digite_o_numero} foi divisivel {valor} vezes')
if valor == 2:
    print('Esse número e primo!!')
else:
    print('Esse número não e primo!!')
