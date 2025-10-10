matriz= [[0,0,0], [0,0,0], [0,0,0]]
maior=0
soma=0
sum=0
for i in range (3):
    for j in range (3):
        matriz[i][j] = int(input(f'Digite um valor para [{i}] x [{j}]: '))
        if matriz[i][j] % 2 == 0:
               soma+=matriz[i][j]
        if j == 2:
            sum+=matriz[i][j]
        if i == 1:
              if matriz [i][j] > maior:
                maior=matriz[i][j]
for e in matriz: 
            print(e)
print(f'A soma dos valores pares inseridos são {soma}')
print(f'A soma dos valores da terceira coluna são {sum}')
print(f'O maior valor da linha 2 é {maior}')