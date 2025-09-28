soma = 0
count = 0
for numeros in range(1, 7):
    number = int(input(f'Digite o {count} número: '))
    if number % 2 == 0:
        print('Número adicionado no cálculo!')
        soma += number
    else:
        print('Esse número não é par!')    
    count += 1
print(f'A soma de todos os números pares de 1 a 6 é {soma}')