primeiro = float(input('Digite um valor: '))
segundo = float(input('Digite um valor: '))
terceiro = float(input('Digite um valor: '))
if primeiro - segundo < terceiro < primeiro + terceiro:
    print('É possivel formar um triângulo ')
else: 
    print('Não é possivel formar um triângulo ')