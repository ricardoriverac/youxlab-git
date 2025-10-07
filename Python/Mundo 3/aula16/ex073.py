# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética. 
# d) Em que posição está o time da Chapecoense.
tabela = (
    "Flamengo",
    "Cruzeiro",
    "Palmeiras",
    "Bahia",
    "Botafogo",
    "Mirassol",
    "São Paulo",
    "Bragantino",
    "Fluminense",
    "Ceará",
    "Corinthians",
    "AtléticoMG",
    "Internacional",
    "Grêmio",
    "Santos",
    "Juventude",
    "vasco",
    "Vitória",
    "Sport",
    "Fortaleza",
)
print(tabela[0:5])
print(tabela[16:20])
print(sorted(tabela))
print(f"A posição do vasco e {tabela.index('vasco')} na posiçao ")