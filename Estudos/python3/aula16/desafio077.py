
Palavras= ('Aprender', 'Programar', 'Linguagem', 'Python', 'Curso', 'Gratis', 'Estudar', 'Praticar', 'Trabalhar', 'Mercado', 'Programador', 'Futuro')
vogais= ('a','e','i', 'o', 'u')
for c in Palavras:
    print(f'As vogais da palavra {c} são:')
    for letra in c:
        if letra.lower() in vogais:
            print(f'{letra}')
    