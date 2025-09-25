import re
def verificar_palindromo(frase):
    frase_processada = re.sub(r'[^a-z0-9]', '', frase.lower())
    frase_invertida = frase_processada[::-1]
    if frase_processada == frase_invertida:
        print(f'"{frase}" é um palíndromo!')
    else:
        print(f'"{frase}" não é um palíndromo.')
