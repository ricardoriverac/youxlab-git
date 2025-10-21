frase = str(input('Digite uma frase: ')).strip().upper()
letra = frase.count('A')
posi = frase.find ('A')+1
ult = frase.rfind ('A')+ 1
print(f'A letra A aparece: {letra} vezes na frase: {frase}')
print(f'A letra A aparece pela primeira vez em {posi}')
print(f'Pela ultima vez em: {ult}')