from datetime import date
atual = date.today().year
maior = 0
menor = 0
for pessoa in range(1, 8):
    nascimento = int(input(f'Digite o ano de nascimento da {pessoa}ª pessoa: '))
    idade = atual - nascimento
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print(f'\nAo todo tivemos {maior} pessoas maiores de idade.')
print(f'E também tivemos {menor} pessoas menores de idade.')

