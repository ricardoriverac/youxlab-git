numero = 0 
soma = 0
contador = 0
while True:
    numero = int(input('Digite um numero (999 pra parar):  '))
    if numero == 999:
        break      
    soma += numero
    contador +=1
print(f'Você digitou {contador} valores e a soma entre eles foi {soma}. ')