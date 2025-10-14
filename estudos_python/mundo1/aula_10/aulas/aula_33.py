'''
Faça um programa que leia três números e mostra qual é o maior a qual é o menor.
'''

#Resposta 

a = int(input('Digite o 1° número: '))
b = int(input('Digite o 2° número: '))
c = int(input('Digite o 3° número: '))

#Verificando número menor

if a<b and a<c:
 menor = a

if b<a and b<c :
 menor = b

if c<a and c<b :
 menor = c

print(f'Esse e o MENOR número: {menor}')

#Verificando número maior

if a>b and a>c :
 maior = a

if b>a and b>c :
 maior = b

if c>a and c>b:
 maior = c

 print(f'Esse e o MAIOR  número: {maior}')