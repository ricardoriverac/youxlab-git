#confirmar = ' '
    #while confirmar not in 'SN':
     #   confirmar = str(input('quer continuar?[S/N]')).strip().upper()[0]
    #if confirmar == 'N':
     #       break
     

numeros = []
confimar=''
while confimar != 'N':
    num=int(input('Digite um valor: '))
    numeros.append(num)
    confimar=str(input('Quer continuar? S/N ')).strip().upper()
print(f'{numeros}')

