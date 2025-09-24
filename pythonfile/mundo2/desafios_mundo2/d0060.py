from math import factorial
numero = int(input('Digite um numero: '))
fatorial = factorial(numero)
while numero < 0:
    fatorial *= numero
    numero -= 1
print(f'O fatorial de {numero} é {fatorial} ')