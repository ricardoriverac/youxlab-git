num = (int(input('Digite o primeiro número: ')),int(input('Digite o segundo número: ')),int(input('Digite o terceiro número: ')), int(input('Digite o quarto número: ')), int(input('Digite o quinto número: ')))
tres = 0
if 3 in num:
    tres = num.index(3)
    print(f'O valor 3 apareceu na posição {tres + 1}')
else:
    print(f'Não há valor 3 na tupla.')
nove = num.count(9)
print(f'Seus valores digitados foram: {num}\nO número nove apareceu {nove} vezes\n')
count = 0
for c in num:
    if c % 2 == 0:
        count += 1
        print(f'Os números pares são: {c}')
