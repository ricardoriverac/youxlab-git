lista = []
listap = []
listai = []

while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    if n % 2 == 0 :
        listap.append(n)
    else :
        listai.append(n)
    while True:
        c = str(input('Você quer continuar? [S/N]: ')).upper()
        if c == 'S':
            break
        if c == 'N':
            break
        else:
            print ('você não digitou nenhuma das alternativas, digite novamente')
    if c == 'N':
        break
print (f'Os números digitados foram {lista}, os números pares foram {listap}, e os impares foram {listai}')