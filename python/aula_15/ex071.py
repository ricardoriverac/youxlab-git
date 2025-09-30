'''
Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) 
e o programa vai informar quantas cédulas de cada valor serão entregues.
OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
'''
print('=' * 20)
print('BANCO PY')
print('=' * 20)
saque = int(input('Digite o valor que deseja sacar: R$ '))
cedula50 = cedula20 = cedula10 = cedula1 = 0
while True:
    if saque >= 50:
        saque -= 50
        cedula50 += 1
    else:
        if saque >= 20:
            saque -= 20
            cedula20 += 1
        else:
            if saque >= 10:
                saque -= 10
                cedula10 += 1
            else:
                if saque >= 1:
                    saque -= 1
                    cedula1 += 1
    if saque == 0:
        break
print(f'Você receberá {cedula50} cédulas de R$50,00, {cedula20} cédulas R$20,00, {cedula10} cédulas de R$10,00 e {cedula1} cédulas de  R$1,00.')
print('=' * 20)
print('VOLTE SEMPRE!')
print('=' * 20)