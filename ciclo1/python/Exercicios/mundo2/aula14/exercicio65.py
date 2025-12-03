resposta = "Sim"
soma = quantidade = media =  maior = menor = 0

while resposta in "Sim":
    numero = int(input("Digite um numero: "))
    soma += numero
    quantidade += 1
    if quantidade == 1: 
        maior = menor = numero
    else: 
        if numero > maior: 
            maior = numero
        if numero < menor: 
            menor = numero 
    resposta = str(input("Quer continuar? [S/N]"))
media = soma / quantidade
print(f"Você digitou {quantidade} e o menor foi {menor}")