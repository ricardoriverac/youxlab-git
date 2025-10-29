#Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa

valor1 = int(input('Escolha o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))
escolha = 1
while escolha != 5:
  print('[ 1 ] somar\n'+
        '[ 2 ] multiplicar\n'+
        '[ 3 ] maior\n'+
        '[ 4 ] novos números\n'+
        '[ 5 ] sair do programa')
  escolha = int(input('Escolha uma das opções:'))
  if escolha == 1:
   soma = valor1 + valor2
   print(f'A soma dos valores é {soma}')
  elif escolha == 2:
    multi = valor1 * valor2
    print(f'A multiplicação dos valores é {multi}')
  elif escolha == 3:
    if valor1 > valor2:
     maior = valor1
    else:
     maior = valor2
     print(f'O maior valor é {maior}')
  elif escolha == 4:
   valor1 = int(input('Digite um novo valor: '))
   valor2 = int(input('Digite um segundo valor novo: '))
  elif escolha == 5:
   print('Você saiu do programa, até a próxima!')
print('Fim do programa.')
