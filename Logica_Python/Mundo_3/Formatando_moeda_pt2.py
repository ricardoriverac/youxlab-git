from utilidadescev import moeda
p = float(input('Digite o valor: '))
print(f'A metade é {moeda.metade(p, True)}')
print(f'O dobro é {moeda.dobro(p, True)}')
print(f'Aumentando 10%, temos {moeda.aumentar(p, 10, True)}')
print(f'Dimunuindo 13%, temos {moeda.diminuir(p, 13, True)}')

help(moeda.aumentar)