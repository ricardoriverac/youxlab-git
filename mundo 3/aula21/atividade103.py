def ficha(nome = "<desconhecido" , gols = 0):
    print(f"o jogador {nome} fez {gols} no camp")
nome = input('Nome do jogador: ').strip()
gols = input('Número de gols: ').strip() 
if nome == "":
    nome = "desconhecido"
if gols.isnumeric():
    gols = int(gols)
else:    
    gols = 0  
ficha(nome,gols)      
