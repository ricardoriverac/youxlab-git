def leiaInt(leia):
    n = input(Leia)
    while not n.isnumeric():
        print('\033[31mErro! Digite um número inteiro válido\033[0;0m')