def aumentar(a=0, b=0, formato=False):
    resultado = a + (a * b / 100)
    return resultado if formato is False else reais(resultado)

def diminuir(a=0, b=0, formato=False):
    resultado = a - (a * b / 100)
    return resultado if formato is False else reais(resultado)

def dobro(a=0, formato=False):
    resultado = a * 2
    return resultado if formato is False else reais(resultado)

def metade(a= 0, formato=False):
    resultado = a / 2
    return resultado if formato is False else reais(resultado)

def reais(preco = 0, simbolo='R$'):
    return f'{simbolo}{preco:>.2f}'.replace('.', ',')

def resumo(* valores):

    print('-' * 25)
    print(f'{"RESUMO DOS VALORES":^25}')
    print('-' * 25)
    print(f'Preço analisado: {reais(preco):^25}')
    print(f'Dobro dos preços {dobro(a):^25}')
    print(f'Metade dos preços: {metade(a):^25}')
    print(f'80% de aumento: {aumentar(a, b):^25}')
    print(f'35% de redução: {diminuir(a, b):^25}')