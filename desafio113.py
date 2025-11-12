def leiaInt(msg):
    """
    -> Lê um número inteiro do teclado, validando a entrada.
    :param msg: Mensagem exibida ao usuário.
    :return: Valor inteiro digitado pelo usuário.
    """
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return n


def leiaFloat(msg):
    """
    -> Lê um número real (float) do teclado, validando a entrada.
    :param msg: Mensagem exibida ao usuário.
    :return: Valor float digitado pelo usuário.
    """
    while True:
        try:
            n = float(input(msg).replace(',', '.'))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número real válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mEntrada de dados interrompida pelo usuário.\033[m')
            return 0.0
        else:
            return n
