print(' > > > > BANCO PY < < < < ')
valorSacado = int(input('Qual o valor que você deseja sacar?: '))
nota50 = 0
nota20 = 0
nota10 = 0
nota1 = 0
while True:
    if valorSacado >= 50:
        valorSacado = valorSacado - 50
        nota50 = nota50 + 1
    else:
        if valorSacado >= 20:
            valorSacado -= valorSacado - 20
            nota20 = nota20 + 1
        else:
            if valorSacado >= 10:
                valorSacado = valorSacado - 10
                nota10 = nota10 + 1
            else:
                if valorSacado >= 1:
                    valorSacado = valorSacado - 1
                    notaa1 = nota1 + 1
    if valorSacado == 0:
        break
print(f'Você irá receber {nota50} notas de R$50,00')
print(f'{nota20} notas de R$20,00')
print(f'{nota10} notas de R$10,00')
print(f'{nota1} notas de  R$1,00.')
print('VOLTE SEMPRE!')