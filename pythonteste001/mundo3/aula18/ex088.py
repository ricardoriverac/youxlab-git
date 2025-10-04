from random import randint

lista = list()
jogadas = list()
titulo = ' MEGA SENA '
print(f'{titulo:=^30}')
jogos = int(input('Quantos palpites da mega sena você quer ver? '))
total = 1
while total <= jogos:
    contagem = 0
    while True:
        numeros = randint(1, 60)
        if numeros not in lista:
            lista.append(numeros)
            contagem += 1
        if contagem >= 6:
            break
    lista.sort()
    jogadas.append(lista[:])
    lista.clear()
    total += 1
for i, l in enumerate(jogadas):
    print(f'Palpite {i+1}: {l}')