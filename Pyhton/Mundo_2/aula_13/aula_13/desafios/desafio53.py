frase = str(input('Escreva uma frase para saber se ela é ou não é palíndromo: ')).strip().upper()
frsc = frase.split()
frac = ''.join(frsc)
contrario = ''
for c in range(len(frac) -1, -1, -1):
    contrario += frac[c]
print (frac, contrario )
if contrario == frac :
    print ('Essa frase é um palídromo!')
else:
    print('Essa frase não é um palídromo!')