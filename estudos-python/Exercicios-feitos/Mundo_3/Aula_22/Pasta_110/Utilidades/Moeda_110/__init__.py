def money(n):
    return f'R${n:.2f}'.replace('.',',')

def increase(i, show=False):
    show=True
    return f'R${(i * 1.10):.2f}'.replace('.',',')

def decrease(m, show=False):
    show=True
    return f'R${(m * 0.8):.2f}'.replace('.',',')

def doubler(o, show=False):
    show=True
    return f'R${(o * 2):.2f}'.replace('.',',')

def halfer(p, show=False):
    show=True
    return f'R${(p / 2):.2f}'.replace('.',',')

def moneyator(x):
    info = f'''
    Verified price: {money(x)}
    Doubled price:  {doubler(x)}
    Halved price:   {halfer(x)}
    Increase 10%:   {increase(x)}
    Reduced 20%:    {decrease(x)}
    '''
    return info

if __name__ == "__main__":
    print(moneyator(100))