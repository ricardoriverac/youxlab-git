numero = contador = soma =0

while numero != 999: 
    numero = int(input("Digite um numero: " 
    "obs: para parar o codigo digite [999] "))
    soma += numero
    contador += 1 
    numero = int(input("Digite um numero " 
    "obs: para parrar digite [999]"))
print(f"Você digitou {contador} e a soma entre eles é {soma}")