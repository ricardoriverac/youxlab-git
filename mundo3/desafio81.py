lista = list()
contador = 0
while True:
    valor = int(input('digite um valor: '))
    lista.append(valor)
    contador += 1
    simounao = str(input('Quer continuar? [s/n] ')).lower().strip()
    while simounao not in 'sn':
        simounao = str(input('Quer continuar? [s/n] ')).lower().strip()
    if simounao == 'n':
        break
if contador == 1:
    print('você digitou {} elemento'.format(contador))
else:
    print('você digitou {} elementos'.format(contador))
print('os valores em ordem decrescente são {}'.format(sorted(lista , reverse=True)))
if 5 in lista:
    print('o valor 5 faz parte da lista!')

