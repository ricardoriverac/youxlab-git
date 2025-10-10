jogador = {}
dadosJogador = []
print('-'*35)
print('   CADASTRANDO JOGADOR DE FUTEBOL:   ')
jogador['nome'] = str(input('-> Nome do Jogador: '))
jogador['qtd_partidas'] = int(input('-> Quantas partidas jogadas: '))
jogador['soma_gols'] = 0
for g in range(jogador['qtd_partidas']):
    jogador['gols em partidas'] = int(input(f'-> Quantos gols jogador fez na partida {g+1}: '))
    jogador['soma_gols'] += jogador['gols em partidas']
print('-'*30)
print('->->->-> DADOS FINAIS <-<-<-<-')
print('-'*30)
print(f'-Nome do Jogador: {jogador["nome"]}.\n-Partidas jogadas: {jogador["qtd_partidas"]}.\n-O jogador {jogador["nome"]} fez {jogador["soma_gols"]} gols no campeonato.')
print('=-'*15)
print('FINALIZANDO...')
print('=-'*15)