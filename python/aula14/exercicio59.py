from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('=-='*10, '''\n[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
''')
    opcao = int(input('>>>>> Qual sua opção? '))
    if opcao == 1:
        soma = n1 + n2
        print(f'{soma}')
    elif opcao == 2:
        produto = n1 * n2
        print(f'{produto}')
    elif opcao == 3:
        if n1 > n2:
            maior = n1
            print(f'{n1}')
        else:
            print(f'{n2}')
    elif opcao == 4:
        print('informe os números novamente.')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Até mais!')
    else:
        print('Opção inválida. Tente novamente!')
    sleep(1)
    print('=-='*10)
print('Acabou')