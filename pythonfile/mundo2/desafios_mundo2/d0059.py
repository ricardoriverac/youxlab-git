valor = int(input('Digite o primeiro valor'))
valor2 = int(input('Digite o segundo valor'))
opcao = 0
while opcao != 5:

    print('''   [1] somar
    [2] multiplicar
    [3] maior
    [4] novos numeros
    [5] sair do programa''')
    opcao = int(input('Qual é a sua opção? '))
    if opcao == 1:
        soma = valor + valor2
        print(f'A soma de {valor} e {valor2} é {soma}')
    elif opcao == 2:
        produto = valor * valor2 
        print(f'A multiplicação de {valor} e {valor2} é {produto}')
    elif opcao == 3:
        if valor > valor2:
            maior = valor
        else:
            maior = valor2
        print(f'Entre {valor} e {valor2} o maior é {maior}')
    elif opcao == 4:
        print('Informe os numeros novamente: ')
        valor = int(input('Primeiro valor: '))
        valor2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando')
    else:
        print('Opção invalida. Tente novamente')
print('Fim do programa')