'''
A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta a mostra sua categoria, da acordo com a idade:
Até 9 anos: MIRIM
Até 14 anos: INFANTIL
Até 19 anos: JUNIOR
Até 25 anos: SENIOR
Acima: MASTER
'''

#Resposta
from datetime import date 

atual = date.today().year
data_de_nascimento = int(input('Digite o seu ano de nascimento: '))
ta = (atual - data_de_nascimento)
print(ta)
if ta <= 9 :
    print('Você e um atleta MIRIM!!')

elif ta  >= 10 and ta <=14:
    print('Você e um atleta INFANTIL!!')

elif ta >= 15 and ta <= 19:
    print('Você e um atleta JUNIOR!!')

elif ta >= 20 and ta <= 25:
    print('Você e um atleta SENIOR!!')

elif ta >= 25 :
    print('Você e um atleta MASTER!!')
print(ta)