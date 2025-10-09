def campeonato(nome='Desconhecido', gols=0):
    if nome.strip() == '':
        nome = 'Desconhecido'
    if not gols.isnumeric():
        gols = 0
    return f'O jogador <{nome}> fez: {gols} gols no campeonato.'


n = str(input('Nome do Jogador: ')).title()
g = str(input('Número de gols: '))
print(campeonato(n, g))