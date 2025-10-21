velo = float(input('Qual é a sua velocidade? '))
limite = 80
ex_velocidade = velo - limite
multa = 7 * ex_velocidade
if velo > limite:
    print(f'Você ultrapassou o limite permitido de {limite} KM e vai te que pagar R${multa}')
else:
    print('Você ta dentro do limite permitido')
