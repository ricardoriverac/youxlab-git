total_de_gols_feito = 0
time = []
print("-="*20)
print("DADOS DE JOGADORES ")
print("-="*20) 
resposta = "" 

while resposta != "n":
    nome_do_jogador =  str(input("digite seu nome : "))
    partidas_jogadas = int(input(f"jogou quantas partidas {nome_do_jogador}: "))
    gols_feito = []

    for n in range(partidas_jogadas):
            gols = int(input(f"quantos gols vc fez na partida {n+1}? "))
            gols_feito.append(gols)
    jogador = {"nome do jogador": nome_do_jogador,
    'gol feitos em cada partida': gols_feito,
    'partidas jogadas': partidas_jogadas,
    'total de gols': sum(gols_feito) } 
    time.append(jogador)
    resposta = str(input("quer continuar? [s/n]")).lower()

    for i,jogador in enumerate(time):
          print(f"{i} - {jogador['nome do jogador']} com {jogador['total de gols']} gols no total.")
while True:
        escolha = int(input("voce que saber o resultado de qual jogador: [999 encerra o programa] "))
        if escolha == 999:
            break
        if 0 <= escolha < len(time):
            jogador = time[escolha]
            for k,v in jogador.items():
                print(f"{k} = {v}")
        else:
             print("JOGADOR NAO ENCONTRADO")    