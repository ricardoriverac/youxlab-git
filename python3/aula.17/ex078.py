maior = 0
menor = 99999
valores = []
for cont in range (0,5):
    valores.append(int(input('Digite um valor: ')))
    for v in valores:
        if v > maior:
            maior = v
        if v < menor:
            menor = v 
print(valores)
print(f'O maior valor digitado foi {maior} que esta na posicao {valores.index(maior)}\nO menor valor foi {menor} que esta na posicao {valores.index(menor)}') 
