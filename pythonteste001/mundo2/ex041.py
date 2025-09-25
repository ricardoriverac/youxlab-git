from datetime import date

atual=date.today().year
nascimento=int(input('ano de nascimento: '))
idade=atual-nascimento
print('atleta tem {} anos.'.format(idade))
if idade<=9:
    print('Classificação: MIRIM')
elif idade<=14:
    print('Classificação: INFANTIL')
elif idade<=19:
    print('Classificação: JUNIOR')
elif idade<=25:
    print('Classificação: SÊNIOR')
elif idade>25:
    print('Classificação: MASTER')
