from datetime import date 
anoDnascimento = int(input('Digite seu ano de nascimento: '))
anoatual = date.today().year
idade = anoatual - anoDnascimento
print(f'Quem nasceu em {anoDnascimento} tem {idade} anos em {anoatual}')
if idade > 18:
    print(f'voce deveria ter se alistado ha {idade-18}anos, no ano de {anoDnascimento + 18}')
elif idade == 18:
    print('Ja esta no ano de se alistar')
else :
    print(f'Ainta faltam {18 - idade} anos para voce se alistar,no ano de{anoDnascimento + 18}')
