matriz = [[0,0,0],[0,0,0],[0,0,0]]
somaPar=0
somaTerceira=0
somaTotal=0
maiorSegundaLinha=0
print ('Escolha 9 valores para adicionar ao tabuleiro (3 X 3)')
for i in range(0,3):
    for j in range(0,3):
        matriz[i][j]=int(input(f'Digite um valor para a posição [{i}] [{j}]: '))
print('Matriz preenchida')


for i in range(0,3):
    for j in range(0,3):
        print(f'[{matriz[i][j]}]', end='')
        if matriz [i][j] % 2 == 0:
            somaPar+=matriz[i][j]
        if j == 2:
            somaTerceira+=matriz[i][2]
        if matriz[1]:
            maiorSegundaLinha=(max(matriz[1]))
            
print(f'A soma de todos os valores pares é {somaPar}')         
print(f'a soma de todos os valores da terceria coluna é {somaTerceira}')
print(f'O maior valor da segunda coluna é {maiorSegundaLinha}')