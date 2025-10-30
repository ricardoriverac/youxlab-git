print('=' * 30)
print('{:^30}'.format('BANCO PYTHON'))
print('=' * 30)

valor = int(input('Que valor você quer sacar? R$'))
total = valor
ced = 50
total_ced = 0

while True:
    if total >= ced:
        total -= ced
        total_ced += 1
    else:
        if total_ced > 0:
            print(f'Total de {total_ced} cédula(s) de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        total_ced = 0
        if total == 0:
            break

print('=' * 30)
print('Volte sempre ao BANCO PYTHON! Tenha um bom dia!')
