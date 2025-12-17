from time import sleep
c = ('\033[m',
     '\033[0;30;41m',
     '\033[0;30;42m',
     '\033[0;30;43m',
     '\033[0;30;44m',
     '\033[0;30;45m',
     '\033[7;30m'
     )


def ajuda(com):
    """Mostra o manual de ajuda do comando ou função digitada."""
    título(f"Acessando o manual do comando '{com}'", 4)
    sleep(1)
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    sleep(1)


def título(msg, cor=0):
    """Exibe um título colorido."""
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')
comando = ''
while True:
    título('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input('Função ou Biblioteca > ')).strip().lower()
    if comando == 'fim':
        break
    else:
        ajuda(comando)
título('ATÉ LOGO!', 1)