numeros =[]
while True:
    n = int(input('Digite um número: '))
    if n not in numeros:
        numeros.append(n)
        print('Numero adicionado!') 
    else:
        print('Número duplicado! Não vou adicionar mais.')
        continuar = input('Quer continuar? [S/N]').strip().upper()
        if continuar == 'N':
            break
print('-=' * 30)
numeros.sort()
print(f'Você digitou os seguintes valores: {numeros}')