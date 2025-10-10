# # Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma 
# # lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

valores = [[], []]

for i in range(1, 8):
    valor  = int(input(f'Digite o {i}° valor: '))

    if valor % 2 == 0:
        valores[0].append(valor)

    else:
        valores[1].append(valor)

valores[0].sort()
valores[1].sort()

print('-' * 80)
print(f'Os valores pares são: {valores[0]}')
print('-' * 80)
print(f'Os valores impares são: {valores[1]}')
print('-' * 80)


