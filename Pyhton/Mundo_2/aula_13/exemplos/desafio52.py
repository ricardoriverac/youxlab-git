numero = int(input('Digite um número para saber se ele é ou não é um número primo: '))
conta = 0
for c in range(1,numero+1):
    if numero % c == 0:
        conta = conta + 1
if conta == 2:
    print(f'O número {numero} é primo!!')
else:
    print(f'O número {numero} não é primo!!')