numero1 = int(input('Primeiro valor: '))
numero2 = int(input('Segundo valor: '))
opçao = 0 
while opçao != 5:
    print('''[ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números 
    [ 5 ] sair do programa''')
    opçao = int(input('Qual é a sua opção? '))
    if opçao == 1: 
        soma = (numero1 + numero2)
        print('A soma entre {} + {} é {}'.format(numero1, numero2, soma))
    elif opçao == 2: 
        produto = numero1 * numero2
        print('O resultado de {} X {} é {}'.format(numero1, numero2, produto))
    elif opçao == 3: 
        if numero1 > numero2:
            maior = numero1
        else:
            maior = numero2
        print('Entre {} e {} o maior valor é {}'.format(numero1, numero2, maior))
    elif opçao == 4: 
        print('Informe os números novamente por favor:')
        numero1 = int(input('Primeiro valor: '))
        numero2 = int(input('Segundo valor: '))
    elif opçao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente')
    print('=-=' * 10)
print('Fim do programa, volte quando quiser! ')