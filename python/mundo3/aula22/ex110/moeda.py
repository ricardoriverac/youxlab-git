def metade(n):
    calculo_metade = n / 2
    return calculo_metade

def dobro(n):
    return n*2

def aumento(n):
    novo_valor = n * 1.1
    return novo_valor

def diminuir(n):
    novo_valor = n * 0.87
    return round(novo_valor, 2)

def resumo(valor):
    print('-----RESUMO------')
    print(f'A metade do valor é:R${metade(valor)}')
    print(f'O dobro do valor é:{dobro(valor)}')
    print(f'Com o aumento de 10%, o valor é:{aumento(valor)}')
    print(f'Com o reduzimento de 13%, o valor é:{diminuir(valor)}')


