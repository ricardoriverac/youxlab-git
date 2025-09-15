frase= str(input('Digite uma frase: ')).strip().upper()
print('A letra A aparece {} vezes na frase '.format(frase.count('A')))
print(f'A primeira letra A aparece {} na frase'.format(frase.rfind('A')))
print(f'A ultima letra A aparece {}'.format(frase.rfind('A')))
