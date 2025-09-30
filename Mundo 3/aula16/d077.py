minhasPalavras = ('Mesa', 'Aluguel', 'Paralelepipedo', 'Suco', 'Portugues', 'Matematica')
vogais = 'aeiou'
for palavra in minhasPalavras:
    print(f'A palavra {palavra} tem as vogais: ', end='')
    for v in vogais:
        if v in palavra.lower():
            print(v, end=' ')
    print()
        