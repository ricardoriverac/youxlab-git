#prog. que lê uma frase e diz quantaz vezes aparece a letra 'A', em que posição ela aparece pela primeira vez e em que posição ela aparece a última vez
frase = str(input('Digite a frase: ')).upper().strip()
print('{}'.format(frase.count('A')))
print('{}'.format(frase.find('A'))) #colocar o +1 após o find alterará a posição do elemento, somando 1
print('{}'.format(frase.rfind('A')))