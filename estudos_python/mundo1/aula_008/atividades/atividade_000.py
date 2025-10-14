#Faça um codigo que leia um número e caucule a raiz quadrada do número 

#Resposta

from math import trunc , sqrt

numero_digitado = float(input('Digite um número : '))
raiz_quadrada = sqrt(numero_digitado)

print(f'A raiz quadrada de {numero_digitado} e equivalente a  {trunc(raiz_quadrada)}')
