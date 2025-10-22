from random import randint
lista = list()
jogos = list()
print('-' * 30)
print('     JOGO DA MEGA SENA     ')
print('-' * 30)
quantidade = int(input('Quantos jogos você quer que eu sorteie?:'))
total = 1
while total <= quantidade:
    cont = 0 
    while True:
        numero = randint(1,60)
        if numero not in lista:
            lista.append(numero)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1
print('-=' * 30, f' SORTEADO {quantidade}  JOGOS','-=' * 3)
for i, l in enumerate(jogos):
        print(f'Jogo {i+1}: {l}')
        slice(2)
print('-=' * 5, '< BOA SORTE! >', '-=' * 5)
