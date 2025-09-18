print('CONFEDERAÇÃO NACIONAL DE NATAÇÃO')
ano_nascimento = int(input('Digite seu ano de nascimento: '))
idade = 2025 - ano_nascimento
if idade <= 9:
    print('Sua categoria é: MIRIM')
elif 10 >= idade <= 14:
    print('Sua categoria é: INFANTIL')
elif 15 >= idade <= 19:
    print('Sua categoria é: JUNIOR')
elif idade == 20:
    print('Sua categoria é: SÊNIOR')
elif idade > 20:
    print('Sua categoria é: MASTER')
