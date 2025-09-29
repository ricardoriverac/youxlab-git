while True:
    numero = int(input("que ver a tabuada de qual numero: "))
    if numero < 0:
        break
    for c in range(1,11):
        print(f"{numero} * {c} = {numero*c}")
    numero = int(input("que ver a tabuada de qual numero: "))
print("voce digitou um numero negativo")        
