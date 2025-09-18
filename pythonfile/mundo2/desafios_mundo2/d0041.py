from datetime import date
atual = date.today().year
nascimento = int(input('Qual o ano do seu nascimento'))
idade = atual - nascimento
print(f'Voce nasceu em {nascimento} e tem {idade} em {atual}')
if idade <=9:
    print('Você esta na categoria MIRIM')
elif idade <=14:
    print('Você esta na categoria INFANTIL')
elif idade <=19:
    print('Você esta na categoria JUNIOR')
elif idade ==20:
    print('Você esta na categoria SÊNIOR')
else: 
    print('Você esta na categoria MASTER')