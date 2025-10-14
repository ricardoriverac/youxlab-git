time = []        # Lista que vai armazenar todos os jogadores (cada um como um dicionário)
jogador = {}     # Dicionário temporário para guardar os dados de um único jogador
gols = []        # Lista temporária para armazenar os gols por partida do jogador atual

while True:
    jogador['Nome'] = str(input('Nome: '))  # Lê o nome do jogador
    Partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou?'))  # Lê quantas partidas ele jogou

    for i in range(Partidas):  # Para cada partida, pergunta quantos gols foram feitos
        gols.append(int(input(f'Quantos gols na partida {i + 1}?')))

    jogador['Gols'] = gols[:]              # Copia a lista de gols para o dicionário do jogador
    jogador['Total'] = sum(gols)           # Soma os gols para saber o total e salva no dicionário
    time.append(jogador.copy())            # Adiciona uma cópia do jogador à lista principal "time"

    while True:  # Loop da da resposta (S ou N)
        resp = str(input('Quer continuar [S / N]')).upper()
        if resp not in 'SN':  # Se não for S ou N, mostra erro e pede novamente
            print("ERRO, escreva somente S ou N")
        else:
            break

    if resp == 'N':  # Se a resposta for N, encerra o cadastro de jogadores
        break

    jogador.clear()  # Limpa o dicionário para reutilizar no próximo jogador
    gols.clear()     # Limpa a lista de gols para reutilizar
print('Cod nome      gols             total')  # Cabeçalho da tabela: -----

for i in range(len(time)):  # Para cada jogador na lista "time"
    print(f'{i} {(time[i])["Nome"]}   {(time[i])["Gols"]}   {(time[i])["Total"]}')  # Mostra código, nome, lista de gols e total
while True:  # Início do loop para mostrar detalhes de jogadores
    escolha = int(input(f'Mostrar dados de qual jogador? [999 para parar] '))  # Pede o código do jogador

    if escolha == 999:  # Se digitar 999, sai do loop
        break

    if escolha < 0 or escolha >= len(time):  # Verifica se o código é válido
        print(f'ERRO! Não existe jogador com código {escolha}!')
        continue

    print(f'LEVANTAMENTO do jogador {(time[escolha])["Nome"]}')  # Mostra o nome do jogador escolhido

    for i in range(len((time[escolha])["Gols"])):  # Mostra os gols em cada partida
        print(f'No jogo {i + 1} fez {time[escolha]["Gols"][i]} gols')