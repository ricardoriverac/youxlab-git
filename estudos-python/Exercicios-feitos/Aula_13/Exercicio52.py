numero = int(input('Escolha um número: '))
vezesQueFoiDividido = 0
for contagem in range (1, numero+1):
    if numero % contagem == 0:
        print (f'\033[33m {contagem} \033[')
        vezesQueFoiDividido += 1
    else:
        print (f'\033[31m {contagem}\033[')
print (f'Ele foi dividido {vezesQueFoiDividido} vezes')
if vezesQueFoiDividido == 2:
    print ('\033[32m Ele é um número primo!!!\033[32m')
else:
    print ('\033[31m Ele não é primo!!!\033[31m')