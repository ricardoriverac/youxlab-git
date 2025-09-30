numero = int(input('Digite um número: '))
conta = numero
fatorial = 1
print(f'analisando {numero} = ', end='')
while conta > 0:
    print(f'{conta}', end='')
    print(' x ' if conta > 1 else ' = ', end='')
    fatorial *= conta
    conta -= 1
print(f'{fatorial}')