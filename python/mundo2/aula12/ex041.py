# A Confederação Nacional de Natação precisa de um programa que leia o ano
# de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#Até 9 anos: MIRIM
#Até 14 anos: INFANTIL
#Até 19 anos: JÚNIOR
#Até 25 anos: SÊNIOR
#Acima de 25 anos: MASTER

import datetime
ano_atual = datetime.date.today( ).year
ano = int(input(f'Digite a sua data de nascimento: '))
idd = ano_atual - ano
if idd <= 9:
    print(f'De acordo com sua idade, sua categoria é MIRIM.')
elif idd <= 14:
    print(f'De acordo com sua idade, sua categoria é INFANTIL.')
elif idd <= 19:
    print(f'De acordo com sua idade, sua categoria é JUNIOR')
elif idd <= 25:
    print(f'De acordo com sua idade, sua categoria é SÊNIOR')
else:
    print(f'De acordo com sua idade, sua categoria é MASTER.')


