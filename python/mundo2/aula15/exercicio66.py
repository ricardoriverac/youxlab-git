numero=0
soma=0
contador=0
while  numero != 999:
    numero = int(input('Digite um numero [999 para parar]: '))
    soma+=numero
    contador+=1
print(f'A soma dos valores {contador-1} foi {soma-999}')