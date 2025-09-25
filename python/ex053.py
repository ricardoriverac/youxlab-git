frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
juntar_palavras = ''.join(palavras)
inverso = ''
inverso = juntar_palavras[::-1]
print(f'O inverso de {juntar_palavras} é {inverso}')
if inverso == juntar_palavras:
    print('É um PALÍNDROMO!')
else:
    print('Não é um PALÍNDROMO!')