'''
Crie um programa que tenha uma tupla com várias palavras (não usar acentos). 
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
'''

#Resposta
vo = 0
palavras = (
    str(input('Digite a 1° palavra sem acentos: ')),
    str(input('Digite a 2° palavra sem acentos: ')),
    str(input('Digite a 3° palavra sem acentos: ')),
    str(input('Digite a 4° palavra sem acentos: ')),
    str(input('Digite a 5° palavra sem acentos: '))
)

for p in palavras:
    vogais = 'aeiou'
    print(f"Na palavra {p} temos: ", end=' ')
    for vogal in p:
        if vogal in vogais:
            print(f' {vogal} -> ', end='')

    print()

