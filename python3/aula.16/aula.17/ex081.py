continuar = 'S'
lista = []
while continuar not in 'N':
    lista.append(int(input('Digite um numero: ')))
    print(lista)
    continuar = str(input('Deseja continuar [S/N]? '))
    if continuar == 'n':
        break
print(f'O numero 5 esta na {(lista.index(5))} posicao')
print(f'foram digitados {len(lista)} numeros ')
print(f'A ordem decrescente desses numeros é {sorted(lista,reverse=True)}')

