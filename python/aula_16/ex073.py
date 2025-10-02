'''
Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética. 
d) Em que posição está o time da Chapecoense.
'''

brasileirao_2025 = (
    "Flamengo",
    "Cruzeiro",
    "Palmeiras",
    "Mirassol",
    "Botafogo",
    "Bahia",
    "São Paulo",
    "Fluminense",
    "Red Bull Bragantino",
    "Grêmio",
    "Ceará",
    "Vasco da Gama",
    "Atlético Mineiro",
    "Corinthians",
    "Internacional",
    "Santos",
    "Juventude",
    "Vitória",
    "Fortaleza",
    "Sport",
)
print(brasileirao_2025[0:5])
print(brasileirao_2025[-4:])
print(sorted(brasileirao_2025))
print(brasileirao_2025.index('Palmeiras'))