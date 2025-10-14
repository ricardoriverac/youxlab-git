from datetime import date
atual = date.today().year
nasc = int(input('ano de nascimento: '))
idade = atual - nasc
print('quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
if idade == 18:
    saldo = 18 - idade
    print('ainda faltam {} anos para o alistamento'.format(saldo))
    print('voce tem que se alistar URGENTEMENTE')
elif idade < 18:
    saldo = 18 -idade
    print('ainda faltam {} anos para o alistamento'.format(saldo))
    ano = atual + saldo
    print('seu alistamento sera em {}'.format(ano))
elif idade > 18:
    print('voce ja deveria ter se alistado ha {} anos'.format(saldo))
    ano = atual - saldo
    print('seu alistamento foi em {}'.format(ano))