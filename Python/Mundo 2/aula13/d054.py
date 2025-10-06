from datetime import date
atual = date.today().year
totalmaior = 0
totalmenor = 0
for pessoa in range(1, 8):
    nascimento = int(input(f'Em que ano a {pessoa}º pessoa nasceu? '))
    idade = atual - nascimento
    if idade >= 21:
        totalmaior += 1
    else:
        totalmenor += 1
print(f'Ao todo tivemos {totalmaior} pessoa maiores de idade.')
print(f'E também tivemos {totalmenor} pessoas menores de idade.')