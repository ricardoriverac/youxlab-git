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