count=0
maior=0
meio=0
numero=0
menor=9999
lista=list()
for c in range (0, 5+1):
    Usuario=int(input('Escolha um valor: '))
    print('Valor adicionado com sucesso...')
    lista.append(Usuario)
    if maior< Usuario:
        maior=Usuario
        print('Adicionado ao final da lista')
    elif menor> Usuario:
        print('Adicionado na posição 0 da lista')
        menor=  Usuario
    elif Usuario > menor and Usuario < maior:
        numerosVariados = Usuario
        count+=1
        if Usuario < numerosVariados:
            count-=1
        print(f'Adicionado na posição {count} da lista')

listaOrdenada= sorted(lista)
print(f'Os valores digitados em ordem foram: {listaOrdenada} ')
   