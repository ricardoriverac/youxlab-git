def lerInt(msg='0'):
    ok = False
    valor = 0
    while True:
        try:
            n = int(input(msg))
            valor = int(n)
            ok = True
        except Exception:
            print(f'\033[31mopção inválida,tente novamente.\033[m',end= '')
            break
        if ok:
            break
    return valor


def linha(tamanho=43):
    return '\033[34m=\033[m' * tamanho


def cabeçalho(txt='\033[35mSISTEMA v1.0.1a\033[m'):
    print(linha())
    print(txt.center(43))
    print(linha())


def menu(lista):
    cabeçalho('\033[35mMENU\033[m')
    c = 1
    for item in lista:
        print(f'\033[32m{c}\033[m - {item}')
        c += 1
    print(linha())
    opc = lerInt('Sua opção: \033[32m')
    return opc