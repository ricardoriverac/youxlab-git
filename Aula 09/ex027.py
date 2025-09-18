nome_completo = str(input('Qual o seu nome completo?')).strip()
nome = nome_completo.split()
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome)-1]))

