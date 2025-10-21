def leiaInt(i=0):
    while True:
        try:
            i = int(input('Digite um número inteiro: '))
        except (ValueError, TypeError):
            print(f'\033[31mErro. Digite um número inteiro válido.\033[m')
        except KeyboardInterrupt:
            print(f'\033[31mUsuário não digitou valor.\033[m')
            return 0
        else:
            return i


def leiaFloat(r=0):
    while True:
        try:
            r = float(input('Digite um número real: '))
        except (ValueError, TypeError):
            print(f'\033[31mErro. Digite um número real válido.\033[m')
        except KeyboardInterrupt:
            print(f'\033[31mUsuário não digitou valor.\033[m')
            return 0
        else:
            return r


print(f'O número inteiro digitado foi {leiaInt()} e o real foi {leiaFloat()}')