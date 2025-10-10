from random import randint

quantidade_jogos = int(input('Quantos jogos serão gerados? '))
lista_jogos = []

for i in range(quantidade_jogos):
    jogo = []
    for n in range(6):
        numero = randint(1, 60)
        jogo.append(numero)
    lista_jogos.append(jogo)

print(lista_jogos)