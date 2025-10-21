num1 = int(input('Digite um numero: '))
num2 = int(input('Digite um numero: '))
num3 = int(input('Digite um numero: '))
num4 = int(input('Digite um numero: '))
minhaTupla = (num1,num2,num3,num4)
print(f'Os valores digitados foram {minhaTupla}')
print(f'O valor 9 aparece {(minhaTupla.count(9))} vezes ')
print(minhaTupla.index(3))
print(f'os numeros pares sao: ')
for n in minhaTupla:
    if n % 2 == 0:
        print(n)