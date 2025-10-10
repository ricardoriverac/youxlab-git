numeros = []

for c in range(5):

    valor = int(input('Digite um valor: '))
    if c == 0 or valor > numeros[-1]:

        numeros.append(valor)
        print('Adicionado ao final da lista ')

    else:
        posicao = 0
        while posicao < len(numeros):
            if valor <= numeros[posicao]:

                numeros.insert(posicao, valor)
                print(f'Adicionado na {posicao} ')
                break
            posicao += 1

print(f'Os valores em ordem foi {numeros}')