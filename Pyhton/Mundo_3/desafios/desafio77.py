palavra = ('jogo', 'computador', 'musica', 'carregador', 'gato',
            'internet', 'escola', 'roupas', 'compras', 'volei',
            'dinheiro', 'celular', 'paralelepipedo')
for c in palavra:
    print(f'A palavra {c} possui essas vogais: ', end='')
    for l in range(0, len(c)):
        if c[l] in 'aeiou':
            print(c[l], end=' ')
    print()