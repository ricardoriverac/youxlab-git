time = []
dic = {}
lista = []
partidas = 0
while True:
    dic['nome'] = str(input('Digite o nome do jogador: '))
    partidas = int(input(f'Quantas partidas o {dic["nome"]} jogou? '))
    for g in range(0, partidas):
        lista.append(int(input(f'Digite a quantidade de gols na partida {g}: ')))
        dic['gols'] = lista[:]
        dic['total'] = sum(lista)
    lista = dic.copy()
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-='*30)
print(dic)
print('-='*30)
