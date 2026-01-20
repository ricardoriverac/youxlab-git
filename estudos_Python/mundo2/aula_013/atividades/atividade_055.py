'''
Faça um programa que leia o peso de cinco pessoas. No final, mostra qual foi o maior e o menor paso lidos.
'''

#Resposta

maior = 0
menor = 1000

for c in range(0, 5):
    peso = float(input('Digite o peso da pessoa:  '))
    if peso > maior :
        maior = peso
    if peso < menor :
        menor = peso
print(f'maior peso e {maior} e o menor peso e {menor}')

    
