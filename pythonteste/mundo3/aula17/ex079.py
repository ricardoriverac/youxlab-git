numeros = list()
while True:
    n = int(input('Forneca um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('Sucesso ao fornercer valor')
    else:
        print('Valor duplicado detectado e não adicionado')
    escolha = str(input('Quer continuar?[S/N] ')).strip().upper()[0]
    if escolha in 'N':
        break
numeros.sort()
print(f'Valores fornecidos: {numeros}')