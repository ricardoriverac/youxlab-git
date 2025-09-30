lista = []
for c in range(0,5):
    numero = int(input('Digite um numero: '))
    if c == 0:
        lista.append(numero)
        print('O numero foi adicionado no final da lista ')
    else:
        for p in range(len(lista)):
            if numero in lista:
                break
            if numero <= lista[p]:
                lista.insert(p,numero)
                print(f'O numero {numero} foi adicionado a {p+1} posicao')
            elif p == len(lista)-1:
                lista.append(numero)
                print('O numero foi adicionado no final da lista')             
    print(lista) 
print(f'final : {lista}') 
