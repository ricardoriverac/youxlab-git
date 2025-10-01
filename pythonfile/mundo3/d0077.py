nomes = ('carro', 'elefante', 'avestruz', 'bicicleta')

for n in nomes:

    print(f'\nem {nomes} tem ', end ='  ')
    for caractere in n:
        if caractere.lower() in 'aeiou':
            print(caractere, end ='')