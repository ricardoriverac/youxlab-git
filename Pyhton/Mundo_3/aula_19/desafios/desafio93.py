dicionario = {}  # Dicionário para guardar dados do jogador
lista = []       # Lista para armazenar os gols por partida

# Entrada de dados:
dicionario['nome'] = str(input('Nome do jogador:'))  # nome do jogador
partidas = int(input('Quantas partidas ele jogou?'))  # número de partidas

# Loop para registrar os gols em cada partida
for c in range(1, partidas + 1):  # Vai do 1 até o número de partidas
    lista.append(int(input(f'Quantos gols ele fez na {c}ª partida ?')))  # Adiciona os gols à lista

# Armazena os dados no dicionário:
dicionario['gols'] = lista[:]  # Salva a lista de gols (usando [:] para copiar)
dicionario['total'] = sum(dicionario['gols'])  # Soma total de gols e salva!

# Mostrando dados:
print('-=' * 30)
for k, i in dicionario.items():
    print(f'O campo [{k}] tem valor {i}')

# mostra detalhes das partidas:
print('-=' * 30)
print(f'O jogador {dicionario["nome"]} jogou no total {partidas}')  # Mostra total de partidas jogadas
for k, i  in enumerate(dicionario['gols']):  # Mostra quantos gols fez em cada partida
    print(f'    => na partida {k + 1}, ele fez {i} gols')

# Exibe o total de gols novamente (opcional, pois já foi mostrado antes)
print(f'O total de gols foi {sum(dicionario["gols"])}')