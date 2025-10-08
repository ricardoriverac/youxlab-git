matriz = []
for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f"digite o valor da posçao [{i + 1},{j+1}]: "))
        linha.append(valor)
    matriz.append(linha)  
print("matriz 3x3:")  
for linha in matriz:
    print(linha)  


