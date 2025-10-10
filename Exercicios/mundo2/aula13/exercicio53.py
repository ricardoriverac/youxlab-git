frase = str(input('Digite uma frase: ')).strip().upper()
sem_espaco = frase.split()
frase_junta = ''.join(sem_espaco)
inverso = ''
for letra in range(len(frase_junta)-1, -1, -1):
    inverso += frase_junta[letra]
if inverso != frase_junta:
    print(f'A frase: {frase} não é um Palíndromo, pois ')
    print(f'{frase_junta} é diferente de {inverso}')
else:
    print(f'A frase: {frase} é um Palíndromo, pois')
    print(f'{frase_junta} é igual a {inverso}')