def LeiaInt(txt):
    valido = False
    while not valido:
        try:
            valor = int(input(txt))
            valido = True
            return valor
        except (ValueError, TypeError):
            print('\033[1;31mO Tipo do valor digitado é Inválido!\033[m')
            valido = False
        except KeyboardInterrupt:
            print('\033[1;31mO usuário decidiu não informar os dados.\033[m')
            valor = 0
            return valor

def LeiaFloat(txt):
    valido = False
    while not valido:
        try:
            valor = float(input(txt))
            valido = True
            return valor
        except (ValueError, TypeError):
            print('\033[1;31mO Tipo do valor digitado é Inválido\033[m')
            valido = False
        except KeyboardInterrupt:
            print('\033[1;31mO usuário decidiu não informar os dados.\033[m')
            valor = 0
            return valor


n_int = LeiaInt('Digite um Número Inteiro: ')
n_real = LeiaFloat('Digite um Número Real: ')
print(f'O número inteiro digitado foi {n_int}, já o número real foi {n_real}')