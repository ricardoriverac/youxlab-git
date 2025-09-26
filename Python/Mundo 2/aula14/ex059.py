opcao = 0
valor1 = int(input('Digite um valor: '))
valor2 = int(input('Digite outro valor: '))
while opcao != 5:
    print(''' Siga o MENU abaixo: 
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NÚMEROS
    [5] SAIR DO PROGRAMA''')
    opcao = int(input())
    if opcao == 1:
        soma = valor2 + valor1
        print(f'A soma dos valores é igual a {soma}.')
    elif opcao == 2:    
        multiplica = valor2 * valor1
        print(f'A multiplicação dos valores é {multiplica}.')
    elif opcao == 3:
        if valor1 >= valor2:
            print(f'O maior valor é {valor1}.')
        else:
            print(f'O maior valor é {valor2}.')
    elif opcao == 4:
        valor1 = int(input('Digite um novo valor: '))
        valor2 = int(input('Digite o outro novo valor:'))