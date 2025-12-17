def leiaDinheiro(msg):
    """
    -> Lê um valor monetário, validando a entrada.
    :param msg: Mensagem exibida ao usuário.
    :return: Valor numérico (float) correspondente ao preço.
    """
    while True:
        entrada = str(input(msg)).strip().replace(',', '.')
        if entrada == '':
            print('\033[31mERRO: O campo não pode ficar vazio!\033[m')
            continue
        try:
            valor = float(entrada)
            if valor < 0:
                print('\033[31mERRO: O valor não pode ser negativo!\033[m')
            else:
                return valor
        except ValueError:
            print(f'\033[31mERRO: "{entrada}" não é um valor monetário válido!\033[m')
