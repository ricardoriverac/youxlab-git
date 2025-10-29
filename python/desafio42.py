from datetime import date
ano_nascimento = int(input('Ano de nascimento do atleta: '))
ano_atual = date.today().year
idade = ano_atual - ano_nascimento
print(f'O atleta tem {idade} anos.')
if idade <= 9:
    print('Categoria: MIRIM')
elif idade <= 14:
    print('Categoria: INFANTIL')
elif idade <= 19:
    print('Categoria: JÚNIOR')
elif idade <= 25:
    print('Categoria: SÊNIOR')
else:
    print('Categoria: MESTRE')
