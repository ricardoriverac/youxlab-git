'''
Faça um programa que calcule a soma entre todos os números impares 
que são múltiplos de três e que se encontram no intervalo de 1 até 500.
'''

#Resposta

soma = 0

for c in range(3, 500, 3):
    soma = soma + c
print(f'A soma de todas as somas é: {soma}')