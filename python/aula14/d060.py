numero = int(input('Escreva um número: '))
contagem = numero
fatorial = 1
print(f'Calculando {numero}! = ', end='')
while contagem > 0:
    print(f'{contagem}', end='')
    print(' x ' if contagem > 1 else ' = ', end='')
    fatorial *= contagem
    contagem -= 1
print(f'{fatorial}')


    


