nome = str(input('Qual é o seu nome: '))
if nome == 'Luis':
    print('Que nome bonito!')
elif nome == 'Maria' or nome == 'Julia' or nome == 'Ana':
    print('Seu nome é bem popular no Brasil!')
elif nome in 'Amanda Luisa Gustavo Carol':
    print('Belo nome feminino!')
else:
    print('Seu nome é bem normal.')
print(f'Tenha um bom dia, {nome}!')