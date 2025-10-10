# Dicionário de cores
cores = {
    'limpa': '\033[m',
    'azul': '\033[1;34m',
    'verde': '\033[1;32m',
    'vermelho': '\033[1;31m',
    'amarelo': '\033[1;33m',
    'fundo': '\033[7;37m'
}


def titulo(mensagem, cor='limpa'):

    print(cores[cor], end='')
    print('-' * (len(mensagem) + 4))
    print(f"  {mensagem}")
    print('-' * (len(mensagem) + 4))
    print(cores['limpa'], end='')


def mostrar_ajuda(comando):
    
    titulo(f"Acessando o manual de '{comando}'", 'amarelo')
    print(cores['fundo'], end='')
    help(comando)
    print(cores['limpa'], end='')


while True:
    titulo("SISTEMA DE AJUDA PyHELP", 'azul')
    opcao = input(f"{cores['verde']}Função ou biblioteca > {cores['limpa']}").strip()
    if opcao.upper() == 'FIM':
        break
    mostrar_ajuda(opcao)

titulo("ATÉ LOGO! ", 'vermelho')