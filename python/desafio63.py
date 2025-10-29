while True:
    num = int(input('Digite um número para calcular seu fatorial (ou 0 para sair): '))
    if num == 0:
        print('Programa encerrado. Até mais!')
        break
    fatorial = 1
    for i in range(1, num + 1):
        fatorial *= i
    print(f'O fatorial de {num} é {fatorial}.\n')
    # Pergunta se quer calcular outro fatorial
    continuar = input('Deseja calcular o fatorial de outro número? [S/N]: ').strip().upper()
    if continuar != 'S':
        print('Programa encerrado. Até mais!')
        break
