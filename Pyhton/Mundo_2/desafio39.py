from datetime import date
ano = int(input('Digite seu ano de nascimento: '))
idade = 2025 - ano
if idade == 18:
    print('Você já pode se alistar!')
elif idade > 18:
    print('Já passou o tempo para se alistar!')
else:
    print(f'Você tem {idade} anos de idade e ainda vai se alistar!')