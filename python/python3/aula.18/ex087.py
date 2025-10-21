matriz = [[0,0,0], [0,0,0], [0,0,0]]
pares = soma = maior = 0
for i in range(0, 3):
    for j in range(0, 3):
        matriz[i][j] = int(input(f'Digite um valor para a linha {i} e coluna {j}: '))
print('-='*30)        
for i in range(0, 3):
    for j in range(0, 3):
      print(f'[{matriz[i][j]}]', end ='')   
    print()  
    if matriz[i][j] % 2 == 0:
        pares += matriz[i][j]
    if j == 2:
        soma += matriz[i][j]
        if i == 1:
            if j == 0:
                maior = matriz[i][j]
            elif matriz[i][j] >maior:
                maior = matriz[i][j]  
    
soma = soma + matriz[i][j]
print()
print(f'A soma dos valores pares é {pares}')
print(f'A soma dos valores da coluna 3 vale {soma}')
print(f'O maior valor da 2 coluna vale {maior}')
    
