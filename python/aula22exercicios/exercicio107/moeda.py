def aumentar(n = 0, a = 0):
    txt = float(input(n))
    au = float(input(a))
    return txt + (txt*au/100)
def diminuir(n, d):
    preco = float(input(n))
    des = float(input(d))
    return preco - (preco * des/100)
def dobro(n):
    num = float(input(n))
    return num * 2

def metade(num):
    numero = float(input(num))
    return numero/2