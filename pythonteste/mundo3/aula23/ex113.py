def lerInt(msg='0'):
    ok = False
    valor = 0
    while True:
        try:
            n = int(input(msg))
            valor = int(n)
            ok = True
        except Exception as erro:
            print(f'\033[31mnumero inválido,motivo do erro: {erro},tente novamente\033[m')
        except KeyboardInterrupt:
            print(f'\n\033[31mo usuário não quis digitar o código\033[m')
            break
        if ok:
            break
    return valor


def lerFloat(msg='0'):
    ok = False
    valor = 0
    while True:
        try:
            n = float(input(msg))
            valor = float(n)
            ok = True
        except Exception as erro:
            print(f'\033[31mnumero inválido,motivo do erro: {erro},tente novamente\033[m')
        except KeyboardInterrupt:
            print(f'\n\033[31mo usuário não quis digitar o código\033[m')
            break
        if ok:
            break
    return valor

n = lerInt('Digite um valor \033[33m')
print('\033[m')
print(f'Você digitou o número {n}')
n = lerFloat('Digite um valor \033[33m')
print('\033[m')
print(f'Você digitou o número {n:.2f}')
