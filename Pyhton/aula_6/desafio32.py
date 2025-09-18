ano = int(input('Digite um ano qualquer: '))
if ano % 4 == 0:
    print('O ano {} é bissexto!!'.format(ano))
else:
    print('O ano {} nâo é bissexto!!'.format(ano))