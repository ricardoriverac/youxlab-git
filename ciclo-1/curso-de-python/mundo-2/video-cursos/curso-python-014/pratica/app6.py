numero = 1
par = impar = 0
while numero != 0:
    numero = int(input('Digite um valor: '))
    if numero != 0: #Faz o número 0 não ser contado no resultado final do terminal.
        if numero % 2 == 0: 
            par += 1
        else:
            impar += 1
print(f'Você digitou {par} números pares e {impar} números ímpares!')