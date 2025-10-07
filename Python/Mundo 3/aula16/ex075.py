# Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

from random import randint

valores = ()

for contagem in range(4):
    numero = int(input('Digite um valor: '))
    valores = valores + (numero,)
print(valores)
print(valores.count(9))
if 3 in valores:
    print(valores.index(3))
else:
    print('Não há o valor 3')
print('Os valores pares são:')

for v in valores:
    if v % 2 == 0:
        print(v)
        
# for n in valores:
