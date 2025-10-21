frase = str(input('Digite uma frase: ')).strip()
frase2 = frase.lower().replace(" "," ")
fraseinvertida = frase2 [::-1]
if frase2 == fraseinvertida:
    print(f'A frase {frase} é um pálindromo')
else:
    print(f'A frase {frase} nao é um pálindromo')