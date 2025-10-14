estatisticas= {}
gols=[]
estatisticas['Nome']= str(input('Qual o nome do atleta? '))
soma=0
for c in range (1, 6):
    gols.append(int(input(f'Quantos gols {estatisticas["Nome"]} fez na partida {c}?')))
estatisticas['Gols']= gols
estatisticas['Total de Gols']=sum(gols)
for i, v in enumerate(estatisticas.items()):
    print(f'A informação {v[0]} tem valor {v[1]}')
print(f"""O jogador {estatisticas["Nome"]} jogou 5 partidas 
             >= fez {estatisticas["Gols"][0]} gols na partida 1.
             >= fez {estatisticas["Gols"][1]} gols na partida 2.
             >=fez {estatisticas["Gols"][2]}  gols na partida 3.
             >=fez {estatisticas["Gols"][3]}  gols na partida 4.
             >=fez {estatisticas["Gols"][4]}  gols na partida 5.""")