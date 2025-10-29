numero = int(input('Digite um número inteiro: '))
total_divisores = 0
for i in range(1, numero + 1):
    if numero % i == 0:
        total_divisores += 1
if total_divisores == 2:
    print(f'O número {numero} É PRIMO!')
else:
    print(f'O número {numero} NÃO É PRIMO!')
