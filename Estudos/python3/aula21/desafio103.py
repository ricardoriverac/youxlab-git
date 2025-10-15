def ficha(a='<desconhecido>', b=0):
    print(f'O jogador {a} fez {b} gols')


nome= str(input('Digite o nome do jogador: '))
gols= input('Digite a quantidade de gols feita pelo jogador')
if gols.isdigit():
    gols = int(gols)
if isinstance(gols, str):
    ficha(a= nome)
if nome == '':
    ficha(b=gols)
ficha(nome, gols)
