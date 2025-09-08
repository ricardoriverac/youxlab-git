#programa que lê a altura e a largura de uma parede em metros, calucla sua área e a quantidade de tinta necessária para pinta-lá
#considerando que cada 1L de tinta pinta uma área de 2m² da parede

altura = float(input('Digite um valor: '))
largura = float(input('Digite um valor: '))
area = (altura * largura)
qntdtinta = area/2
print('{0} \n{1} \n{2} \n{3}'.format(altura, largura, area, qntdtinta))
