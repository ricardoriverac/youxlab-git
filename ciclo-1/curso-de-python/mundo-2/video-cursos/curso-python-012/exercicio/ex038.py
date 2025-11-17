valor1 = int(input('Digite um número: '))
valor2 = int(input('Digite outro número: '))

if valor1 > valor2:
    print(f'O número {valor1} é maior!')

elif valor1 < valor2:
    print(f'O número {valor2} é maior!')

else:
    print('Não há um número maior que o outro, os dois são iguais.')