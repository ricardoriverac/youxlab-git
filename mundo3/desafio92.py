nome = (input('qual seu nome? '))
nascimento = (int(input('quando voce nasceu? ')))
idade = 2025 - nascimento 
if idade < 18:
    print(f'sua idade é de {idade}')
    print('você ainda não pode trabalhar!!')
else:
    cdt = input('carteira de trabalho: ')
    contratadoem = input('ano de contratação: ')
    salario = int(input('Qual seu salario?: '))
    idade = 2025 - nascimento
    print('=' * 35)
    print (f'seu nome é {nome}')
    print('-' * 35)
    print (f'você nasceu em {nascimento}')
    print('-' * 35)
    print (f'sua carteira de trabalho é {cdt}')
    print('-' * 35)
    print (f'você foi contratado em {contratadoem}')
    print('-' * 35)
    print (f'seu salario é de {salario}')
    print('=' * 35)