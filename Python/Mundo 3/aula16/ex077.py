# Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos). 
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
palavras = ('amor','frase','ceu','gloss','instagram')

for c in palavras:
    print(f'As palavras são:{palavras}')
    print(c)

    for vogais in c:
        
        if vogais.lower() in 'a,e,i,o,u':
            print(f'As vogais são: {vogais}')
    

