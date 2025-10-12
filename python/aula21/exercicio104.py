def leiaInt(msg):
    ok = False
    valor = 0 
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
            print(f'\033[032mO valor {valor} é um número válido.\033[m')
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return valor

n = leiaInt('Digite um valor: ')
