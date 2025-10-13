def aumentar(n = 0, a = 0):
    valor = 0
    valor2 = 0
    ok = False
    ok2 = False
    while True:
        din = float(input(n))
        au = float(input(a))
        if din == 0:
            print('Digite outro valor para calcular o aumento.')
        else:
            valor = din
        if au == 0:
            print('Digite um valor diferente.')
        else:
            valor2 = au
        if valor != 0 and valor2 != 0:
            ok = True
            ok2 = True
            aumento = valor + (valor * valor2/100)    
        if ok and ok2:
            break
    
    return aumento
    

#def diminuir(n):

#def dobro(n):
    #return n * 2

#def metade(n):
    #return n/2