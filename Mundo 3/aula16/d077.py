<<<<<<< HEAD
palavras = ('Mesa', 'Aluguel', 'Paralelepipedo', 'Suco', 'Portugues', 'Matematica')
for p in palavras:
    for p in 'a' and 'e' and 'i' and 'o' and 'u':
=======
minhasPalavras = ('Mesa', 'Aluguel', 'Paralelepipedo', 'Suco', 'Portugues', 'Matematica')
vogais = 'aeiou'
for palavra in minhasPalavras:
    print(f'A palavra {palavra} tem as vogais: ', end='')
    for v in vogais:
        if v in palavra.lower():
            print(v, end=' ')
    print()
>>>>>>> 0fdf57991a5e770f9e2e47de83b45958517ffe41
        