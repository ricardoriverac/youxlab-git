numero = total = cont = 0
while numero != 999:
    numero = int(input('Digite um número inteiro ou 999 para parar: '))
    if numero != 999:
        total += numero
        cont += 1
print('Foram digitados {} números e a soma entre eles foi {}'.format(cont, total))
