frase = str(input('Digite uma frase: ')).strip().upper().split()
junta = ''.join(frase)
inverso = ''
for letra in range(len(junta) - 1, -1, -1):
    inverso += junta[letra]
print(inverso)
print(f'{junta}')
if inverso == junta:
    print('\033[33mEle é um palíndromo')
else:
    print('\033[31mEle não é um palíndromo')

