# Curso Python #012 - Condições Aninhadas
# if carro.esquerda():
# se 
#     carro.siga()
#     carro.esquerda()
#     carro.siga()
#     carro.direita()
# elif carro.direta():
# senão se
#     carro.siga()
#     carro.direita()
#     carro.siga()
# else:
# senão
    # carro.esquerda()
    # carro.siga()
    # carro.pare()
# PRÁTICA 
nome = str(input('Qual é o seu nome? '))
if nome == 'Julia':
    print(f'Que nome bonito!')
elif nome == 'Igor' or nome == 'Pablo' or nome == 'Daniela':
    print('Seu nome é bem popular Brasil.')
elif nome in 'Maria Paula Vitória Lara':
    print('Belo nome feminino.')
else:
    print('Seu nome é tão normal.')
print(f'Tenha um bom dia, {nome}!')