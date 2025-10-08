import random
lista=[]
for valor in range (0,5):
    numero = int(input('Digite um valor: '))
    lista.append(numero)
print(f'O maior numero {max(lista)}')
print(f'O menor numero é {min(lista)}')
print(f'A posição do {max(lista)} é {lista.index(max(lista))}')
print(f'A posição do {min(lista)} é {lista.index(min(lista))}')