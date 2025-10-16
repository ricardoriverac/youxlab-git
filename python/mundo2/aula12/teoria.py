nome = str(input('Digite seu nome: '))
if nome == 'Thawane':
    print('Que nome diferente!')
elif  nome == 'Pedro' or nome == 'Helena' or nome == 'Ravi':
    print('Seu nome é lindo!')
elif nome in ('Natalia Sofia Geisy'):
    print('Seu nome é bem bonito.')
else:
    print('Seu nome é bem comum.')
print(f'É um prazer te conhecer {nome}, tenha uma boa noite!')

