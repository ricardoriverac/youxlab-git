numero1 = int(input('Digite o primeira valor '))
numero2 = int(input('Digite o segundo valor '))
opcao = 0
soma = numero1 + numero2 
multiplicacao = numero1 * numero2
while opcao != 5:
    print(''' [1] somar
          [2] multiplicar
          [3] maior
          [4] novos numeros
          [5] antecessor e sucessor
          [6] sair do programa''')
    opcao = int(input('Qual é a sua opcao? '))
    if opcao == 1:
     print(f'A soma de {numero1} e {numero2} é {soma}')
    elif opcao == 2:
       print(f'A multiplicacao dos numeros {numero1} e {numero2} é {multiplicacao}')
    elif opcao == 3:
       maior = numero1 > numero2 and numero2 > numero1
       print(f'Entre os numeros {numero1} e o {numero2} o maior é {maior}')
    elif opcao == 4:
       print('Informe os valores novamente  ')
       numero1 = int(input('Digite outro valor '))
       numero2 = int(input('Digite o segundo valor '))
    elif opcao == 5:
       antecessor = numero1 - 1
       sucessor = numero1 + 1
       antecessor2 = numero2 - 1
       sucessor2 = numero2 + 1
       print(f'{numero1} seu antecessor é {antecessor} e seu sucessor é {sucessor}\n {numero2} seu sucessor é {sucessor2} e seu antecessor é {antecessor2}')
    elif opcao == 6:
       print('Fim do programa!volte sempre!')