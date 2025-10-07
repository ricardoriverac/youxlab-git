matriz = [[0,0],[0,1],[0,2],
          [1,0],[1,1],[1,2],
          [2,0],[2,1],[2,2]]
for c, v in enumerate(matriz):
    numero = (int(input(f'insira um valor para a posição {v}')))
    matriz[c].clear()
    matriz[c].append(numero)
    if c == 8:
        break
for p,v in enumerate(matriz):
    print(v, end=' ')
    if p == 2 or p == 5:
        print()