minhaTupla = ('pizza', 50, 'suco', 8, 'hamburguer', 27)
print('cardapio')
print('_'*20)
for c in range(0, len(minhaTupla)):
    if c % 2 == 0:
        print(f'{minhaTupla[c]:.<30}', end = ' ')
    else:
        print(f'{minhaTupla[c]:.>7}')
      
