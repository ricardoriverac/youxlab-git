soma = 0 
numero = 0
while True:     
    numero = int(input('Digite um numero: '))
    if numero == 999:
        break  
    soma += numero  
print(f'A soma é {soma}')   
    