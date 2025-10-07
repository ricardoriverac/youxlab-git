dic = {}
resp = ' '
count = 0
while True:
    dic['pessoa'] = str(input('Nome: '))
    dic['sexo'] = str(input('Sexo: '))
    if dic['sexo'] not in 'MmFfNBnbGFgf':
        print('Não há opções no momento, sinto muito :(')
        break