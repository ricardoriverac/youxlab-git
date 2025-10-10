from datetime import date
atual = date.today().year
totalmaior = 0
totalmenor = 0
for pessoas in range(1, 8):
    nascimento = int(input(f'em que ano a {pessoas}ª pessoa nasceu? '))
    idade = atual - nascimento
    if idade >= 18:
        totalmaior += 1
    else:
        totalmenor += 1
print(f'Ao todo tivemos {totalmaior} maiores de idade e {totalmenor} menores de idade!')
