lista = []
while True:
    entrada = (int(input('Digite um valor: ')))
    if entrada not in lista:
        lista.append(entrada)
        print('Número adicionado com sucesso!')
    else:
        print('ERROR:0xd07! o número já se encontra na lista..')
    perg = ' '
    while perg not in 'NS':
        perg = str(input('Deseja continuar? [S/N]')).upper()
    if perg in 'N':
        break
print('-='*30)
print(f'Você digitou os valores {sorted(lista)}.')