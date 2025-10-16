def money(n):
    return f'R${n:.0f},00'

def increase(i):
    return f'R${(i * 1.10):.0f},00'

def decrease(m):
    return f'R${(m * 0.8):.0f},00'

def doubler(o):
    return f'R${(o * 2):.0f},00'

def halfer(p):
    return f'R${(p / 2):.0f},00'