#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólar ela pode comprar. 

#Resposta

quantia_de_dinheiro = float(input('Qual a sua quantia de dinheiro : '))
valor_do_dolar = (quantia_de_dinheiro / 5.39)

print(f'A quantidade de diheiro na carteira atualmente  e {quantia_de_dinheiro}R$, e a quantia de dolar que podera comprar e  {valor_do_dolar}US$')