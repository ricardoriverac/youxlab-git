lanche = ['pizza', 'hamburguer', 'cookie']
lanche.append('suco')
lanche.insert(3, 'shwarma')
if 'kibe' not in lanche:
    lanche.insert(4, 'kibe')
if 'pizza' in lanche:
    del lanche['pizza']
print(lanche)