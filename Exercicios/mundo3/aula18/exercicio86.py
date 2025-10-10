matriz = [[0,0,0], [0,0,0], [0,0,0]]

for a in range(0,3):
    for b in range(0,3):
        matriz[a][b] = int(input(f"Digite um valor para adicionar dentre a matriz {[a], [b]}: "))

for a in range(0,3):
    for b in range(0,3):
       print(matriz[a][b],end=", ")
    print()