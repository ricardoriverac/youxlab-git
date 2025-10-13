lista = []
quantos = 0

while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    quantos += 1
    while True:
        continuar = str(input('Você deseja continuar? [S/N]: ')).upper()
        if continuar == 'S':
            break
        if continuar == 'N':
            break
        else:
             print ('Você não digitou nenhuma das opções')
    if continuar == 'N':
            break

lista.sort(reverse=True)
print (f'Você digitou {quantos} números, e a ordem decrescente deles são {lista}')
if 5 in lista:
    print ('O número 5 esta na lista')