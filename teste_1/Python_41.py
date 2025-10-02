from datetime import date
anoatual = date.today().year
anodenascimento = int(input('Ano de nascimento:'))
idade = anoatual - anodenascimento
atleta = print('O atleta tem {}anos.'.format(idade))
if idade <= 9:
    print('Classificação:MIRIM')
elif idade <= 14:
    print('Classificação:INFANTIL')
elif idade <= 19:
    print('Classificação:JUNIOR')
elif idade <= 25: 
    print('Classificação:SENIOR')
else: 
    print('Classificação:MASTER')