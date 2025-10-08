def lerInt(msg):
    ok = False
    valor = 0
    while True:
        try:
            n = int(input(msg))
            valor = int(n)
            ok = True
        except Exception as erro:
            print(f'numero inválido,motivo do erro: {erro},tente novamente')
        if ok:
            break
    return valor


def lerFloat(msg):
    ok = False
    valor = 0
    while True:
        try:
            n = float(input(msg))
            valor = float(n)
            ok = True
        except Exception as erro:
            print(f'numero inválido,motivo do erro: {erro},tente novamente')
        if ok:
            break
    return valor

n = lerInt('Digite um valor ')
print(f'Você digitou o número {n}')
n = lerFloat('Digite um valor ')
print(f'Você digitou o número {n:.2f}')