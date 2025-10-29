
def monetario (mo):
    mo= f'{round(mo)},00'
    return mo
def metade (m, formato=False):
    m=m/2
    if formato  is not False:
      return monetario(m)
    

def dobro (d, formato=False):
    d=d*2
    if formato  is not False:
        return monetario(d)
       


def aumento (a, formato=False):
    a=a * 1.10
    
    if formato is not False:
        return monetario(a)
