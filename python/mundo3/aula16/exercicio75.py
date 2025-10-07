valor1 = int(input('Digite um valor: '))
valor2 = int(input('Digite um valor: '))
valor3 = int(input('Digite um valor: '))
valor4 = int(input('Digite um valor: '))
numero = (valor1, valor2, valor3, valor4)
print(f'Os valores digitados foram: {numero}')
if numero.count(9) == 1:
    print(f'O número 9 apareceu {numero.count(9)} vez')
elif numero.count(9) == 0:
    print('O número 9 não foi digitado')
else:
    print(f'O número 9 apareceu {numero.count(9)} vezes')
if 3 in numero:
    print(f'O primeiro número 3 foi digitado na {numero.index(3) + 1}ª posição')
else:
    print('Não tem nenhum número 3 nos valores digitados')
print('Os valores pares digitados foram: ',end = '')
for p in numero:
    if p % 2 == 0:
        print(p)
