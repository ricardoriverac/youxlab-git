numero1 = int(input('Primeiro valor: '))
numero2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('''[1]Somar
          [2]Multiplicar
          [3]Maior
          [4]Números novos
          [5]Sair do programa''')
    opcao = int(input('>>>>> Escolha uma opção: '))
    if opcao == 1:
        soma = numero1 + numero2
        print(f'A soma dos números {numero1} e {numero2} é igual a: {soma}')
    elif opcao == 2:
        multiplicacao = numero1 * numero2
        print(f'A multiplicação dos números {numero1} e {numero2} é igual a: {multiplicacao}')
    elif opcao == 3:
        maior = numero1 > numero2
        print(f'O número {numero1} é MAIOR do que o número {numero2}')
    elif opcao == 4:
        print('INforme os números novamente: ')
        num_novo = int(input('Digite o primeiro número novo: '))
        num_novo2 = int(input('Digite o segundo número novo: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente!')
    print('=-=' * 10)
print('Fim do programa! VOLTE SEMPRE!')