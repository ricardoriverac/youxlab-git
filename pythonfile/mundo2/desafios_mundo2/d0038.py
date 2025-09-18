numero = int(input('Digite um numero inteiro: '))
numero2 = int(input('Digite o segundo numero: '))
if numero > numero2:
    print((f'O {numero} é o maior'))
elif numero2 > numero:
    print(f'O {numero} é o maior ')
else:
    print('Os dois valores são iguais')
