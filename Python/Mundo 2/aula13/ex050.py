somaPares = 0 
for c in range(0, 6):
    numero = int(input('Digite o um número: '))
    if (numero %2) != 0:
        somaPares += numero
print(f'O somátorio de todos os valores foi {somaPares}') 