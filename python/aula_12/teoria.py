# condições aninhadas 
nome = str(input('Qual é o seu nome? ')) 
if nome == 'Ana':
    print('Que nome bonito! ')
elif nome == 'Isabela' or nome == 'Marcela' or nome == 'José':
    print('Seu nome é bem popular no Brasil. ')
elif nome in 'Luciane Kayllane Sebastiana':
    print('Belo nome feminino. ')
else: 
    print('Seu nome é bem normal. ')
print(f'Tenha um bom dia, {nome}!')

# o 'elif' pode ser usado inúmeras vezes,desde que esteja antes de 'else' e depois de 'if'
