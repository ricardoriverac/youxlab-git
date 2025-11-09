from time import sleep

cor = ('\033[m',
       '\033[0;30;41m',
       '\033[0;30;42m',
       '\033[0;30;43m',
       '\033[0;30;44m',
       '\033[0;30;45m',
       '\033[7;30m'
       )


def ajuda(comando):
    titulo(f'Acessando o manual do comando \' {comando}\'', 4)
    print(cor[6], end=' ')
    help(comando)
    print(cor[0], end=' ')
    sleep(2)

def titulo(mensagem,cor=0):
    tamanho = len(mensagem) + 4
    print('~' * tamanho)
    print(f'{mensagem}')
    print('~' * tamanho)
    print(cor[0], end=' ')

comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP')
    comando = str(input("Função ou Biblioteca >"))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
        titulo('ATÉ LOGO',1)