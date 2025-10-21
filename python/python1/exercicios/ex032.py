ano = int(input('Digite um ano: '))
if ano % 4 == 0:
    ano % 100 == 0
    ano % 400 == 0
    print('É bissexto')
else:
    print('Nao é bissexto')
