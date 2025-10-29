frase = input('Digite uma frase: ').strip().upper()
frase_sem_espaco = frase.replace(' ', '')
inversa = frase_sem_espaco[::-1]
if frase_sem_espaco == inversa:
    print(f'A frase "{frase}" É um palíndromo!')
else:
    print(f'A frase "{frase}" NÃO é um palíndromo.')
