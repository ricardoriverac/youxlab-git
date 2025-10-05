palavras = ('jogar', 'curso', 'trabalhar', 'tupla',
            'vogais', 'programador', 'python', 'dados', 'lista')
for p in palavras:
    print(f'\nNa palavras {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')