lista = []

while True:
    valor = int(input(f'Digite um valor:'))
    
    if valor in lista:
        print('Número repetido! Não e possivel ser adicionado!')
        break

    else: 
        lista.append(valor)
        print('Valor adicionado com sucesso....')

    continuar = (input('Quer continuar? [S/N]:')).upper().strip()
    if continuar != 'S':
        print('Encerrando...')
        break
    
print(f'\nlista final:{lista}')

