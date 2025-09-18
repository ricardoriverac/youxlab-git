frase=str(input('Digite uma frase: ')).strip().replace(" ", '')
fraseInvertida= frase[::-1]
fraseFinal= ''.join(fraseInvertida)
print(fraseFinal)
if fraseFinal == frase:
    print(str('Temos um palíndromo! '))
else:
    print(str('Não temos um palíndromo! '))