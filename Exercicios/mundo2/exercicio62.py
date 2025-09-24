primeiro_termo = int(input("Digite o numero do primeiro termo: "))
razao = int(input("Digite o valor da razão: "))
termo = primeiro_termo 
contador = 1

while contador <= 10: 
    print(f"{termo}")
    termo += razao
    contador += 1

quantos_termos_a_mais = int(input("Quantos termos a mais você quer?: "))

while quantos_termos_a_mais != 0:
    c = 0
    while c < quantos_termos_a_mais:
        print(f"{termo}")
        termo += razao
        c += 1
    quantos_termos_a_mais = int(input("Quantos termos a mais você quer?: "))

print("Finalizado")