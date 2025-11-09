ano1= float(input('Que ano quer analisar? Coloque 0 para analisar o ano atual:'))
if ano1 % 4 == 0 and ano1 % 100 != 0:
    print('O ano {} é biessexto'.format(ano1))
else:
    print('O ano {} não é bissesto'.format(ano1))
