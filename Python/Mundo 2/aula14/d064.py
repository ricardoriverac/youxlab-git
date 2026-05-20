numero = contar = soma = 0 
numero = int(input('Digite um valor [999 para parar]: '))
while numero != 999:
   soma += numero
   contar += 1 
   numero = int(input('Digite outro valor [999 para parar]: '))
print(f'Você digitou {contar} números, e a soma entre eles foi {soma}.')

