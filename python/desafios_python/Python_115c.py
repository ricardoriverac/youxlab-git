def leiaInt(mensagem):
    while True:
        try:
            numero = int(input(mensagem))
        except (ValueError, TypeError):
            print('\033[31m ERRO: por favor, digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mUsuário preferiu não digitar esse número/\033[m')
            return 0
        else:
            return numero

def linha(tamanho = 42):
    return '-' * tamanho


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def menu(lista):
    cabecalho('MENU PRINCIPAL')
    conta = 1
    for item in lista:
        print(f'\033[33m{conta}\033[34m{item}\033[m')
        opcao = leiaInt('\033[32mSua Opção: \033[m')
        return opcao