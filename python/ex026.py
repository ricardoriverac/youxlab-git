frase = str(input('Digite uma frase: '))
print('A letra a aparece {} vezes na frase.'.format(frase.count('a')))
print('A primeira letra A aparece na posição. {}'.format(frase.find('a')+1))
print('A última letra A aparece na posição.{}'.format(frase.rfind('a')+1))