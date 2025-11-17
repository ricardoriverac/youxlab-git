palavras = ('anuncio', 'mouse', 'escola', 'video', 'joao', 'pokemon', 'oculos', 'mercado', 'online', 'curso', 'diploma', 'musica', 'exercicio', 'hora', 'conexao', 'skate')

for palavra in palavras:
    print(f'\nNa palavra \033[32m{palavra.upper()}\033[m temos as vogais: ', end=' ')

    for vogais in palavra:
        if vogais.lower() in 'aeiou':
            print(vogais, end=' ')