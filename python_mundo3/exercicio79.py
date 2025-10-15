lista = []
opção = ''

while True:
    n = int(input('Digite um valor: '))
    if n in lista:
        print ('Este valor já foi digitado')
    else:
        lista.append(n)
    o = str(input('Você deseja continuar? [S/N]: ')).upper()
    if o == 'N':
        break

lista.sort()
print (f'os valores digitados em ordem crescente é {lista}')