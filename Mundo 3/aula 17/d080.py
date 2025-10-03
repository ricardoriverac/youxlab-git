lista = []
for num in range(0, 5):
    numerosNumericos = int(input('-''Digite um valor: '))
    if num == 0 or numerosNumericos > lista[-1]:
        lista.append(numerosNumericos)
        print('O número foi digitado no final da lista.')
    else:
        posicao = 0
        while posicao < len(lista):
            if numerosNumericos <= lista[posicao]:
                lista.insert(posicao, numerosNumericos)
                print(f'O número foi adicionado na posição {posicao}.')
                break
            posicao += 1
print(f'Os valores digitados em ordem foram: {lista}.')

# lista = [0,8,9,7,6]
# print(len(lista))
        