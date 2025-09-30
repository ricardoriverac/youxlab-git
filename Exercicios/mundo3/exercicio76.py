nomes_preços = ()

for produtos in range(2):
    nomes = str(input(f"Qual o nome do {produtos+1}ª produto?: "))
    preco = float(input(f"Qual o preço do {produtos+1}ª produto?: "))
    nomes_preços += (nomes, preco)
print("nome/preço")
for ordem in range(0,len(nomes_preços), 2):
   print(nomes_preços[ordem], " -> ",nomes_preços[ordem+1])