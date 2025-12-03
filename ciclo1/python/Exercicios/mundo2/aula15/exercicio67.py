while True: 
    numero = int(input("Digite um numero para saber a tabuada (digite um numero negativo para finalizar): "))
    if numero < 0:
        break
    for contas in range(0,11):
        print(f"{numero} x {contas} = {numero*contas}")
print("Finalizado!")
