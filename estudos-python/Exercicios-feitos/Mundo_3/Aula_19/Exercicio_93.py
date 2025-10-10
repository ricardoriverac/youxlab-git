contador = 0
soma = 0
while True:
    numero = int(input('Escreva'))
    if numero == 999:
        break
    contador += 1
    soma += numero
print (soma/contador)