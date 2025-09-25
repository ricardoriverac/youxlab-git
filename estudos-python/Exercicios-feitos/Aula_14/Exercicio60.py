numero = int(input('Escolha um número: '))
contador = numero
fatorial = 1
while contador>0:
    print (f'{contador}', end='')
    print (' X ' if contador > 1 else ' = ', end='')
    fatorial *= contador
    contador-=1
print (f'{fatorial}')