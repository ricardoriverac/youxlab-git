#Teoria da aula 21.

def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f
fator1 = fatorial(6)
fator2 = fatorial(5)
fator3 = fatorial()
print(f'O resultado é {fator1}, {fator2} e {fator3}.')