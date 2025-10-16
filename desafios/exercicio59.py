numero1 = int(input('Digite um numero: '))
numero2 = int(input('Digite mais um numero: '))
opcao = 0
while opcao != 5:
    print('''   [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior 
    [ 4 ] novos numeros
    [ 5 ] sair do programa''')
    opcao = int(input(' Qual e a sua opcao? '))
    if opcao == 1:
       soma = numero1 + numero2
       print(f'A soma entre {numero1} + {numero2} = {soma}')
    elif opcao == 2:
        produto = numero1 * numero2
        print(f'A soma entre {numero1} x {numero2} = {produto}')
    elif opcao == 3:
        if numero1 > numero2:
            maior = numero1
        else:
            maior = numero2
            print(f'Entre {numero1} e {numero2} o maior valor é {maior}')
    elif opcao == 4:
        print('Informe o numero novamente:')
        numero1 = int(input('Primeiro valor: '))
        numero2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opcao invalida, tente novamente ')
    print('=-=' * 20)
print('Fim do programa. volte sempre! ')