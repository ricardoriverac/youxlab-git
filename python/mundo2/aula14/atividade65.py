resposta = "s"
quantidade = 0
soma = 0
maior = 0 
menor = 0
#numero = int(input("digite um numero: "))
while resposta == "s": 
    numero = int(input("digite um numero: "))
    quantidade = quantidade  + 1
    soma += numero
    if quantidade == 1:
        maior = numero
        menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    resposta = str(input(f"voce deseja continuar? [s/n]: ")).lower() 
    media = soma / quantidade
print(f" a media foi {media} eo maior numero foi {maior} eo menor foi {menor}" )   
