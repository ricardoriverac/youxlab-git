lista = []
resposta = ''
while resposta in 'S':
    numero = int(input('Coloque aqui um número: '))
    if numero not in lista:
        lista.append(numero)
    else:
        print('Esse número existe.')
    resposta = str(input('Você quer continuar? [S/N]')).upper()
    if resposta == 'N':
        break
print(sorted(lista))