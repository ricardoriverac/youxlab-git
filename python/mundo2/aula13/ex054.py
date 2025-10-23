#Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date
ano_atual = date.today().year
for pessoa in range(0,7):
   nasci = int(input('Digite sua data de nascimento: '))
   idade = ano_atual - nasci
   if idade >= 18:
      print('É de maior.')
   else:
    print('É de menor')
