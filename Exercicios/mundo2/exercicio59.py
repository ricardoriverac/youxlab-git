import math
valor1=int(input("Digite o primeiro valor: "))
valor2=int(input("Digite o segundo valor: "))
opcao=0

while opcao != 5:
    print('''
    [1] somar
    [2] multiplicar 
    [3] maior
    [4] novos numeros 
    [5] sair do programa''')
    opcao = int(input('-> Qual é sua opção: '))
    if opcao == 1:
        soma = valor1 + valor2
        print(f"A soma entre {valor1} + {valor2} é {soma}")
    elif opcao == 2:
        produto = valor1 * valor2
        print(f"O resultado de {valor1} x {valor2} é {produto}")
    elif opcao == 3: 
        if valor1 > valor2:
            maior = valor1
        else:
            maior = valor2
        print(f"Entre {valor1} e {valor2} o maior é {maior}")    
    elif opcao == 4:
        print("Informe os numero novamente: ")
        valor1 = int(input("Digite o primeiro valor: "))
        valor2 = int(input("Digite o segundo valor: "))
    elif opcao == 5:
        print("Finalizado!") 