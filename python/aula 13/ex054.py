from datetime import date
atual = date.today().year
total_maior = 0
total_menor = 0
for pess in range(1, 8):
    nascimento = int(input(f'Qual o ano de nascimento da {pess} pessoa? :'))
    idade = atual - nascimento
    if idade >= 18:
        total_maior += 1
    else:
        total_menor += 1
print(f'Ao todo tivemos {total_maior} pessoas maiores de idade')
print(f'E tivemos {total_menor} pessoas menores de idade')