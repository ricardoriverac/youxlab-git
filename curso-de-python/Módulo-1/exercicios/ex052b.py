numero = int(input('Digite o número que deseja saber se é um número primo: '))
for c in range(1, numero + 1):
    numero % c == 0
if numero == 2:
    print(f'O número {numero} é primo!')
else:
    print(f'O número {numero} não é primo!')