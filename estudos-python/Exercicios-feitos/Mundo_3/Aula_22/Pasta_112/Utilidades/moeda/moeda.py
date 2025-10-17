from Utilidades.dados.dados import money, doubler, halver, increase, decrease

def moneyator(x):
    info = f'''
    Verified price: {money(x)}
    Doubled price:  {doubler(x)}
    Halved price:   {halver(x)}
    Increase 10%:   {increase(x)}
    Reduced 20%:    {decrease(x)}
    '''
    return info