from datetime import date
ano_nascimento = int(input('Seu ano de nascimento: '))
idade = 2025 - ano_nascimento
if idade == 18:
    print(f'Você tem {idade} e já pode se alistar!')
elif idade > 18:
    print(f'Você tem {idade} e já passou o tempo de alisar!')
else:
    print(f'Você tem {idade} e ainda vai se alistar!')
