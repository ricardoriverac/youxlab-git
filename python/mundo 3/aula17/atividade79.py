recebedor = []
while True:
    valor = int(input("digite um numero: "))
    recebedor.append(valor) 
    recebedor.sort()
    resposta = str(input("quer continuar? [s/n] ")).lower()
    while resposta != "s" and resposta != "n":
          resposta = str(input("quer continuar? [s/n] ")).lower()
    while resposta == "s":
              valor = int(input("digite um numero: ")) 
              if valor not in recebedor:
                     recebedor.append(valor)
              else:
                print("esse numero ja foi adicionado") 
                resposta = str(input("quer continuar? [s/n] ")).lower()           
    if resposta == "n":
            break
print(f" {recebedor} esse sao os valores digitados")


 