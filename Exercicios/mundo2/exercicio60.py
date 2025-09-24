numero = int(input('Digite um numero para saber o seu fatorial: '))
calculo= numero 
fatorial = 1
print(f"Calculando {numero}")

while calculo > 0:
    print(f"{calculo}")
    fatorial = calculo * fatorial
    calculo -= 1
print(f"{fatorial}")