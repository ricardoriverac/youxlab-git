'''
Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores 
lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.
'''

#Resposta

dados = []
contador = 0

for c in range(0, 9):
    contador += 1
    numero = int(input(f'Digite o {contador}° número: '))
    
    dados.append(numero)
    dados.sort()

print(dados[0] , dados[1] , dados[2] )
print(dados[3] , dados[4] , dados[5] )
print(dados[6] , dados[7] , dados[8] )
    