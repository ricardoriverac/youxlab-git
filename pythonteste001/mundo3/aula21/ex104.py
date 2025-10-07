def lerInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('Digite um número válido')
        if ok:
            break
    return valor


n = lerInt('Digite um valor ')
print(f'Você digitou o número {n}')