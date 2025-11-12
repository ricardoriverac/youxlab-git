#Crie um programa que simule o funcionamento de um caixa eletrônico.No início, pergunte ao
# usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas
# de cada valor serão entregues.OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.


saque = int(input('Qual o valor que vai ser sacado: '))
resto_divisao = 0
print(f'{saque // 50} notas de R$50')
resto_divisao = saque % 50
print(f'{resto_divisao // 20} notas de R$20')
resto_divisao = resto_divisao % 20
print(f'{resto_divisao // 10} notas de R$10')
resto_divisao = resto_divisao % 10
print(f'{resto_divisao // 1} moedas de 1.')








