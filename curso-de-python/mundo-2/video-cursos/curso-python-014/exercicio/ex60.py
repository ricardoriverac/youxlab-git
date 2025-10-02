numero = int(input("Digite um valor: "))
contador = numero
fatorial = 1

while contador > 0:
    if contador == 1:
        print(f'{contador} = ', end='')
    else:
        print(f'{contador} x ', end='')
    fatorial *= contador
    contador -= 1

print(fatorial)