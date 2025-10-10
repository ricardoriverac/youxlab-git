palavras = ('DINHEIRO', 'FELICIDADE', 'FAMILHA', 'FOME', 'ESPERANCA', 'FE', 'TECNOLOGIA', 'PYTHON', 'GANAMSTYLE')
for p in palavras:
    print(f'\nA palavra {p} tem as vogais ', end = '')
    for letra in p:
        if letra.upper() in 'AEIOU':
            print(letra, end = ' ')