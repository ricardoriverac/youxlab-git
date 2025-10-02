numero=0
soma=0
contador=0
while  numero != 999:
    numero = int(input('Digite um numero [999 para parar]: '))
    soma+=numero
    contador+=1
print(f'Voce digitou {contador-1}, e a soma foi {soma-999}')