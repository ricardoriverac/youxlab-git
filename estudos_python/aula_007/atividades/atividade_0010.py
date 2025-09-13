'''
Escreva um programa que pergunte a quantidade
de Km percorridos por um carro alugado e a 
quantidade pelos dias pelos quais ele foi 
alugagado.Calcule o preço a pagar, sabendo que 
o carro custa R$60 por dia e R$0,15 por Km rodado.
''' 

#Resposta 

quantidade_de_Km_percorrido = float(input('Qual a quantidade de Km o carro percorreu : '))
quantidade_de_dias_foi_alugado = int(input('Por quantos dias o carro foi alugado : '))
precodia = (quantidade_de_dias_foi_alugado * 60)
precokm = (quantidade_de_Km_percorrido * 0.15)

print(f'O preço a pagra pelo Km rodade e R${precokm}, e o preço a pagar pelo dia rodado e R${precodia}')

