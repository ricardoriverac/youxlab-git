distância = float(input('Qual a distância da sua viagem? '))
print(f'Você irá começar uma viagem de {distância}Km.')
if distância <=200:
    preço = distância * 0.50

else:
    preço = distância * 0.45
print(f'E o preço da sua passagem sera de R${preço : .2f}')