# Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. 
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista. 

valores = []
maior = 0
menor = 0
posicao = 0
posicaoMenor = 0

for cont in range(0, 5):
    valor = int(input('Digite o valor: '))
    valores.append(valor)

    if cont == 0: # cont - é igual a uma posição
        maior = valor
        menor = valor
   
    else:
        if maior < valor:   # substituição
            maior = valor
            posicao = cont

        if menor > valor:
            menor = valor
            posicaoMenor = cont
    
print(f'O maior valor é: {maior} na posição {posicao}.\nO menor valor é: {menor} na posição {posicaoMenor}.')