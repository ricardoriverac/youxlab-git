numeros = []

for numero in range(0, 5):
    novoNumero = int(input(f'Digite um número: '))

    if numeros == []:
        print('Número adicionado no final da lista.')
        numeros.append(novoNumero)

    else:
        for i, v in enumerate(numeros):
            if novoNumero < v:
                print(f'O número foi adicionado na posição {i}.')
                numeros.insert(i, novoNumero)
                break

        if novoNumero > v:
            print('Número adicionado no final da lista.')
            numeros.append(novoNumero)

print(f'Os valores que você digitou em ondem foram \033[33m{numeros}\033[m.')