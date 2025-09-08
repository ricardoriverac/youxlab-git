#mostre quantos reais uma pessoa possui e quantos dólares ela pode comprar

conta = float(50)
reais = str(conta) + 'R$'
cotdol = float(input('Qual a cotação atual do dólar? '))
dolares = str(conta / cotdol) + 'USD'
print('O valor presente na conta é {0} \nO usuário pode comprar {1}'.format(reais, dolares)) 

