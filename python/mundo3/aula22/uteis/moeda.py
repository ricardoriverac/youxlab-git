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
        
        
def aumentar(p, m=True):
    p= p * 1.10
    if m is not False:
      return  monetario(p)
    else:
        return p
def diminuir(p, m=True):
    p= p * 0.87
    if m is not False:
       return monetario(p)
    else:
        return p
        