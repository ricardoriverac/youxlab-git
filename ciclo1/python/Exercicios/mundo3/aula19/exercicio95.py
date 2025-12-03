#refazendo o exercicio 93 adicionando uma quantidade ilimitada de quantos jogadores e podendo ver os dados de cada um.

jogadores = []
jogos = {}
partidas = []
resposta = "S"

while resposta != "N":
    jogos.clear()
    jogos['nome'] = str(input("Qual o nome do jogador?: "))
    total = int(input("Quantas partidas ele jogou?: "))
    partidas.clear()
    
    for i in range(1, total+1):
        partidas.append (int(input(f"Quantos gols ele fez na {i}ª partida?: ")))
    
    jogos['gols'] = partidas [:]
    jogos['total'] = sum(partidas)
    jogadores.append(jogos.copy())
    
    resposta = str(input("Deseja continuar? [S/N]: ")).upper()
    
for i in jogos.keys():
    print(f"{i}", end="   ")
print()

for c, d in enumerate(partidas):
    print(f"{c}", end=" ")
    for e in d.values():
        print(f"{str(e)}", end="  ")
    print()
    
while True:
    busca = int(input("Mostra dados de qual jogador (1 para encerrar): "))
    if busca == 1:
        break
    if busca >= len(jogadores):
        print(jogadores)