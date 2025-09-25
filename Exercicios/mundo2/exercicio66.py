soma = contador = 0

while True: 
    numero = int(input("\nobs: digite [999] para encerrar\n" 
    "Digite um valor: "))
    if numero == 999: 
        break
    contador += 1 
    soma += numero
print(f"A soma dos {contador} valores foi de {soma}!")