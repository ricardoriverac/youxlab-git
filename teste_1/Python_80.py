lista = []
 
for c in range(0, 5):
    valor = int(input('Digite um valor: '))
    
    # Se for o primeiro ou maior que o último, adiciona no final
    if c == 0 or valor > lista[-1]:
        lista.append(valor)
        print(f'Adicionado na ... (posição {len(lista) - 1})')
    else:
        posicao = 0
        while posicao < len(lista):
            if valor <= lista[posicao]:
                lista.insert(posicao, valor)
                print(f'Adicionado na posição {posicao} da lista...')
                break
            posicao += 1

print('-=' * 30)
print(f'Os valores digitados em ordem foram: {lista}')
