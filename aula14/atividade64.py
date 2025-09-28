#numero = int(input("digite um numero: "))
soma = 0 
quantidade = 0
numero = int(input("digite um numero: "))
while numero < 999:
    quantidade = quantidade + 1
    soma = soma + numero
    numero = int(input("digite um numero: ")) 
print (f"essa foi a quantidade de numeros digitados {quantidade}")  
print(f"essa ea soma entre todos numeros {soma}")
