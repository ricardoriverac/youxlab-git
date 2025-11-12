def leiaInt(msg):
    """
    -> Lê um número inteiro, validando a entrada.
    :param msg: mensagem a ser exibida no input
    :return: valor inteiro digitado pelo usuário
    """
    while True:
        n = input(msg)
        if n.isnumeric():
            return int(n)
        else:
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}.')
