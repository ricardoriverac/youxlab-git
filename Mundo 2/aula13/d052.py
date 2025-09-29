numero = int(input('Digite um número: '))
contador_divisores = 0
for primo in range(1, numero +1):
    if numero % primo == 0:
        contador_divisores += 1

if contador_divisores == 2:
    print('Esse número é um número PRIMO!')
else:
    print('Esse número NÃO é um número primo')


