from datetime import date
atual = date.today().year
nascimento = int(input('Digite o ano que você nasceu: '))
idade = atual - nascimento
print(f'Quem nasceu em {nascimento} tem {idade} anos em {atual}')
if idade == 18:
     print('Voce tem que se alistar ')
elif idade < 18:
     print('Voce ainda nao tem 18 anos ')   
elif idade > 18:
     print ('Voce ja deveria ter se alistado')