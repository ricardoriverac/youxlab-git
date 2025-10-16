''' 
Faça um programa que leia 5 valores numéricos e guarde-os 
em uma lista. No final, mostre qual foi o maior e o menor 
valor digitado e as suas respectivas posições na lista. 
'''

#Resposta
maior = 0
menor = 100000
lista = []
for c in range(0, 5):
    lista.append(int(input('Digite um número: ')))
    if lista < maior:
        maior = lista
    elif lista > menor:
        menor = lista

print(lista)
print(maior)
print(menor)