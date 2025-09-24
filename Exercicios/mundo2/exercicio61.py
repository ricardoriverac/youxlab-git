primeiro_termo = int(input("Digite o numero do primeiro termo: "))
razao = int(input("Digite o valor da razão: "))
termo = primeiro_termo 
contador = 1

while contador <= 10: 
    print(f"{termo}")
    termo += razao
    contador += 1