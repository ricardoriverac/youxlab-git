# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.


minha_lista =[]
for c in range(5):
    valores_nume = int(input('Digite um valor: '))
    minha_lista.append(valores_nume)
print(f'A lista dos valores digitados são: {minha_lista}')
maior_num = max(minha_lista)
menor_num = min(minha_lista)
print(f'O maior número digitado é {maior_num}, e o menor é {menor_num}')
for c, v in enumerate(minha_lista):
    print(f'Na posição {c} temos o valor {v}.')