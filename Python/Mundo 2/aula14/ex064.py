numeros = 0
cont = 0
soma = 0 
numeros = int(input('Digite um número [Digite 999 para parar o programa]: '))
while numeros != 999:
    soma += numeros
    cont += 1
    numeros = int(input('Digite um número:'))
print(f'Você digitou {cont} números e a soma entre eles foi {soma}.')