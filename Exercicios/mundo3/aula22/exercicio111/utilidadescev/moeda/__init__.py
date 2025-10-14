def aumentar (valor = 0, taxa = 0, formato =False):
    preco = valor + (valor*taxa /100)
    return preco if formato is False else moeda(preco)

def diminuir (valor = 0, taxa = 0, formato = False):
    preco = valor - (valor*taxa / 100)
    return preco if formato is False else moeda(preco)

def dobro (valor = 0, formato =False):
    valor *= 2
    return valor if not formato else moeda(valor)

def metade (valor = 0, formato = False):
    valor /= 2
    return valor if not formato else moeda(valor)

def moeda (valor = 0, moeda = 'R$'):
    return f'{moeda}{valor}'.replace('.', ',')

def resumo (valor = 0, taxa = 10, taxa2 = 10):
    print('Resumo do valor'.center(30))
    print("  ")
    print(f'Valor recebido: {moeda(valor)}')
    print(f'Dobro do valor: {dobro(valor, True)}')
    print(f'Metade do valor: {metade(valor, True)}')
    print(f'{taxa}% de aumento no valor: {aumentar(valor, taxa, True)}')
    print(f'{taxa2}% de redução no valor: {diminuir(valor, taxa, True)}')
    print(" ")