matriz = [[0,0,0],[0,0,0],[0,0,0]]
print ('Escolha 9 valores para adicionar ao tabuleiro (3 X 3)')
for i in range(0,3):
    for j in range(0,3):
        matriz[i][j]=int(input(f'Digite um valor para a posição [{i}] [{j}]: '))
print('Matriz preenchida')

for i in range(0,3):
    for j in range(0,3):
        print(f'[{matriz[i][j]}]', end='')
    print()
    