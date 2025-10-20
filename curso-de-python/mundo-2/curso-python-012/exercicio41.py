from datetime import date
atual = date.today().year
nascimento = int(input('quando nasceu'))
idade = atual - nascimento
print('atleta tem {} anos'.format(idade))
if idade <= 9:
    print('classificacao: MIRIM')
elif idade > 9 and idade <=14:
    print('classificacao: INFANTIL') 
elif idade <= 19:
    print('classificacao: JUNIOR')
elif idade <= 25:
    print('classificacao: SENIOR')
else:
    print('classificacao: MASTER')