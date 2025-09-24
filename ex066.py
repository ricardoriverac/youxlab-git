numero = 0 
soma = 0
numerosdigitados = 0
while True:
    numero = int(input('Digite um numero '))
    if numero == 999:
        break
    soma += numero  
    numerosdigitados += 1
print(f'Foram digitados {numerosdigitados} numeros a soma vale {soma}')