numero = int(input('Digite um número: '))
a = 1
b = 0
contagem = 1
while contagem <= numero:
    resultado = (a+b) - ((a+b)-b)
    print(f'{resultado} -> ',end='')
    a = a + b
    b = a - b
    contagem = contagem + 1
print('Acabou!')