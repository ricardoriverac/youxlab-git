print('FORMULÁRIO DA CONFIDERAÇÃO NACIONAL DE NATAÇÃO')
print('Seja bem-vindo adicione os seus dados abaixo se deseja participar')
ano = int(input('Digite o ano do seu nascimento: '))
idade = 2025 - ano
if idade <= 9:
    print(f'Você tem {idade} anos, então a sua categoria é MIRIM!')
elif idade <= 14:
    print(f'Você tem {idade} anos, então a sua categoria é INFANTIL!')
elif idade <= 19:
    print(f'Você tem {idade} anos, então a sua categoria é JUNIOR!')
elif idade <= 25:
    print(f'Você tem {idade} anos, então a sua categoria é SÊNIOR!')
elif idade > 25:
    print(f'Você tem {idade} anos, então a sua categoria é MASTER!')
    