tabela = ("Flamengo","Santos","Palmeiras","Gremio",
             "Atletico Paranaense", "São Paulo","Internacional",
             "Conrithians","Fortaleza","Goias","Bahia","Vasco",
             "Atletico Mineiro","Fluminense","Botafogo","Ceará",
             "Cruzeiro","CSA","Chapecoense","Avaí")
print ('os cinco primeiros times da tabela são:')
print (tabela[:5])
print ('os ultimos 4 colocados são:')
print (tabela[-4:])
print ('O time em ordem alfabetica é ')
print (sorted(tabela))
print ('O chapecoense esta na posição:')
print (tabela.index('Chapecoense'))