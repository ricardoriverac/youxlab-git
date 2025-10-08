'''
Desenvolva um programa que leia seis números inteiros e mostre a soma 
apenas daqueles que foram pares. Se o valor digitado for impar. desconsidere-o.
'''

#Resposta

n = 0
soma = 0

for c in range(1, 7):
    n = n +1
    
    digite = int(input(f'Digite o {n}° número: '))
    if digite % 2 == 0 :
        soma = soma + digite
print(f'A soma de todos os números e {soma}')
