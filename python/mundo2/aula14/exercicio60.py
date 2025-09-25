numero=int(input('Digite um numero: '))
numero_inicial=numero
resultado= 1
while numero>0:
    resultado= resultado*numero
    print(f'{numero}')
    numero-=1
print(f'O fatorial de {numero_inicial} é {resultado}')