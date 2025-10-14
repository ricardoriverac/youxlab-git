'''faça um progarma que leia a largura e a altura
 de uma parede em metros, calcule a sua área e a 
 quantidade de tinta necessária para pintá-la,
 sabendo que cada litro de tinta, pinta uma área 
 de 2m**2'''

#Responda 

alrura = float(input('Qual e altura em metros da  parede : ' ,))
largura = float(input('Qual e a largura em metros da parede : ' ,))
area = (alrura * largura)

print(f'A quantidade de tinta necessaria para pintar a parede é : {area} litros')
