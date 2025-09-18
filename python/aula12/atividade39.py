from datetime import date
anoNasc = int(input('Digite o ano de seu nascimento: '))
anoAtual = date.today().year
idade = anoAtual - anoNasc
alist = anoNasc + 18
if idade > 18:
    resto = idade - 18
    print(f'Quem nasceu em {anoNasc} tem {idade} anos\nVocê já deveria ter se alistado há {resto} anos\nSeu alistamento foi em {alist}')
elif idade < 18:
    resto = 18 - idade
    print(f'Quem nasceu em {anoNasc} tem {idade} anos\nVocê deve se alistar em {resto} anos\nSeu alistamento será {alist}')
else:
    print(f'Quem nasceu em {anoNasc} tem {idade} anos\nVocê já deveria ter se alistado esse ano\nSeu alistamento é AGORA em {alist}')