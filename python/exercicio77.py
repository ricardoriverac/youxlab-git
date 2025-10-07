comentarios = ('suco', 'maracuja', 'roupa','camisa','carro')
for c in comentarios:
    print(f'comentarios {c} temos ')
    for letra in c:
        if letra.lower() in 'aeiou':
            print(letra)