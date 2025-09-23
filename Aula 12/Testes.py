nome = str(input('Qual é seu nome? '))
if nome == 'Marcela':
    print('Que nome mais bonito! ')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo': 
    print('Seu nome é bem popular no Brasil.')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}!'.format(nome))