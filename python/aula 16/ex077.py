palavras = ('amizade', 'python', 'programar', 'aprender',
            'curso', 'video', 'estudos', 'gratis', 'aula')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos  ' , end='')
    for vogal in p:
        if vogal in p:
            if vogal.lower() in 'aeiou':
                print(vogal, end='')

                