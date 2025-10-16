# Exercício Python 109: Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais,
# informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.

def aumentar(preco=0, taxa=0, formatar=False):
    resp = preco + (preco * taxa / 100)
    return moeda(resp) if formatar else resp

def diminuir(preco=0, taxa=0, formatar=False):
    resp = preco - (preco * taxa / 100)
    return moeda(resp) if formatar else resp

def dobro(preco=0, formatar=False):
    resp = preco * 2
    return moeda(resp) if formatar else resp

def metade(preco=0, formatar=False):
    resp = preco / 2
    return moeda(resp) if formatar else resp

def moeda(preco=0, moeda='R$'):
    return f'{moeda} {preco:.2f}'.replace('.', ',')
