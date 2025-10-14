#criando duas listas
matriz = [] #lista para guardar todas as linhas da matriz (uma lista de listas).
numeros = [] # lista para guardar temporariamente uma linha da matriz
# loop para criar as 3 linhas / de 0 até 2 já que o 3 não conta.
for c1 in range(0, 3):
    # Loop para preencher cada linha com 3 valores (de 0 a 2..
    for c2 in range(0, 3):
        
    #Pede para digitar um valor para a posição [linha e coluna]
        numeros.append(int(input(f'valor para posição [{c1, c2}]: ')))

    #Adiciona uma cópia da linha completa na matriz
    matriz.append(numeros[:])  # [:] está copiando a lista
    numeros.clear() # Limpando a lista para usar denovo

# Exibindo a matriz formatada:
for c1 in range(0, 3): # Para cada linha
    print() # pula linha
    for c2 in range(0, 3): # Para cada coluna da linha
        print(f'  [{matriz[c1][c2]:^3}]', end='') # mostra o valor formatado dentro de colchetes e centralizado
print() # pula linha
