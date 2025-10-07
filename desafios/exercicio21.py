valores = []

for cont in range(5):
    valores.append(int(input('Digite um valor: ')))

maior = max(valores)
menor = min(valores)

print(f'\nValores digitados: {valores}\n')

for i, v in enumerate(valores):
    print(f'O valor {v} está na posição {i}')

print(f'\nO menor valor é {menor} e o maior é {maior}')