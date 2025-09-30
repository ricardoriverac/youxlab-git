número1 = int(input('Primeiro valor: '))
número2 = int(input('Segundo valor: '))
print('{:=^50}'.format(' O que deseja fazer? '))
print('[ 1 ] somar\n[ 2 ] multiplicar\n[ 3 ] maior\n[ 4 ] novos números\n[ 5 ] fechar programa')
opção = int(input('qual opção você escolherá? '))
if opção == 1:
      soma = número1 + número2
      print('=' * 30)
      print(f'a soma de {número1} e {número2} é {soma}')
      print('=' * 30)
if opção == 2:
      multiplicação = número1 * número2
      print('=' * 30)
      print(f'a multiplicação de {número1} por {número2} é {multiplicação}')
      print('=' * 30)
if opção == 3:
      numero1maior = número1 + 1
      numero2maior = número2 + 1
      print('=' * 30)
      print(f'os valores agora são respectivamente {numero1maior} e {numero2maior}')
      print('=' * 30)
if opção == 4:
      número1 = int(input('Novo primeiro valor: '))
      número2 = int(input('Novo segundo valor: '))
while opção == 1 or opção == 2 or opção == 3 or opção == 4:
      print('{:=^50}'.format(' O que deseja fazer? '))
      print('[ 1 ] somar\n[ 2 ] multiplicar\n[ 3 ] maior\n[ 4 ] novos números\n[ 5 ] fechar programa')
      opção = int(input('qual opção você escolherá? '))
      if opção == 1:
            soma = número1 + número2
            print('=' * 30)
            print(f'a soma de {número1} e {número2} é {soma}')
            print('=' * 30)
      if opção == 2:
            multiplicação = número1 * número2
            print('=' * 30)
            print(f'a multiplicação de {número1} por {número2} é {multiplicação}')
            print('=' * 30)
      if opção == 3:
            numero1maior = número1 + 1
            numero2maior = número2 + 1
            print('=' * 30)
            print(f'os valores agora são respectivamente {numero1maior} e {numero2maior}')
            print('=' * 30)
      if opção == 4:
            número1 = int(input('Novo primeiro valor: '))
            número2 = int(input('Novo segundo valor: '))
print('\033[31mprograma fechado\033[m')