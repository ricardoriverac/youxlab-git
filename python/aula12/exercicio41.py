from datetime import date
anoNasc = int(input('Digite o ano de seu nascimento: '))
anoAtual = date.today().year
idade = anoAtual - anoNasc
if idade <= 9:
    print('mirim')
elif 9 < idade <= 14:
    print('infantil')
elif 14 < idade <= 19:
    print('junior')
elif 19 < idade <= 25:
    print('sênior')
else:
    print('master')