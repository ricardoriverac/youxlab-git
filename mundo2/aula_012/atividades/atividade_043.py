'''
Desenvolva uma lógica que leia o peso e a altura de uma pessoa. calcule seu IMC a mostre seu status, de acordo com a tabala abaixo:
- Abaixo da 18.5: Abaixo do Peso
- Entre 18.5 g 25: Peso ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade mórbida
'''

#Resposta
import math

peso_do_individo = float(input('Digite o seu  peso em kg: '))
altura_do_individo = float(input('Digite a sua altura em metros: '))

calculo = math.pow(altura_do_individo , 2)
calculo2 = peso_do_individo / calculo

if calculo2 < 18.5 :
    print('Você esta abaixo do peso!!')

elif calculo2 >= 18.5 and calculo2 < 25:
    print('Você esta no peso ideal!!')

elif calculo2 >= 25 and calculo2 < 30 :
    print('Você esta com sobrepeso')

elif calculo2 >=30 and calculo2 <= 40 :
    print('Você esta com obesidade!!')

elif calculo2 > 40 :
    print('Você esta com obesidade mórbida!!')