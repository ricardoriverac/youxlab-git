times = ('Corinthians', 'Palmeiras', 'Santos', 'Gremio', 
         'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense',
         'Atletico', 'Botafogo', 'Atletico-PR', 'Bahia', 
         'São Paulo', 'Fluminense', 'Sport Recife', 'EC Vitoria', 
         'Coritiba', 'Avai', 'Ponte Preta', 'Atletico_GO')

for a in range(5):
    print(f"Os 5 primeiros times são: {times[a]}")
print("")
for b in range(4):
    print(f"Os 4 ultimos são: {times[16 + b]}")
print("")
ordem = sorted(times)
for c in ordem:
    print(f"Em ordem alfabetica: {c}")
print("")
for index,d in enumerate(times):
    if (times[index] == "Chapecoense"):
        print(f"A posição da Chapecoense está em {index +1}")








#print("")
#print(f'Os cinco primeiros times são: {times[0:5]}')
#print("")
#print(f'Os ultimos 4 colocados são: {times[16:]}')
#print("")
#print(f"Em ordem alfabetica: {}")



