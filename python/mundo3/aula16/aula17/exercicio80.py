lista=list()
resposta='S'
while resposta=='S':
    numero=int(input('Digite um numero: '))
    if len(lista)==0:
        lista.append(numero)
    else:
        for pos in range(len(lista)):
            if numero < lista[pos]:
                lista.insert(pos,numero)
                break
            if pos == len(lista)-1:
                lista.append(numero)
            
    resposta=str(input('Deseja continuar? S/N ')).upper()
            
print(lista)