counte = 0
b=0

def fatorial(a):
    for c in range(a):
        counte = counte + 1
        if counte == 1 :
            b = a
        f = a * b 
        b = a - b

fatorial(4)