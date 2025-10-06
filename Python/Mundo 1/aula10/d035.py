reta1 = float(input('Primeiro comprimento: '))
reta2 = float(input('Segundo comprimento: '))
reta3 = float(input('Terceiro comprimento: '))
if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('Os comprimentos acima FORMAM UM TRIÂNGULO!')
else:
    print('Os comprimentos acima NÃO FORMAM UM TRIÂNGULO!')
