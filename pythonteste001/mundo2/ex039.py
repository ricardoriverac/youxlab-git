from datetime import date

atual=date.today().year
nascimento=int(input('Ano de nascimento: '))
idade=atual-nascimento
print('quem nasceu em {} tem {} anos em {}'.format(nascimento,idade,atual))
if idade == 18:
    print('você tem que se alistar imediatamente!')
elif idade<18:
    saldo=18-idade
    print('ainda faltam {} anos para o seu alistamento'.format(saldo))
    ano=atual+saldo
    print('seu alistamento será em {}'.format(ano))
elif idade>18:
    saldo=idade-18
    print('você já deveria ter se alistado há {} anos'.format(saldo))
    ano=atual-saldo
    print('seu alistamento foi em {}'.format(ano))