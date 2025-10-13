lista = {}
lista2 = list()
count = 0

lista['nome'] = str(input('Qual o nome do jogador? '))
lista['partidas'] = int(input('Quantas partidas você jogou? '))
while count != lista['partidas']:
    count+= 1
    lista2.append(int(input('Numeros de gols feitos: ')))
    lista['gols'] = lista2[:]
print (lista)