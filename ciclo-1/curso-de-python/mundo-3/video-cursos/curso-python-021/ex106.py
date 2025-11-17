from time import sleep

def ajuda(comando):
    print(f'\033[0;30;44mProcuando o comando \'{comando}\' no manual...\033[m')
    print('\033[0;30;43m', end='')
    help(comando)
    print('\033[m', end='')
    sleep(2)

def titulo(mensagem):
    tamanhoPalavra = len(mensagem) + 2
    print('\033[0;30;42m', end='')
    print('~' * tamanhoPalavra)
    print(f' {mensagem}')
    print('~' * tamanhoPalavra)
    print('\033[m', end='')
    sleep(1)


#Código Principal
comando = ''
while True:
    titulo('SISTEMA DE AJUDA EM PYTHON ')
    comando = str(input('Código > '))
    if comando.upper() == 'FIM':
        break

    else:
        ajuda(comando)
titulo('\033[0;30;41mATÉ A PRÓXIMA!\033[m')