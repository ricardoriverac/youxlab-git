numeros = []
while True:
    valores = int(input('Digite um valor: '))
    if valores not in numeros:
        numeros.append(valores)
        print('Numero adicionado')
    else:
        print('Esse numero ja existe')
    resposta = input('quer continuar [S/N] ').upper()
    if resposta == 'N':
        break
numeros.sort
print(f'a lista com os valores que você digitou é : {numeros}')