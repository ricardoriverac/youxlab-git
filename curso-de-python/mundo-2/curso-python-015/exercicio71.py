valor = int(input('qual valor deseja ser sacado? '))
if valor > 0: 
    cont = 0
    while valor >= 50:
        cont += 1
        valor -= 50
    print(f'{cont} notas de R$50')
    
    cont = 0
    while valor >= 20:
        cont += 1
        valor -= 20
    print(f'{cont} notas de R$20')

    cont = 0
    while valor >= 10:
        cont += 1
        valor -= 10
    print(f'{cont} notas de R$10')

    cont = 0
    while valor >= 1:
        cont += 1
        valor -= 1
    print(f'{cont} moedas de R$1')
else:
    print('saldo invalido')
