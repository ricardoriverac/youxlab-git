def monetario(mo):
    mo = f'R${round(mo)},00'
    return mo
    
    
def metade(p, m=True):
    p = p / 2
    if m is not False:
       return monetario(p)
    else:
       return p
        
        
def dobro(p, m=True):
    p= p * 2
    if m is not False:
       return monetario(p)
    else:
       return p
        
        
def aumentar(p, aumentar, m=True):
    p = p * (1+ aumentar/100)
    if m is not False:
      return  monetario(p)
    else:
        return p
def diminuir(p, m=True):
    p= p * 0.87
    if m is not False:
       return  monetario(p)
    else:
        return p

def resumo(p,aumenta=0, diminuir=0):
    print('-'* 40)
    print('RESUMO DO VALOR'.center(40))
    print('-'*40)
    print(f'Preço analisado:  {p}')
    print(f'O dobro do preço: {dobro(p, True)}')
    print(f'A metade do preço: {metade(p, True)}')
    print(f'{aumenta}% de aumento: {aumentar(p, aumenta, True)}')
    
    