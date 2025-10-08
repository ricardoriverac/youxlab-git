valor1 = int(input('Digite um valor: '))
valor2 = int(input('Digite outro valor: '))
escolhaUsuario = 0

while escolhaUsuario != 5:
    print('-' * 20)
    print(f'O que você deseja fazer com os valores {valor1} e {valor2}')
    print('[1] Somar')
    print('[2] Multiplicar')
    print('[3] Maior')
    print('[4] Novos Números')
    print('[5] Sair do programa')

    escolhaUsuario = int(input('Escolha uma das 5 opções: '))
    if escolhaUsuario == 1:
        print(f'A soma entre o número {valor1} e {valor2} resulta em {valor1 + valor2}' )

    if escolhaUsuario == 2:
        print(f'A multiplicação do número {valor1} e o {valor2} resulta em {valor1 * valor2}')

    if escolhaUsuario == 3:
        maior = valor1
        if valor2 > valor1:
            maior = valor2
        print(f'Entre o número {valor1} e {valor2} o maior é o número {maior}')

    if escolhaUsuario == 4:
        valor1 = int(input('Digite um novo valor: '))
        valor2 = int(input('Digite um novo outro valor: '))