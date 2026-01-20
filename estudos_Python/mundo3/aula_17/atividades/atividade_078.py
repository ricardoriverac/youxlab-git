''' 
Faça um programa que leia 5 valores numéricos e guarde-os 
em uma lista. No final, mostre qual foi o maior e o menor 
valor digitado e as suas respectivas posições na lista. 
'''

#Resposta

lista = []
for c in range(0, 5):
    lista.append(int(input('Digite um número: ')))
    
c1 = c2 = 0
max = (max(lista))
min = (min(lista))

print(f'O maior número e {max} e as posições que ele esta:', end='') 
for c, v in enumerate(lista):      
    if v == max:
        print(f' {c}...',end='')

print(f'\nO menor número e {min}, e as posições que ele esta:' , end= '')
for c, v in enumerate(lista):      
     if v == min:
        print(f' {c}...',end='')