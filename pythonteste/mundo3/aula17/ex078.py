lista = []
maior = posicaoMaior = menor = posicaoMenor = 0
for c in range(0,5):
    lista.append(int(input(f'Forneça um valor para a posição {c + 1}: ')))
    if c == 0:
        maior = menor = lista[c]
    else:
        if lista[c] > maior:
            maior = lista[c]
        if lista[c] < menor:
            menor = lista[c]
for indice, valor in enumerate(lista):
    if lista[indice] == maior:
        posicaoMaior = indice + 1
    if lista[indice] == menor:
        posicaoMenor = indice + 1
print(f'Você forneceu os valores {lista}\nE o maior valor é {maior} e esta na posição {posicaoMaior} e o menor é {menor} e esta na posição {posicaoMenor}')
