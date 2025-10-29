from datetime import date
atual = date.today().year
nasc = int(input('Qual e o seu nome de nascimento? '))
idade = atual - nasc
print(f'Quem nasceu em {nasc} tem {idade} anos em {atual}')
