def money(n):
    return f'R${n:.0f},00'

def increase(i, show=False):
    show=True
    return f'R${(i * 1.10):.0f},00'

def decrease(m, show=False):
    show=True
    return f'R${(m * 0.8):.0f},00'

def doubler(o, show=False):
    show=True
    return f'R${(o * 2):.0f},00'

def halfer(p, show=False):
    show=True
    return f'R${(p / 2):.0f},00'