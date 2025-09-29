numero = soma = contador = 0
while True:
    numero = int(input('Digite um numero,[ digite 999] para parar:'))
    if numero == 999:
        break
    contador += 1
    soma += numero
print(f'A soma dos {contador} numeros é {soma}!!!')