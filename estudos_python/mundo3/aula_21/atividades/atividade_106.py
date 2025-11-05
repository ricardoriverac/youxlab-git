# Mini sistema de ajuda interativa em Python
# Utilizando cores ANSI e o sistema de help()

# Cores (usando códigos ANSI)
c = ('\033[m',         # 0 - sem cor
     '\033[0;30;41m',  # 1 - vermelho
     '\033[0;30;42m',  # 2 - verde
     '\033[0;30;43m',  # 3 - amarelo
     '\033[0;30;44m',  # 4 - azul
     '\033[0;30;45m',  # 5 - roxo
     '\033[7;30m'      # 6 - branco invertido
     )


def ajuda(com):
    """Mostra o manual de um comando ou função."""
    titulo(f'Acessando o manual do comando "{com}"', 4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')


def titulo(msg, cor=0):
    """Imprime um título colorido e centralizado."""
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')


# Programa principal
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        titulo('ATÉ LOGO!', 1)
        break
    else:
        ajuda(comando)
