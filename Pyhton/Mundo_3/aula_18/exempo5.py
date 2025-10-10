galera = list()
dado = list()
totalmaioridade = 0
totalmenoridade = 0
for c in range(0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear() #muito importante usar os dois pontos
print(galera)