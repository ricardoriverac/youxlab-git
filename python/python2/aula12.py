nome = str(input('Qual é o seu nome'))
if nome == 'Agatha':
    print('Que nome bonito!')
elif  nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é popular non Brasil')
elif nome in 'Ana Claudia Jessica Juliana':
    print('Belo nome feminino')
else:
    print('seu nome é bem normal')
print(f'Tenha um bom dia {nome}')
