numero = int(input("digitee um numero pra descobrir seu fatorial: ")) 
c = numero
f = 1
print(f"calculando {numero}! = ")
while c > 0:
    print(f"{c}")
    print(f"x" if c > 1 else "=")
    f *= c
    c -= 1
print(f"{f}")       