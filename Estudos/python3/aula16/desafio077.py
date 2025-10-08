
Palavras= 'Aprender', 'Programar', 'Linguagem', 'Python', 'Curso', 'Gratis', 'Estudar', 'Praticar', 'Trabalhar', 'Mercado', 'Programador', 'Futuro'
tupla= 'a','e','i', 'o', 'u'
for Palavras2 in Palavras:
    print(f'As vogais da palavra {Palavras2} são:')
    for letra in Palavras2:
        if letra.lower() in tupla:
            print(f'{letra}')
    