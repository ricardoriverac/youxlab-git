from datetime import date


nome = input('qual é o seu nome? ')
idade = input('quantos anos você tem? ')
linguagem_favorita = input('qual é a sua linguagem de programação favorita? ')
data_atual = date.today()
ano_atual = data_atual.year
print(f"O ano atual é: {ano_atual}")
print(f'Você se chama:{nome} \n sua idade é:{idade} \n sua linguagem favorita é:{linguagem_favorita}')
print(f'você nasceu no ano de {(ano_atual) - int(idade)}')