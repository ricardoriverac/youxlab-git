total_de_gols_feito = 0
gols_feito = []
print("-="*20)
print("DADOS DO JOGADOR ")
print("-="*20) 

nome_do_jogador =  str(input("digite seu nome : "))
partidas_jogadas = int(input(f"jogou quantas partidas {nome_do_jogador}: "))
for n in range(partidas_jogadas):
    gols = int(input(f"quantos gols vc fez na partida {n+1}? "))
    gols_feito.append(gols)

jogador = {"nome do jogador": nome_do_jogador,
'gol feitos em cada partida': gols_feito,
'partidas jogadas': partidas_jogadas,
'total de gols': sum(gols_feito) }  

print("-="*20) 
print("RESULTADOS DO JOGADOR DURANTE O CAMPEONATO") 

for k,v in jogador.items():
    print(f"{k} = {v}")
