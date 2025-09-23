from datetime import date 
atual = date.today().year
nascimento = int(input('Ano de nascimento:'))
idade = atual - nascimento
print('Quem nasceu em {} tem {} anos em {}'.format(nascimento, idade, atual))
if idade == 18:
    print('Voce tem que se alistar!')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda falta {} anos para o alistamento'.format(saldo))
elif idade > 18:
    saldo = idade - 18
    print('Voce ja deveria ter sido alistado há {} anos'.format(saldo))"