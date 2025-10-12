def moeda(n):
    aux = f'R${n:.2f}'.replace('.', ',')
    return aux
def dobro(num):
    r = num * 2
    return r
def metade(num):
    r = num / 2
    return r
def aumentar(num, porcent):
    r = num + (porcent/100 * num)
    return r
def diminuir(num, porcent):
    r = num - (porcent/100 * num)
    return r
def moeda(val, moeda='R$'):
    return f'{moeda}{val:.2f}'.replace('.', ',')
from mundo3.desafio107.moeda import *
def det(simb='-', comp=60):
    print(simb * comp)
det()
num = float(input('Digite um preço: R$'))
print(f'O dobro de {moeda(num)} é {moeda(dobro(num))}')
print(f'A metade de {moeda(num)} é {moeda(metade(num))}')
print(f'{moeda(num)} + 10% é {moeda(aumentar(num, 10))}')
print(f'{moeda(num)} - 10% é {moeda(diminuir(num, 10))}')
det()