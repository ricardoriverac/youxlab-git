from time import sleep
cores = ('\33[m',           #0 sem cor
        '\33[30;41m',       #1 vermeho
        '\33[33;44m',       #2 amarelo com fundo azul
        '\33[35;43m',       #3 roxo com fundo amarelo
        '\33[30;42m',       #4 branco com fundo verde
        '\033[7m')        #5 inverso


def title(text, cor=0):
    tamanho = len(text) + 4
    print(cores[cor], end='')
    print('~' * tamanho)
    print(f'  {text}')
    print('~' * tamanho)
    print(cores[0])


def pyhelp():
    while True:
        title('SISTEMA DE AJUDA PyHELP', 4)
        resp = str(input('Função ou Biblioteca> ')).lower().strip()
        if resp == 'quit':
            title('Obrigado por usar PyHELP', 1)
            sleep(1)
            break
        else:
            title(f'Carregando função {resp}', 2)
            sleep(1)
            print(cores[5])
            help(resp)
            print(cores[0])



pyhelp()