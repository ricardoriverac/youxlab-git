reta1 = int(input('Digite o valor da primeira reta: '))
reta2 = int(input('Digite o valor da segunda reta: '))
reta3 = int(input('Digite o valor da terceira reta: '))
if reta1 == reta2 and reta2 == reta3 and reta1 == reta3:
    print('Todos os lados são iguais, teremos um triângulo Equilátero.')
elif reta1 == reta2 or reta2 == reta3:
    print('Apenas 2 lados são iguais, teremos um triângulo Isóceles.')
elif reta1 != reta2 and reta2 != reta3 and reta1 != reta3:
    print('Nenhum dos lados são iguais, teremos um triângulo Escaleno.')