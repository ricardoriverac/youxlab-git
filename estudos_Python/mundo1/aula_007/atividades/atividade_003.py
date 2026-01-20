#Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimitros 

#Resposta

Valor_em_metros = float(input('Qual o valor em metros : '))
centimetros = (Valor_em_metros / 100 )
milimetros = (centimetros / 1000)

print(f'\nO valor de {Valor_em_metros}m em centimetros e equivalente a  {centimetros}cm e em milimitros e {milimetros}mm')

