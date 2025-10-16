def resumo(preço, k, z):   
    
    print('-' * 15)
    print('RESUMO DO VALOR')
    print('-' * 15)
    
    
    def metade(a = 0, formato = False):
        c = a / 2
        return c if formato is False else virgula(c)


    def dobro(a = 0, formato = False):
        c = a * 2
        return c if formato is False else virgula(c)


    def aumento(a = 0, b = 1, formato = False):
        c = a * b / 100
        s = c + a
        return s if formato is False else virgula(s)


    def diminuir(a = 0, b = 1, formato = False):
        c = a * b / 100
        s = a - c
        return s if formato is False else virgula(s)


    def virgula(a = 0, formato = False):
        c = (f'{a:.2f}'.replace('.', ','))
        return c if formato is False else virgula(c)
    
    
    print(f'Preço analisado: R${virgula(preço)}')
    print(f'Dobro do preço: R${virgula(dobro(preço))}')
    print(f'Metade do preço: R${virgula(metade(preço))}')
    print(f'{k}% de aumento: R${virgula(aumento(preço, k))}')
    print(f'{z}% de redução: R${virgula(diminuir(preço, z))}')


import moeda
import dado
p = dado.leiaDinheiro('Digite o preço: R$50')
moeda.resumo(p, 35, 22)