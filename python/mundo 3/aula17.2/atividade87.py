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
soma_total1 = sum(sum(linha) for linha in matriz)
soma_terceira_coluna = sum(matriz[i][2] for i in range(3))
maior_da_aegunda_linha = max(matriz[1])
print(f""" A soma de todos valores {soma_total1}
o maior valor da segunda linha e {maior_da_aegunda_linha}
a soma da terceira coluna e {soma_terceira_coluna} """)