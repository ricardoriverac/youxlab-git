numero = soma = contador = 0
while True:
    numero = int(input('digite um número[999 para parar]: '))
    if numero == 999:
        break
    soma += numero
    contador += 1
print(f'você digitou {contador} números e a soma deles é {soma}')