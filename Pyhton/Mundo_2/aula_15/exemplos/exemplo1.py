#exemplo sobre o break

numeron= a = 0
numero = int(input('Digite um número: '))
while True:
    numero = int(input('Digite um número: '))
    if numero == 999:
        break
    a = numero + a
    print(f'A soma vale {a}')