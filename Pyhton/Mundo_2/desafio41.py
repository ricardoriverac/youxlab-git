from datetime import date
ano = int(input('Digite seu ano de nascimento: '))
idade = 2025 - ano
if idade <= 9:
    print('Categoria: Mirim')
elif idade <= 14:
    print('Categoria: Infantil')
elif idade <= 19:
    print('Categoria: Junior')
elif idade <= 20:
    print('Categoria: Sênior')
else:
    print('Categoria: Master')