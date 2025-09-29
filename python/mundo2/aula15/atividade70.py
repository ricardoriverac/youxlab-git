valor_barato = 0
nome_barato = ""
soma = 0
primeiro = True
valor1000 = 0 
resposta = "s"
while True:
    produto = str(input("digite o nome do produto: "))
    preço = float(input("quantos que custou:  "))
    soma = soma + preço
    if preço >= 1000:
        valor1000 = valor1000 + 1
    if primeiro == True:
        primeiro = False
        valor_barato = preço
        nome_barato = produto
    else:
        if preço < valor_barato:
          valor_barato = preço
          nome_barato = produto
    resposta = str(input("quer continuar [s,n]")).lower()        
    if resposta == "n":
        break
print(f"o total gasto foi {soma} e {valor1000} passaram de 1000R$, o menor valor e {valor_barato} eo nome e {nome_barato} ")    
