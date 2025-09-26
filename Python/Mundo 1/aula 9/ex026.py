frase = str(input('Digite uma frase: ')).lower().strip()
print('A letra A aparece {}'.format(frase.count('a')))
print('Em que posição ela aparece pela primeira vez? {}'.format(frase.find('a')+1))
print('Em que posição ela aparece na ultima vez? {}'.format(frase.rfind('a')+1))
