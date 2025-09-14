import math
cateto_oposto = float(input("digite o comprimento do cateto oposto: "))
cateto_adjacente =float(input("digite o comprimento do cateto adjacente: "))
hi = math.hypot(cateto_adjacente,cateto_oposto)
print(f"a hipotenusa vai medir: {hi:.2f} ") 