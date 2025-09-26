reta1 = float(input('Digite o tamanho da primeira reta: '))
reta2 = float(input('Digite o tamanho da segunda reta: '))
reta3 = float(input('Digite o tamanho da terceira reta: '))
if reta1 + reta3 > reta2 and reta2 + reta3 > reta1:
    print('É possível termos um triângulo.')
if reta1 + reta2 < reta3:
    print('Não é possível termos um triângulo.')