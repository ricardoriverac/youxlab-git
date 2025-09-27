numero = soma = contador = 0
# contador = 0
while True:
    numero = int(input('Digite um número (Digite 999 para parar o programa): '))
    if numero == 999:
        break
    contador += 1 
    soma += numero
    
print(f'ACABOU. Soma vale {soma} e a quantidade de números é {contador} vezes.')