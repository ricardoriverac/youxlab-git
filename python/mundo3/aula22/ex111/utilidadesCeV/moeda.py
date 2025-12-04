def metade(n, formatar=False):
    calculo_metade = n / 2
    return moeda(calculo_metade) if formatar else calculo_metade

def dobro(n, formatar=False):
    res = n * 2
    return moeda(res) if formatar else res

def aumentar(n, formatar=False):
    novo_valor = n * 1.1
    return moeda(novo_valor) if formatar else novo_valor

def diminuir(n, formatar=False):
    novo_valor = n * 0.87
    return moeda(novo_valor) if formatar else novo_valor

def moeda(n):
    return f'R${n:.2f}'.replace('.', ',')

def resumo(valor):
    print('-----RESUMO------')
    print(f'A metade do valor é:R${metade(valor)}')
    print(f'O dobro do valor é:{dobro(valor)}')
    print(f'Com o aumento de 10%, o valor é:{aumentar(valor)}')
    print(f'Com o reduzimento de 13%, o valor é:{diminuir(valor)}')




