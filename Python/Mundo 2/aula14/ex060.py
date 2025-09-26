numero = int(input('Digite um número: '))
if numero == 0 or numero == 1:
    print("O fatorial de", numero, "é 1")
else:
    fatorial = 1
    contador = numero
    while contador > 0:
        fatorial = fatorial * contador
        contador = contador - 1
    print("O fatorial de", numero, "é", fatorial)
