from datetime import date
atual = date.today().year
for pessoas in range(1, 8):
    nascimento = int(input('Em que ano voce nasceu? '))
    idade = atual - nascimento
    if idade >= 18:
        print('Essa pessoa é de maior')
    else:
        print('Essa pessoa é de menor')